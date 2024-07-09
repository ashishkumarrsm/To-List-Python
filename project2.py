tasks=[]
def add_task(task):
    tasks.append({"task":task,"Done":False})
def mark_done(task_index):
    if 0<=task_index<len(tasks):
        tasks[task_index]["Done"]=True
    else:
        print("Invalid Operation ")
def delete_task(task_index):
      if 0<=task_index<len(tasks):
        tasks.pop(task_index)
      else:
        print("Invalid Operation ")
def show_task():
    for i,task in enumerate(tasks):
        status="Done" if task["Done" ] else "Note done"
        print(f"[  :->  ].{task['task']} - {status}")
def main():
    while True:
        print("\\nTo-Do List Application")
        print("1. Add Task")
        print("2. Mark Task As Done")
        print("3. Delete Task")
        print("4. Show Task")
        print("5. Exit")

        choice=input("Enter Your choice: ")
        if choice=="1":
            task=input("Enter Task: ")
            add_task(task)
        elif choice=="2":
            task_index=int(input("Enter Task Index to mark as done: "))
            mark_done(task_index)
        elif choice=="3":
             task_index=int(input("Enter Task Index to Delete: "))
             delete_task(task_index)
        elif choice=="4":
            show_task()
        elif choice=="5":
            break;
        else:
            print("Invalide choice")

main()