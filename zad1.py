import os
import sys
def display_environment_variables(params):
    env_vars = os.environ
    filtered_vars = []
    for var in env_vars:
        if all(param.lower() in var.lower() for param in params):
            filtered_vars.append(var)
    filtered_vars.sort()
    for var in filtered_vars:
        print(f"{var}: {env_vars[var]}")
if __name__ == "__main__":
    params = sys.argv[1:]
    display_environment_variables(params)