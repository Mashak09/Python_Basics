def show_menu(): # functions are used to organise code so that it can be reused later
    print('\n=== To-Do List menu ===')
    print('1.View Tasks')
    print('2.Add Task')
    print('3.Remove Task')
    print('4.Save Tasks')
    print('5.Load Tasks')
    print('6.Exit')

tasks=[] # idoru list idl nanga users endro tasks ittra ad nokra 

while True:
    show_menu() # we call the function here so that the user can see all the options 
    choice=input('Yed ayeng oru task choose aak monu (1-6)')
    if choice == '6':
        print('Bye Bye Mone')
        break

    if choice == '1':
        if not tasks:#checks if the task 1 list is empty or not
            print('Tasks ille monu!, First tasks add aak ok')
        else:
            print('\n Your Tasks')
            for i, task in enumerate(tasks,1):  #enumerate() gives us both the index and the task of the item
            #starting the list from 1 makes it look natural 
                print(f'{i}.{task}')
            #f string use akr to disply each task with its number

