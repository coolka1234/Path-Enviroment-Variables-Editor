import tkinter as tk
import subprocess

def run_script1():
    arg = entry1.get()
    process = subprocess.Popen(["python", "display_enviroment_variables.py", arg], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    display_output(output, error)

def run_script2():
    arg = entry2.get()
    arg1,arg2,arg3=arg.split()
    process = subprocess.Popen(["python", "backup.py", arg1, arg2, arg3], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    display_output(output, error)

def run_script3():
    arg = entry3.get()
    process = subprocess.Popen(["python", "script3.py", arg], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    display_output(output, error)

def run_script4():
    arg = entry4.get()
    process = subprocess.Popen(["python", "script4.py", arg], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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

entry1.grid(row=0, column=1, padx=10, pady=5)
entry2.grid(row=1, column=1, padx=10, pady=5)
entry3.grid(row=2, column=1, padx=10, pady=5)
entry4.grid(row=3, column=1, padx=10, pady=5)

# Create labels
label1 = tk.Label(root, text="Script 1 Argument:")
label2 = tk.Label(root, text="Script 2 Argument:")
label3 = tk.Label(root, text="Script 3 Argument:")
label4 = tk.Label(root, text="Script 4 Argument:")

label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
label2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
label3.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
label4.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)

# Create buttons
button1 = tk.Button(root, text="Run Script 1", command=run_script1)
button2 = tk.Button(root, text="Run Script 2", command=run_script2)
button3 = tk.Button(root, text="Run Script 3", command=run_script3)
button4 = tk.Button(root, text="Run Script 4", command=run_script4)

button1.grid(row=0, column=2, padx=10, pady=5)
button2.grid(row=1, column=2, padx=10, pady=5)
button3.grid(row=2, column=2, padx=10, pady=5)
button4.grid(row=3, column=2, padx=10, pady=5)

# Create output text box
text_output = tk.Text(root, height=10, width=60, wrap=tk.WORD)
text_output.grid(row=4, columnspan=3, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
