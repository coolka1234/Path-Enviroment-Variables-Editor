from multiprocessing import process
import tkinter as tk
import subprocess
import os
def run_script1():
    arg = entry1.get()
    process = subprocess.Popen(["python", "display_enviroment_variables.py", arg], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    display_output(output, error)

def run_script2():
    arg = entry2.get()
    sys_args=arg.split()
    namesSignature = True
    if(len(sys_args) ==4):
        process=subprocess.Popen(["python", "backup.py", (sys_args[0]), (sys_args[1]), sys_args[2], sys_args[3]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    elif(len(sys_args) == 3):
        namesSignature = False
        process=subprocess.Popen(["python", "backup.py", (sys_args[0]), (sys_args[1]), sys_args[2]], stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    elif(len(sys_args) == 2):
            process=subprocess.Popen(["python", "backup.py", (sys_args[0]), (sys_args[1])], stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    else:
        process=subprocess.Popen(["python", "backup.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error=process.communicate()
        display_output(output, error)
        raise Exception("Invalid number of arguments")
    output, error = process.communicate()
    display_output(output, error)

def run_script3():
    arg = entry3.get()
    process = subprocess.Popen(["python", "catalog_analyzer.py", arg], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    display_output(output, error)

def run_script4():
    arg = entry4.get()
    process = subprocess.Popen(["python", "restore.py", arg], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    user_input = "1"  # Replace with the actual input
    process.communicate(input=user_input.encode())
    output, error = process.communicate()
    display_output(output, error)

def display_output(output, error):
    text_output.config(state=tk.NORMAL)
    text_output.insert(tk.END, output.decode("utf-8"))
    text_output.insert(tk.END, error.decode("utf-8"))
    text_output.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Script Runner")

# Create text boxes
entry1 = tk.Entry(root, width=30)
entry2 = tk.Entry(root, width=30)
entry3 = tk.Entry(root, width=30)
entry4 = tk.Entry(root, width=30)
entry5 = tk.Entry(root, width=30)  # Additional user input
entry1.grid(row=0, column=1, padx=10, pady=5)
entry2.grid(row=1, column=1, padx=10, pady=5)
entry3.grid(row=2, column=1, padx=10, pady=5)
entry4.grid(row=3, column=1, padx=10, pady=5)
entry5.grid(row=4, column=1, padx=10, pady=5)
# Create labels
label1 = tk.Label(root, text="Display enviromental variables:")
label2 = tk.Label(root, text="Backup given folder:")
label3 = tk.Label(root, text="Analyze a folder. Output will be created in cwd:")
label4 = tk.Label(root, text="Script 4 Argument:")
label5 = tk.Label(root, text="Additional User Input:")  # Label for additional user input

label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
label2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
label3.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
label4.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
label5.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)  # Grid position for label of additional user input
# Create buttons
button1 = tk.Button(root, text="Run display_enviroment_varaibles.py", command=run_script1)
button2 = tk.Button(root, text="Run backup.py", command=run_script2)
button3 = tk.Button(root, text="Run catalog_analyzer.py", command=run_script3)
button4 = tk.Button(root, text="Run Script 4", command=run_script4)


button1.grid(row=0, column=2, padx=10, pady=5)
button2.grid(row=1, column=2, padx=10, pady=5)
button3.grid(row=2, column=2, padx=10, pady=5)
button4.grid(row=3, column=2, padx=10, pady=5)

text_output = tk.Text(root, height=10, width=60, wrap=tk.WORD)
text_output.grid(row=4, columnspan=3, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
