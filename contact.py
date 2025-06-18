contacts={}
def add_contact():
    name=input("Name:")
    phone=input("Phone:")
    email=input("Email:")
    address=input("Address:")
    contacts[name]={"Phone":phone,"Email":email,"Address":address}

def view_contacts():
    for name,info in contacts.items():
        print(f"\n Name:{name}")
        for key,value in info.items():
            print(f"{key}:{value}")

def search_contact():
    search_name=input("Enter name to search:")
    if search_name in contacts:
        print(contacts[search_name])
    else:
        print("Contact not found")

def update_contact():
    name=input("Enter name to update:")
    if name in contacts:
        contacts[name]["Phone"]=input("New Phone:")
        contacts[name]["Email"]=input("Email:")
        contacts[name]["Address"]=input("New Address:")
    else:
        print("Contact not found.")


def delete_contact():
    name=input("Enter name to delete:")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n---CONTACT BOOK---")
    print("1.Add Contact\n2. View Contacts\n3. Search Contact\n4.Update Contact\n5. Delete Contact\n6. Exit")
    choice=input("Choose an option:")

    if choice=='1':
        add_contact()
    elif choice=='2':
        view_contacts()
    elif choice=='3':
        search_contact()
    elif choice=='4':
        update_contact()
    elif choice=='5':
        delete_contact()
    elif choice=='6':
        break
    else:
        print("Invalid Choice.")
