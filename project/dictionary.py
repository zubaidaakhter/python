print ("\n ..Welcome to the Dictionary Application..")
# menu = "\n1: Enter to add new words.\n2:Enter to delete words.\n3: Enter to update/edit an word \n4:Enter to check Dicrionary \n5:Enter to quit."
# print(menu)

dictionary={}

def display_word():
    print("word:\t\tDiscription:")
    for w in dictionary:
        print("{}\t\t{}".format(w,dictionary.get(w)))
 
while True:
    menu_user = int(input("\n1: Enter to add new words.\n2:Search a new words.\n3: Enter to dispaly word \n4:Enter to update/edit an word \n5:Delete the word.\n please enter an option:"))
    if menu_user == 1:
        with open('dictionary.txt' , 'a') as f:
         word = input("enter a new word:")
         discription = input("Enter the discription of the word:")
         dictionary[word] = discription
         f.writelines((word,':',discription,' \n'))
    elif menu_user == 2:
        search_name = input("Enter a word:")
        if search_name in dictionary:
            print(search_name,"'s word is" , dictionary[search_name])
        else:
            print("Name is not found in dictionary")
    elif menu_user == 3:
        if not dictionary:
            print("empty dictionary")
        else:
            display_word()
    elif menu_user == 4:
        with open('dictionary.txt' , 'r') as f:
         edit_word = input("Enter the word to be edited:")
        if edit_word in dictionary:
           discription = input("enter discription:")
           dictionary[edit_word]=word
           print("word updated!!")
           f.writelines()
           display_word() 
        else:
            print("Name is not found in contact book..")
    elif menu_user == 5:
        del_word = input("Enter the contact to be deleted:")
        if del_word in dictionary:
            confirm = input ("Do you want to delete this word, enter yes/no:")
            if confirm == 'yes':
                dictionary.pop(del_word)
            display_word()
        else:
            print("word  not found in the Dictionary")
         
    else:
           break


