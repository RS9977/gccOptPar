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

# Example usage:
filename = 'my_program'  # Replace with your file name
instruction_count, total_instructions = count_instructions(filename)
print("Instruction Frequencies:")
for instruction, count in instruction_count.items():
    print(f"{instruction}: {count}")
print(f"Total Instructions: {total_instructions}")
