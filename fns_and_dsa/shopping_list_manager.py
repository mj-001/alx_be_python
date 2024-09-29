def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            shopping_list.append(input("Enter the item to add : "))
            # Prompt for and add an item
            pass
        elif choice == '2':
            item_to_remove=input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
            else:
                print(f"{item_to_remove}not found in the list")

            # Prompt for and remove an item
            pass
        elif choice == '3':
            if shopping_list:
                for item in shopping_list:
                    print(item)

            else:
                print("The shopping list is empty")
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()