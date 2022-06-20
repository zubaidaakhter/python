from re import search


contact = {}

def display_contact():
    print("Name:\t\tContact Number:")
    for Key in contact:
        print("{}\t\t{}".format(Key,contact.get(Key)))

print("\n...... welcome to the  phonebook management application.....\n ..Use the given menu to create phonebook..\n")   

while True:
    menu = int(input(" 1.Add a new contact\n 2.search a contact\n 3.Display contact\n 4.Edit the contacts\n 5.Delete the contacts\n 6.quit the  program\n Please enter an option:"))
    if menu == 1:
        with open('contact.txt' , 'a') as f:
         name = input("enter the contact name:")
         phone = input("Enter the phone number:")
         contact[name] = phone
         f.writelines((name,':',phone,' \n'))
    elif menu == 2:
        search_name = input("Enter the contact name:")
        if search_name in contact:
            print(search_name,"'s contact number is" , contact[search_name])
        else:
            print("Name is not found in contact book")
    elif menu == 3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif menu == 4:
        with open('contact.txt' , 'r') as f:
         edit_contact = input("Enter the contact to be edited:")
        if edit_contact in contact:
           phone = input("enter mobile number:")
           contact[edit_contact]=phone
           print("contact updated!!")
           f.writelines()
           display_contact() 
        else:
            print("Name is not found in contact book..")
    elif menu == 5:
        del_contact = input("Enter the contact to be deleted:")
        if del_contact in contact:
            confirm = input ("Do you want to delete this contact, enter yes/no:")
            if confirm == 'yes':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in the contact book")
         
    else:
           break


