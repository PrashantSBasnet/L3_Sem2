class BasicCrud:
    
    #because everytime it is executed so you can pass the filename here
    #if there are multiple files, you can have multiple parameters
    def __init__(self, filename):
        self.filename = filename

    def create(self, data):
        
        with open(self.filename, 'a') as file:
            file.write(data + '\n')

    def read(self):
        
        with open(self.filename, 'r') as file:
            return file.readlines()

    def update(self, old_data, new_data):
        
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        
        with open(self.filename, 'w') as file:
            
            for line in lines:
                if old_data in line:
                    file.write(new_data + '\n')
                else:
                    file.write(line)

   
    def delete(self, user_id):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        with open(self.filename, 'w') as file:
            for line in lines:
                if line.split(',')[0].strip() != user_id: #we are trying to delete by id #can this trick be used to check duplicate id??
                    file.write(line)


#I'm just trying to put the code that triggers the fundamental opertaions in different class
#If we have multiple classes, this pattern will be helpful                    
class Driver:
#this is where the first execution starts
    def main():
   
        #object 
        #instantiation
        #we need to pass a value because    __init__ (has parameters see above!!)
        #pass dynamic paths. it means pass it thru variable by taking user input if possible/applicable
        user_db = BasicCrud('/Users/prashant/Documents/employee.txt')
        #think - can you create a separete class to write in a different file?

    
        print("1. Create\n2. Read\n3. Update\n4. Delete\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = input("Enter user id: ")  #can you make it auto incremental while storing? #it should not have duplicates in real-case scenario
            user_name = input("Enter user name: ")
            data = f"{user_id}, {user_name}" #formating to put it as comma separated entry
            user_db.create(data)
            print("Record created successfully.")
        
        elif choice == '2':
            print("User records:")
            print(user_db.read())
        
        elif choice == '3':
            old_data = input("Enter old data to update (id, name): ")
            new_data = input("Enter new data (id, name): ") #asking to enter in this format for the ease of development
            user_db.update(old_data, new_data)
            print("Record updated successfully.")
       
        elif choice == '4':
            user_id = input("Enter user id to delete: ") 
            user_db.delete(user_id)
            print("Record deleted successfully.")
        
        elif choice == '5':
            print("Program Terminated!!")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
