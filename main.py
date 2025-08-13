import mysql.connector
from datetime import datetime
import matplotlib.pyplot as plt

# Function to connect to the database


def connect_db():
    return mysql.connector.connect(
        host="localhost", user="root", password="redhat", database="food_service_atm"
    )


# Function to check if a user exists or register a new user


def login_or_register():
    while True:
        name = input("Enter your name: ")
        flag = True
        for i in name:
            if i.isdigit():
                print("Enter the correct name.")
                flag = False
                break
        if flag:
            break

    db = connect_db()
    cursor = db.cursor()

    # Check if the user exists
    cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
    user = cursor.fetchone()

    if user:
        print(f"Welcome back, {name}!")
        user_id = user[0]
    else:
        # Register new user
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        db.commit()
        print(f"Welcome, {name}! You've been registered.")
        user_id = cursor.lastrowid

    db.close()
    return user_id, name


# Function to fetch the menu from the database


def fetch_menu():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM food_items")
    items = cursor.fetchall()
    db.close()
    return items


# Function to display the menu


def display_menu():
    print("\nAvailable Food Items:")
    items = fetch_menu()
    for item in items:
        print(f"{item[0]}. {item[1]} - ₹{item[2]:.2f}")


# Function to place an order


def place_order(user_id):
    total_cost = 0.00  # Initialize the total cost for the user

    while True:
        display_menu()

        food_id = int(
            input("Enter the food item number to order (or 0 to finish ordering): ")
        )
        if food_id == 0:
            break  # Exit the ordering loop

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM food_items WHERE id = %s", (food_id,))
        food_item = cursor.fetchone()

        if not food_item:
            print("Invalid food item. Please try again.")
            db.close()
            continue

        food_name, food_price = food_item[1], food_item[2]
        quantity = int(input(f"How many {food_name}s would you like to order? "))
        cost = food_price * quantity
        total_cost += float(cost)  # Convert Decimal to float

        cursor.execute(
            "INSERT INTO orders (user_id, food_item_id, quantity, total) VALUES (%s, %s, %s, %s)",
            (user_id, food_id, quantity, cost),
        )
        db.commit()
        db.close()

        print(
            f"{food_name} x{quantity} added to your order. Total cost: ₹{float(cost):.2f}"
        )

    return total_cost


# Function to show the user's orders


def show_orders(user_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT o.quantity, f.name, o.total, o.order_date FROM orders o "
        "JOIN food_items f ON o.food_item_id = f.id WHERE o.user_id = %s",
        (user_id,),
    )
    orders = cursor.fetchall()
    db.close()

    if orders:
        print("\nYour Order History:")
        for order in orders:
            print(
                f"{order[1]} x{order[0]} - Total: ₹{order[2]:.2f} (Ordered on: {order[3]})"
            )
    else:
        print("You have no orders yet.")


# Function to display the total bill


def show_bill(total_cost):
    print(f"\nTotal Bill: ₹{total_cost:.2f}")
    print("Thank you for your order!")


# Main function to run the ATM


def plot_sales_chart():
    today = datetime.now().strftime("%Y-%m-%d")  # Get today's date

    db = connect_db()
    cursor = db.cursor()

    # Fetch sales data for the day
    cursor.execute(
        """
        SELECT f.name, SUM(o.quantity) AS total_quantity, SUM(o.total) AS total_sales
        FROM orders o
        JOIN food_items f ON o.food_item_id = f.id
        WHERE DATE(o.order_date) = %s
        GROUP BY f.name
        ORDER BY total_sales DESC
    """,
        (today,),
    )
    sales_data = cursor.fetchall()
    db.close()

    if not sales_data:
        print("\nNo sales data available for today.")
        return

    # Extract data for plotting
    food_names = [row[0] for row in sales_data]
    quantities = [row[1] for row in sales_data]
    sales = [float(row[2]) for row in sales_data]

    print("\nSales Data for Today:")
    for name, quantity, sale in zip(food_names, quantities, sales):
        print(f"{name}: {quantity} units sold, Total: ₹{sale:.2f}")

    # Fixed color palette
    fixed_colors = ["cadetblue", "wheat", "lightcoral", "olive", "plum"]
    colors = [fixed_colors[i % len(fixed_colors)] for i in range(len(food_names))]

    # Plot the chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(food_names, sales, color=colors, alpha=0.85, edgecolor="black")

    # Add value labels on top of each bar
    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            f"₹{bar.get_height():.2f}",
            ha="center",
            fontsize=10,
            color="black",
            fontweight="bold",
        )

    # Chart customization
    plt.title("Sales Chart for Today", fontsize=18, fontweight="bold")
    plt.xlabel("Food Items", fontsize=14, fontweight="bold")
    plt.ylabel("Total Sales (₹)", fontsize=14, fontweight="bold")
    plt.xticks(rotation=45, ha="right", fontsize=12)
    plt.tight_layout()

    # Show the plot
    plt.show()


def main():
    user_id, name = login_or_register()

    print(f"\nHello, {name} 😊.")

    while True:
        print("\nOptions:")
        print("1. Place an order")
        print("2. View order history")
        print("3. View sales chart for today")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            total_cost = place_order(user_id)
            if total_cost > 0:
                show_bill(total_cost)
        elif choice == "2":
            show_orders(user_id)
        elif choice == "3":
            plot_sales_chart()
        elif choice == "4":
            print("Thank you for using the Food Service ATM!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
