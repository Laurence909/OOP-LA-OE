#OE2
class PhoneClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

def main():
    num_objects = int(input("How many objects do you want to create? "))
    
    objects_list = []

    for i in range(num_objects):
        name = input(f"Enter name for object {i + 1}: ")
        obj = PhoneClass(name)
        objects_list.append(obj)

    while True:
        print("\nMenu:")
        print("1. See list")
        print("2. Delete an object")
        print("3. Update an object")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            # See list
            print("\nObjects list:")
            for idx, obj in enumerate(objects_list):
                print(f"{idx + 1}. {obj}")

        elif choice == '2':
            # Delete an object
            index = int(input("Enter the number of the object to delete: ")) - 1
            if 0 <= index < len(objects_list):
                del objects_list[index]
                print("Object deleted.")
            else:
                print("Invalid index.")

        elif choice == '3':
            # Update an object
            index = int(input("Enter the number of the object to update: ")) - 1
            if 0 <= index < len(objects_list):
                new_name = input("Enter new name: ")
                objects_list[index].name = new_name
                print("Object updated.")
            else:
                print("Invalid index.")

        elif choice == '4':
            # Exit
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
