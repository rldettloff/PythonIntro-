contacts = {'Ryder':'808-866-0093', 'Mom':'360-454-4545', 'Dad':'360-656-6565'}


def display_contact():
    print('Name \t\tContact Number')
    for key in contacts:
        print(f'{key}\t\t{contacts.get(key)}')
while True:
    choice = int(input('1. Add New Contact \n2. Update Contact Info \n3. Delete Contact \n4. List Saved Contacts \n5. Search Saved Contacts \n6. Exit \nEnter Your Choice'))
    if choice == 1:
        name = input('Enter the Contact name')
        phone = input('Enter the mobile number')
        contacts[name] = phone
                 
    elif choice == 2:
        update_contact = input('Enter Contact Name to Edit')
        if update_contact in contacts:
            phone = input('Enter Phone Number')
            contacts[update_contact] = phone
            print('Contact has been Updated')
            display_contact()
        else:
            print('Name Unavailable')
            
    elif choice == 3:
        delete_contact = input('Enter Contact to Delete')
        if delete_contact in contacts:
            confirm_delete = input('Confirm Contact Deletion? (Yes/No)')
            if confirm_delete == 'Yes' or 'yes':
                contacts.pop(delete_contact)
            display_contact
        else:
            print("Not in Contacts List")
            
    elif choice == 4:
        if contacts:
            display_contact()
        else:
            print('No Contacts Available')
            
    elif choice == 5:
        search_name = input('Enter the Contacts Name')
        if search_name in contacts:
            print(f"{search_name}'s contact number is ', {contacts[search_name]}")
        else:
            print("Not in Contacts List")
    else:
        break
    
        
