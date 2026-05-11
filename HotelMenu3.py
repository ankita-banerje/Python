menu = {
    "pizza": 120,
    "burger": 30,
    "coffee": 10
}

while True:
    choice = input("\nType 'menu', 'order', or 'exit': ").lower()

    if choice == "menu":
        print(menu)

    elif choice == "order":
        total = 0

        while True:
            item = input("Enter item: ").lower()

            if item in menu:
                total += menu[item]
                print(f"{item} added. Price: {menu[item]}")
            else:
                print("Item not found")

            more = input("Add more? (yes/no): ").lower()

            if more == "no":
                break

        print("Total bill:", total)

    elif choice == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid input")