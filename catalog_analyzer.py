import os
import subprocess
import json
def process_files(directory):
    results = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            output = subprocess.run([r"C:\Users\krzys\OneDrive\Pulpit\Studia\Semestr4\SkryptoweLab\Lista4\out_put_analyzer\\target\\release\out_put_analyzer.exe"
                           ,os.path.join(directory, filename)], capture_output=True, shell=True)
            result = json.loads(output.stdout)
            results.append(result)
    return results

# Example usage
if __name__ == "__main__":
    process_files(r"C:\Users\krzys\OneDrive\Pulpit\Studia\Semestr4\SkryptoweLab\Lista4")