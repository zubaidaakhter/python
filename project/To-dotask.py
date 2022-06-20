

from re import T
from types import new_class

todo_list = {}
print ("\n ..Welcome to the TO-DO Application..")
def menu():
 todo_menu = "\n1: Enter to add new task to TO-DO List.\n2:Enter to delete TO-DO List.\n3: Enter to update/edit the list\n4: Enter to quit.\n5:Enter to check the TO-DO List:"
 print(todo_menu)





def my_list():
    print("Task:\t\t  Task-Description:")
    for Key in todo_list:
        print("{}\t\t{}".format(Key,todo_list.get(Key)))

# def new_list():
#     file_name = "To-doList.txt"
#     file1 = open(file_name,"a+")
#     file1.close
        

start = True        
while start:
    user_input = input("\nWhat would you like to do? (1,2,3,4,5): ")
    if user_input == "1":
        
        while True:
            with open('TO-DO List.txt' , 'a') as f:
             Task = input("Enter the Task:")
            Description = input("Enter the Task-discription:")
            todo_list[Task] = Description
            f.writelines((Task,':',Description,' \n'))
            menu()
            # new_todo = input ("\n Please enter you new task for the TO-DO list: ")
            # print("\n Your current TO-DO List is{new_todo}.")
            # todo_list.append(new_todo)
            
            
            
            # f.writelines((date,':',task,' \n',':',new_todo))
            break
    elif user_input == "2":
        while True:
            item_name = input("\n Please enter a name of the item you want to delete.")
            try:
                if item_name in todo_list:
                    choice = input("\nAre you sure you want to delete {item_name} from TO-DO List? Y/N")
                    if choice == "y":
                        my_list()
                        todo_list.remove(item_name)
                        print("Your task is deleted.")
                        
                        my_list()
                        break
                else:
                     print("item not found..")
            except Exception:
                   print("Error!! Something went wrong..")

    if user_input == "3":
        while True:
            item_name = input("\n Please enter a name of the item you want to update.")
            try: 
                if item_name in todo_list:
                   choice = input("\nAre you sure you want to update {item_name} from TO-DO List? Y/N")
                if choice == "y":
                    update_item = input("Please enter a updated {item_name} task for the TO-DO list.")
                    index = todo_list,index(item_name)
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





        
    
     