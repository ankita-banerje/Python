# 🍔 Python Restaurant Ordering System

A beginner-friendly **Python food ordering system** built using loops, dictionaries, conditionals, and user input handling.  
This project simulates a simple restaurant menu where users can:

✅ View the menu  
✅ Order multiple items  
✅ Calculate total bill automatically  
✅ Exit anytime  

Perfect for beginners learning Python fundamentals 🚀

---

## 📌 Features

- Interactive command-line interface
- Multiple item ordering support
- Automatic bill calculation
- Beginner-friendly code structure

---

## 🖥️ Demo

```bash
Type 'menu', 'order', or 'exit': menu
{'pizza': 120, 'burger': 30, 'coffee': 10}

Type 'menu', 'order', or 'exit': order
Enter item: pizza
pizza added. Price: 120
Add more? (yes/no): yes

Enter item: coffee
coffee added. Price: 10
Add more? (yes/no): no

Total bill: 130
```

---

## 📂 Project Structure

```bash
restaurant-ordering-system/
│
├── main.py
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/restaurant-ordering-system.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd restaurant-ordering-system
```

### 3️⃣ Run the Program

```bash
python main.py
```

---

## 🧠 Concepts Used

This project helps practice:

- Python Dictionaries
- `while` loops
- Nested loops
- Conditional statements
- User input handling
- String methods
- Basic billing logic

---

## 💻 Source Code

```python
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
```

---

## 🌟 Future Improvements

- Add quantity support
- Generate receipt
- GUI version using Tkinter
- Store orders in files/database
- Add discount system
- Add payment simulation

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork the repo and improve the project.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Built with Python and curiosity ❤️
