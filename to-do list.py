import tkinter
import tkinter .messagebox
import pickle

# for build the to-do list structure .
window = tkinter.Tk()
window.title("Own to do list")

# function for add the task if we click on add to task button.
def task_adding():
    todo=task_add.get()
    if todo !="":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)

    else:
        tkinter.messagebox.showwarning(title="Attention !!",message="To add a task, Please enter some task")

# function for remove the task if we click on remove to task button.
def task_removing():
    try:
        index_todo=list_frame.curselection()[0]
        list_frame.delete(index_todo)

    except:
        tkinter.messagebox.showwarning(title="Attention !!",message="To delete a task you must select the task")

# function for task loading
def task_loading():
    try:
        todo_list=pickle.load(open("tasks.dat","rb"))
        list_frame.delet(0,tkinter.END)
        for todo in tasks:
            list_frame.insert(tkinter.END,todo)

    except:
        tkinter.messagebox.showwarning(title="Attention !!",message="Cannot find task.dat")


# function for save task
def task_save():
    todo_list=list_frame.get(0,list_frame.size())
    pickle.dump(todo_list,open("tasks.dat","wb"))




list_frame=tkinter.Frame(window)
list_frame.pack()

# for maintaining the height and width of the to-do list 
todo_box=tkinter.Listbox(list_frame,height=20,width=50)
todo_box.pack(side=tkinter.LEFT)

# if the list is too much long then there should be a scroll bar ,so for scroll bar we use:
scroller=tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)

# now built the box where we put the task which is going to be add.
todo_box.config(yscrollcommand=scroller.set)
# scroller.config(command=list_frame.yview)

# Now built the function for entering the task.
task_add=tkinter.Entry(window,width=70)
task_add.pack()

# Now its time to add button for adding task and deleting task or whatever.
add_task_button=tkinter.Button(window,text="CLICK TO ADD TASK",font=("arial",20,"bold"),background="pink",width=40,command=task_adding)
add_task_button.pack()

remove_task_button=tkinter.Button(window,text="CLICK TO REMOVE TASK",font=("arial",20,"bold"),background="yellow",width=40,command=task_removing)
remove_task_button.pack()

load_task_button=tkinter.Button(window,text="CLICK TO LOAD TASK",font=("arial",20,"bold"),background="green",width=40,command=task_removing)
load_task_button.pack()

save_task_button=tkinter.Button(window,text="CLICK TO SAVE TASK",font=("arial",20,"bold"),background="red",width=40,command=task_save)
save_task_button.pack()


window.mainloop()