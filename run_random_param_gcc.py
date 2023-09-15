import subprocess
import re
import random
import tempfile
import os

def parse_gcc_params(output):
    params = {}
    param_pattern = r"--param=([\w-]+)=<(-?\d+),(-?\d+)>"
    exceptions_param = ['lazy-modules', 'logical-op-non-short-circuit']
    for match in re.finditer(param_pattern, output):
        param_name = match.group(1)
        if param_name not in exceptions_param:
            a = int(match.group(2))
            b = int(match.group(3))
            # Initialize parameter with a random value within the specified range
            value = random.randint(a, b)
            params[param_name] = value

    # For parameters with a list of possible values, choose a random value from the list
    list_pattern = r"--param=([\w-]+)=\[((?:\w+\|)+\w+)\]?"
    for match in re.finditer(list_pattern, output):
        param_name = match.group(1)
        if param_name not in exceptions_param:
            possible_values = match.group(2).split('|')
            # Choose a random value from the list of possible values
            if param_name not in params:
                value = random.choice(possible_values)
                params[param_name] = value
        

    # For parameters without specified ranges, assign a random value only if not in param_names
    default_pattern = r"--param=([\w-]+)="
    for match in re.finditer(default_pattern, output):
        param_name = match.group(1)
        if param_name not in exceptions_param:
            # Check if the parameter has already been assigned a value from param_pattern
            if param_name not in params:
                value = random.randint(0, 1000000)  # Assign any random number
                params[param_name] = value

    return params

def compile_with_gcc(source_file, output_binary, gcc_params):
    try:
        # Build the GCC command with parameters
        gcc_command = ["gcc", "-S", "-O3", "-o", output_binary]
        for param_name, param_value in gcc_params.items():
            gcc_command.append(f"--param={param_name}={param_value}")
        gcc_command.append(source_file)

        # Run GCC to compile the program
        subprocess.check_call(gcc_command)

        print(f"Compilation successful. Binary '{output_binary}' generated.")

    except subprocess.CalledProcessError as e:
        print("Error during compilation:")
        print(e.output)

def count_instructions(filename):
    # Initialize a dictionary to store instruction frequencies
    instruction_count = {}

    # Initialize a variable to store the overall number of instructions
    total_instructions = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove leading and trailing whitespace and split the line into words
                words = line.strip().split()

                # Check if the line starts with a dot (.) or is empty
                if not words or words[0].startswith('.') or words[0][-1]==':':
                    continue  # Ignore this line

                # Extract the first word (instruction) from the line
                instruction = words[0]

                # Update the instruction count dictionary
                if instruction in instruction_count:
                    instruction_count[instruction] += 1
                else:
                    instruction_count[instruction] = 1

                # Increment the overall instruction count
                total_instructions += 1

        # Return the instruction count dictionary and total number of instructions
        return instruction_count, total_instructions

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}, 0



def main():
    try:
        # Run `gcc --help=params` and capture the output
        output = subprocess.check_output(["gcc", "--help=params"], stderr=subprocess.STDOUT, universal_newlines=True)
        # Parse the output to extract parameter names and descriptions
        gcc_params = parse_gcc_params(output)

        # Input source code file name
        source_file = "test.c"

        # Output binary name
        output_binary = "my_program"

        # Compile the program with GCC using the initialized parameters
        compile_with_gcc(source_file, output_binary, gcc_params)

        filename = 'my_program'  # Replace with your file name
        instruction_count, total_instructions = count_instructions(filename)
        print("Instruction Frequencies:")
        for instruction, count in instruction_count.items():
            print(f"{instruction}: {count}")
        print(f"Total Instructions: {total_instructions}")



    except subprocess.CalledProcessError as e:
        print("Error running 'gcc --help=params':")
        print(e.output)

if __name__ == "__main__":
    main()
