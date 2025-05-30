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
