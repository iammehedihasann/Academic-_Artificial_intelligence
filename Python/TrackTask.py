import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x600")

# Prevent window from being resized
root.resizable(False, False)
root.config(bg="#ffffff") # Light gray background


def add_task():
    task = task_entry.get()
    if task:
        add_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        print("Please enter a task!")


# Delete Task
def delete_task():
    try:
        selected_index = add_listbox.curselection()[0]
        add_listbox.delete(selected_index)
    except IndexError:
        print("Please select a task to delete")

# delete all task
def clear_all_tasks():
    add_listbox.delete(0, tk.END)


# Markable task
def mark_complete():
    try:
        selected_index = add_listbox.curselection()[0]
        task = add_listbox.get(selected_index)
        
        # Check if task is complete already marked complete
        if not task.startswith("✓ "):
            # Mark as complete with checkmark
            add_listbox.delete(selected_index)
            add_listbox.insert(selected_index,"✓ "+ task)
            add_listbox.itemconfig(selected_index, fg="gray")
    except IndexError:
        print("Please  select a task to mark as complete")
        
 #header Frame 
header_frame = tk.Frame(root, bg="#4a7c9e")
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="📝 My To-Do List",font=("Arial", 18, "bold"),bg="#4a7c9e",fg="white")
header_label.pack(pady=15)

# input Frame 

input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack( pady=20)

# Add some typing widgets
task_entry = tk.Entry(input_frame, width=35, font=("Arial", 12), bd=2, relief=tk.GROOVE)
task_entry.pack(side=tk.LEFT, padx=10, ipady=5)

#  Adding button 
add_button = tk.Button(input_frame, text="Add task", width=12,font=("Arial",10,"bold"),
                       bg="#5cb85c", fg="white",
                       activebackground="#4cae4c",
                       bd=0, cursor="hand2",
                       command=add_task)
add_button.pack(side=tk.LEFT)

# list Frame
list_frame = tk.Frame(root, bg="#f0f0f0")
list_frame.pack(padx=10, pady=20)


scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)

add_listbox = tk.Listbox(list_frame, width=55, height=14,
                         font=("Arial", 11),
                         bd=2,relief=tk.SUNKEN,
                         selectmode=tk.SINGLE,
                         activestyle='none',
                         bg="white",
                         selectbackground="#d4e6f1",
                         selectforeground="black",
                         yscrollcommand=scrollbar.set)

scrollbar.config(command=add_listbox.yview)

add_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# button frame
button_frame = tk.Frame(root,bg="#f0f0f0")
button_frame.pack(pady=20)


# mark button 
mark_button = tk.Button(button_frame, text="✓ Mark Complete", width=15, 
                       font=("Arial", 10, "bold"),
                       bg="#5bc0de", fg="white",
                       activebackground="#46b8da",
                       bd=0, cursor="hand2",
                       command=mark_complete)
mark_button.grid(row=0, column=0, padx=8)

# delete button
delete_button = tk.Button(button_frame, text="✕ Delete Task", width=15, 
                         font=("Arial", 10, "bold"),
                         bg="#d9534f", fg="white",
                         activebackground="#c9302c",
                         bd=0, cursor="hand2",
                         command=delete_task)
delete_button.grid(row=0, column=1, padx=8)

# clear button 
clear_button = tk.Button(button_frame, text="Clear All", width=15, 
                        font=("Arial", 10, "bold"),
                        bg="#f0ad4e", fg="white",
                        activebackground="#ec971f",
                        bd=0, cursor="hand2",
                        command=clear_all_tasks)
clear_button.grid(row=0, column=2, padx=8)
# footer section

footer_label = tk.Label(root, text="Select a task and use buttons to manage it", font=("Arial", 9, "italic"), bg="#f0f0f0", fg="#666666")
footer_label.pack(side=tk.BOTTOM, pady=10)


root.mainloop()

