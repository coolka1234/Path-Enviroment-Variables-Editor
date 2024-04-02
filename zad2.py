import os
path = os.environ.get('PATH')
directories = path.split(os.pathsep)
def print_directories():
    for directory in directories:
        print(directory)
def print_executables():
    for directory in directories:
        print(directory)
        files = os.listdir(directory)
        executables = [file for file in files if os.access(os.path.join(directory, file), os.X_OK)]
        for executable in executables:
            print(executable)

if __name__ == "__main__":
    print_directories()
    print_executables()