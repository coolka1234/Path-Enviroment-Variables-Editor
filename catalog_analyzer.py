from collections import Counter
import os
import subprocess
import json
def process_files(directory):
    results = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            output = subprocess.run([r"C:\Users\krzys\OneDrive\Pulpit\Studia\Semestr4\SkryptoweLab\Lista4\out_put_analyzer\\target\\release\out_put_analyzer.exe"
                           ,os.path.join(directory, filename)], capture_output=True, shell=True, text=True, check=True)
            with open('output.json') as f:
                result = json.load(f)
            results.append(result)
    return results
def process_dict_list(dict_list):
    num_of_characters = 0
    num_of_words = 0
    num_of_rows = 0
    num_of_files=len(dict_list)
    counter_words=Counter()
    counter_chars=Counter()
    for dict in dict_list:
        num_of_characters += dict['num_characters']
        num_of_words += dict['num_words']
        num_of_rows += dict['num_rows']
        counter_words[dict['most_common_word']]+=1
        counter_chars[dict['most_common_char']]+=1
    summary = {
    'num_of_files': num_of_files,
    'num_of_characters': num_of_characters,
    'num_of_words': num_of_words,
    'num_of_rows': num_of_rows,
    'most_common_words': counter_words.most_common(),
    'most_common_characters': counter_chars.most_common()
    }
    with open('summary.json', 'w') as f:
        json.dump(summary, f)
    return summary

if __name__ == "__main__":
    dict_list=process_files(r"C:\Users\krzys\OneDrive\Pulpit\Studia\Semestr4\SkryptoweLab\Lista4")
    process_dict_list(dict_list)