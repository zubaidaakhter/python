print ("\n ..Welcome to the TO-DO Application..")
todo_menu = "\n1: Enter to add new task to TO-DO List.\n2:Enter to delete TO-DO List.\n3: Enter to update/edit the list\n4: Enter to quit.\n5:Enter to check the TO-DO List:"
print(todo_menu)

todo_list = []

def my_list():
    
    
    for i in todo_list:
        print(title="To DO LIST")
        print("{}\t\t{}".format(i,todo_list.get(i)))
    


start = True        
while start:
    user_input = input("\nWhat would you like to do? (1,2,3,4,5): ")
            
    if user_input == "1":
         with open("List.txt" , 'a') as f:
            new_todo = input ("\n Please enter you new task for the TO-DO list: ")
            task_des = input("\n please enter the task discription:")
            print("\n Your current TO-DO task is:\n " +str(new_todo))
            print("\n Your current Task description:\n " +str(task_des))

            todo_list.append(new_todo)
            todo_list.append(task_des)
            # todo_list[new_todo] = task_des
            f.writelines((new_todo,':',task_des,' \n'))
            
            
          
    elif user_input == "2":
        while True:
            item_name = input("\n Please enter a name of the item you want to delete: ")
           
            if item_name in todo_list:
                choice = input("\nAre you sure you want to delete from TO-DO List? Y/N:")
                if choice == "y":
                        # my_list()
                    todo_list.pop(item_name)
                    print("Your task is deleted.")
                        
                        # my_list()
                    break
            else:
                print("item not found..")
           

    if user_input == "3":
        while True:
            item_name = input("\n Please enter a name of the item you want to update:")
            try: 
                if item_name in todo_list:
                   choice = input("\nAre you sure you want to update  from TO-DO List? Y/N:")
                if choice == "y":
                    update_item = input("Please enter a updated {item_name} task for the TO-DO list.")
                    index = todo_list.index(item_name)
                    todo_list.remove(item_name)
                    todo_list[index]=update_item
                    print("Your task is updated.")
                    my_list()
                    break
                else:
                 print("item not found..")
            except Exception:
               print("Error!! Something went wrong..")

    if user_input == "4":
        ask_user = input("\n Are you sure about quiting the program?(Y/N):")
        if ask_user == "y":
            start = False
    elif user_input == "5":
            my_list()
    
    elif user_input == "":
        print("\n please enter one of the given options..")
    else:
        print("")





        
    
     