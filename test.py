import re
import random
def parse_gcc_params(output):

    exceptions_param = ['lazy-modules', 'logical-op-non-short-circuit']

    params = {}
    param_pattern = r"--param=([\w-]+)=<(-?\d+),(-?\d+)>"
    for match in re.finditer(param_pattern, output):
        param_name = match.group(1)
        a = int(match.group(2))
        b = int(match.group(3))
        # Initialize parameter with a random value within the specified range
        value = random.randint(a, b)
        if param_name not in exceptions_param:
            params[param_name] = value

    # For parameters with a list of possible values, choose a random value from the list
    list_pattern = r"--param=([\w-]+)=\[((?:\w+\|)+\w+)\]"
    for match in re.finditer(list_pattern, output):
        param_name = match.group(1)
        possible_values = match.group(2).split('|')
        # Choose a random value from the list of possible values
        if param_name not in params:
            value = random.choice(possible_values)
            if param_name not in exceptions_param:
                params[param_name] = value
        

    # For parameters without specified ranges, assign a random value only if not in param_names
    default_pattern = r"--param=([\w-]+)="
    for match in re.finditer(default_pattern, output):
        param_name = match.group(1)
        # Check if the parameter has already been assigned a value from param_pattern
        if param_name not in params:
            value = random.randint(0, 1000000)  # Assign any random number
            if param_name not in exceptions_param:
                params[param_name] = value

    return params


a = '--param=logical-op-non-short-circuit=<-1,1> True if a non-short-circuit operation is optimal.'

b = parse_gcc_params(a)
print(b)