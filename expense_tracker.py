def show_menu():
    print("\n==== EXPENSE TRACKER====")
    print("1.Add Expense")
    print("View Expense")
    print("3.Search Expense")
    print("4.Total Expense")
    print("5.Exit")

    def main(): #defines the main fn which is the entry point of the program
        while True: #this is an infinte loop which keeps on running until you usew break
            show_menu() #calls your fn which displays the menu
            choice=input('oru choic id: ')
            if choice =='1':
                pass
            if choice =='2':
                pass
            if choice =='3':
                pass
            if choice =='4':
                pass
            if choice =='5':
                break
            else:
                print('oru number id monu neen endro akyonthu ulle')
            
if __name__ == "__main__":
    main()