contact ={}

def display_contact():
    # print("Name\t\tContact number")
    for Key in contact:
        print("{}\t\t{}".format(Key,contact.get(Key)))


print("\n...... welcome to the  phonebook management application.....\n ..Use the given menu to create phonebook..\n")   
while True:
    menu = int(input("1.Add a new contact\n 2.Edit a contact\n 3.Delete contact\n 4.Display the contacts\n 5.Search the contacts\n write quit to exit program\n Please enter an option:"))
    
    with open('contact.txt' , 'a') as f:
    if menu == 1:
           name = input ("Enter the contact name:")
           phone = input ("Enter the mobile number:")
           contact[name] = phone
           f.writelines((name,':',phone,' \n'))
     else:
        print("The contact is added succesfully")
   
        if menu == 2:
          edit_contact = input ("Enter the contact to be edited:")
    if edit_contact in contact:
            phone = input("Enter the mobile number:")
            contact[edit_contact]= phone
            display_contact()
    else:
            print("Name is not found in the contact book")

    if menu == 3:
        del_contact = input("enter the contact to be deleted:")
        if del_contact in contact:
            confirm = input ("Do you want to delete this contact, enter yes/no")
            if confirm == 'yes':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in the contact book")
     
    elif menu == 4:
       if not contact:
        print("empty contact book")
       else:
        display_contact()
    if menu == 5:
        with open('contact.txt','r') as f:
            search = input('Search:')
            for i in f:
                if search in i:
                    print(i)
    else:
            print ("Name is not found in the contact book")
    
    if menu == 'quit':  
       break

