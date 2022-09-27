# Steps:
	# 1) First of all, Design your app using any program (like: Sketchbox, microsoft whiteboard)
	# 2) Install & import Required Libraries (tkinter, random, messagebox)
	# 3) Design app using tkinter
	# 4) Create functions to:
		# addTask()
		# updateTasks()
		# deleteSingleTask()
        # deleteAllTasks()
		# sortASC()
		# sortDEC()
		# randomTask()
		# numberOfTask()
		# saveAction()
		# loadActions()
		# exitApp()
		# loadInfo()
  
from tkinter import *
from tkinter import messagebox
import random

tasks = []

def addTask():
    labelDisplay["text"] = ""
    labelDisplay["bg"] = "white"
    
    task = textInput.get()
    if task != "":
        tasks.append(task)
        textInput.delete(0, END)
        updateTasks()
    else:
        labelDisplay["bg"] = "red"
        labelDisplay["text"] = "Please enter task"

def updateTasks():
    tasksListBox.delete(0, END)
    for task in tasks:
        tasksListBox.insert(END, task)
    numTasks = len(tasks)
    tasksCountLabel['text'] = numTasks

def doneTask():
    de = tasksListBox.get(ACTIVE)
    if de in tasks:
        tasks.remove(de)
    updateTasks()

def sortASC():
    tasks.sort()
    updateTasks()

def sortDESC():
    tasks.sort(reverse=True)
    updateTasks()

def randomTask():
    randTask = random.choice(tasks)
    labelDisplay['text'] = randTask
    labelDisplay['bg'] = 'green'

def saveTasks():
    conf = messagebox.askquestion('Save Confirmation', "Save your progress?")
    print(conf)
    if conf == 'yes':
        with open('tasks.txt', 'w') as fileHandle:
            for task in tasks:
                fileHandle.write('%s\n' % task)
    else:
        pass

def loadLastTasks():
    conf = messagebox.askquestion('Load Tasks Confirmation', "Load Last Tasks?")
    print(conf)
    if conf == 'yes':
        with open('tasks.txt', 'r') as fileReader:
            for task in fileReader:
                tasks.append(task)
                updateTasks()
    else:
        pass

def clearTasks():
    conf = messagebox.askquestion('Delete Confirmation', "Are you sure to delete all Tasks?")
    print(conf)
    if conf == 'yes':
        global tasks
        tasks = [] # local
        updateTasks()
    else:
        pass

def exitApp():
    conf = messagebox.askquestion('Exit Confirmation', "Are you sure to Exit?")
    if conf == 'yes':
        root.destroy()
    else:
        pass

def info():
    messagebox.showinfo("Info", "This is To-Do List App to organize your tasks!")

root = Tk()
root.title("To-Do List")
root.config(bg="white", padx=5, pady=5)

appImage = PhotoImage(file=r"C:\Users\future\OneDrive\Desktop\projects\todo-list\logo_todo.png")

labelImage = Label(root, image=appImage, bg="white")
labelImage.grid(columnspan=3, row=0, pady=10)

doneTaskBtn = Button(root, text="Done Task", bg="white", width=13, command=doneTask)
doneTaskBtn.grid(row=1, column=0, padx=2)

sortTasksASCBtn = Button(root, text="Sort Tasks (ASC)", bg="white", width=13, command=sortASC)
sortTasksASCBtn.grid(row=1, column=1, padx=2)

sortTasksDESCBtn = Button(root, text="Sort Tasks (DESC)", bg="white", width=13, command=sortDESC)
sortTasksDESCBtn.grid(row=1, column=2, padx=2)

randomTaskBtn = Button(root, text="Random Task", bg="white", width=13, command=randomTask)
randomTaskBtn.grid(row=2, column=0, padx=2, pady=3)

loadLastTasksBtn = Button(root, text="Load Last Tasks", bg="white", width=13, command=loadLastTasks)
loadLastTasksBtn.grid(row=2, column=1, padx=2)

infoBtn = Button(root, text="Info", bg="white", width=13, command=info)
infoBtn.grid(row=2, column=2, padx=2, pady=3)

saveTasksBtn = Button(root, text="Save", bg="#09bb09", fg="white", width=33, font=("Tahoma 11 bold"), command=saveTasks)
saveTasksBtn.grid(row=3, columnspan=3, padx=3)

toDoListLabel = Label(root, text="To-Do List", font=("Arial 10 bold"), bg="white")
toDoListLabel.grid(row=4, column=0, pady=10, sticky="w")

tasksCountLabel = Label(root, text="0", bg="#0693e3", fg="white")
tasksCountLabel.grid(row=4, column=0, sticky="e", ipadx=3)

tasksListBox = Listbox(root, width=51)
tasksListBox.grid(row=5, columnspan=3)

enterTaskLabel = Label(root, text="Enter task: ", font=("Arial 8"), fg="grey", bg="white")
enterTaskLabel.grid(row=6, column=0, sticky="w", pady=3)

textInput = Entry(root, width=30)
textInput.grid(columnspan=3, row=7, sticky="w", pady=1, ipadx=2, ipady=2)

addTaskBtn = Button(root, text="add", bg="white", fg="green", width=12, command=addTask)
addTaskBtn.grid(row=7, column=2, padx=3)

labelDisplay = Label(root, text="", font=("Arial 10"), bg="white", fg="white")
labelDisplay.grid(columnspan=3, row=8)

bottomFrame = Frame(root, bg="white")
bottomFrame.grid(columnspan=3)

clearTasksBtn = Button(bottomFrame, text="Clear Tasks", bg="white", fg="green", width=16, font=("Arial 13"), command=clearTasks)
clearTasksBtn.grid(column=0, row=9, padx=2, pady=10, ipady=10)

exitBtn = Button(bottomFrame, text="Exit", bg="red", fg="white", width=16, font=("Arial 13"), command=exitApp)
exitBtn.grid(column=1, row=9, padx=2, pady=10, ipady=10)

root.mainloop()