def show_menu(): # functions are used to organise code so that it can be reused later
    print('\n=== To-Do List menu ===')
    print('1.View Tasks')
    print('2.Add Task')
    print('3.Remove Task')
    print('4.Save Tasks')
    print('5.Load Tasks')
    print('6.Exit')
    print('7.Mark as completed')

tasks = [{"text": "Buy milk", "done": False}, {"text": "Call Ammi", "done": True}] # idoru dictionary idl nanga users endro tasks ittra ad nokra 

while True:
    show_menu() # we call the function here so that the user can see all the options 
    choice = input('Yed ayeng oru task choose aak monu (1-7): ') # changed to 7 since we have 7 options
    if choice == '6':
        print('Bye Bye Mone')
        break

    if choice == '1':
        if not tasks: # checks if the task list is empty or not
            print('Tasks ille monu!, First tasks add aak ok')
        else:
            print('\n Your Tasks')
            for i, task in enumerate(tasks, 1):  # enumerate() gives us both the index and the task of the item
                # starting the list from 1 makes it look natural 
                status = "✅" if task["done"] else "❌"
                print(f'{i}. [{status}] {task["text"]}') # f string use akr to display each task with its number

    elif choice == '2':
        task = input('nikk endro task benu, Add aak monu: ')
        tasks.append({"text": task, "done": False}) # this is a built-in method which adds the task to the end of the tasks list
        print(f'task added: {task}')

    elif choice == '3':
        if not tasks: # checks if the task is empty
            print('endum task ille remove akogu mone')
        else:
            print('\nYour Tasks:')
            for i, task in enumerate(tasks, 1): # enumerate() endro akr chenneng nikk tasks along with index thand and starts with 1
                status = "✅" if task["done"] else "❌"
                print(f'{i}. [{status}] {task["text"]}') # f string nikk clean formatting aakr like index um pinne task ro ok

            try:
                task_num = int(input('nikk yed task remove akonu adro number id: ')) # ask the user to input the task they want to remove
                if 1 <= task_num <= len(tasks): # the task should be inside the number of tasks
                    removed = tasks.pop(task_num - 1) # removes the task using pop 
                    print(f'task removed: {removed["text"]}')
                else:
                    print('task number invalid id')
            except ValueError: # valueerror chenneng neen number enter akonu instead of text like abc appa id error kaatr
                print('nikk number idogu chenno naan ')

    elif choice == '4':
        with open("tasks.txt", 'w') as file: # opens and creates tasks.txt as a written file
            for task in tasks: 
                file.write(f"{task['text']}|{task['done']}\n") # writes each task's text and status separated by |
            print("Tasks have been saved to 'tasks.txt'")

    elif choice == '5':
        try:
            with open("tasks.txt", 'r') as file: # opens the file in read mode
                tasks = [] # clear current tasks
                for line in file:
                    if line.strip(): # skip empty lines
                        text, done = line.strip().split("|")
                        tasks.append({"text": text, "done": done == "True"})
                print("Tasks loaded from 'tasks.txt'")
        except FileNotFoundError:
            print('tasks.txt ude ille mone ad first save ak')

    elif choice == '7':
        if not tasks: # checks if the tasks are empty
            print('tasks lists empty monu complete akogu endum ille')
        else:
            print('\nyour tasks') # if there are tasks it shows it
            for i, task in enumerate(tasks, 1): # enumerate as told before is use to show the task along with the index
                status = "✅" if task["done"] else "❌"
                print(f'{i}. [{status}] {task["text"]}')

            try:
                task_num = int(input('Enter the task number you want as completed: '))
                if 1 <= task_num <= len(tasks): # checks if the entered task is within the amount of tasks thats there
                    if tasks[task_num - 1]["done"]:
                        print('task id first ge complete air monu')
                    else:
                        tasks[task_num - 1]["done"] = True
                        print('task marked as completed')
                else:
                    print('Invalid Task Number')
            except ValueError:
                print('number id monu neen endro itto ulle')

    else:
        print('Invalid choice monu, 1-7 vare option id')