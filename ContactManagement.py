class Contact:
    
    def __init__(self):
        self.contacts = {  
            "John": 123456789,
            "Smith": 1020304050,
            "Marshall": 6050403020,
            "Roman": 90120484848
        }

    def TakeDetails(self):
        name = input("Enter Name: ")
        no = int(input("Enter Number: "))
        if name in self.contacts:
            print(f" '{name}' Already Exist in Contacts!!")
        else:    
             self.contacts[name] = no  # Store in the dictionary
                
             print(f"Contact '{name}' added successfully!")
                

    def DeleteContact(self):
        name_to_delete = input("Enter Name to Delete: ")
        
        if name_to_delete in self.contacts:
            del self.contacts[name_to_delete]  # Remove from dictionary
            print(f" '{name_to_delete}' deleted successfully.")
        else:
            print(f" '{name_to_delete}' is not found in Contacts.")
            

    def Calling(self):
        to_Call = input("Enter Name to Call: ")
       
        if to_Call in self.contacts:
            print(f"Calling {to_Call} at {self.contacts[to_Call]}...")
        else:
            print(f" '{to_Call}' not found in Contacts.")
    
    def ShowDetails(self):
        if self.contacts:
            print("Contact List:")
            for name,no in self.contacts.items():
                print(f"{name} : {no}")
        else:
            print("No Contacts Available.")
                    

con= Contact()
while True:
    print("\n📱 Contact Management System")
    print("1. Enter New Contact")
    print("2. Show Contacts Details")
    print("3. Call")
    print("4. Delete Contact")
    print("5. Exit")
    

    Choice=input("Enter Your choice:")
    if Choice=="1":
        con.TakeDetails() # Add a new contact
    elif Choice=="2":
        con.ShowDetails() #To Show Contact List
    elif Choice=="3":
        con.Calling() # Call a contact
    elif Choice=="4":
        con.DeleteContact()  # Delete a contact
    elif Choice=="5":
        print("Thanks For Using My Contact Management")
        break  
    else:
        print('Invalid Input!!! Please Choose valid Choice')    
        