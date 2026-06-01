import csv
import os
from datetime import datetime

FILE_NAME = "expense_records.csv"


# Add New Expense
def add_record():
    description = input("Enter expense description: ")
    amount = float(input("Enter amount (₹): "))
    category = input("Enter category (Food/Travel/Shopping/Bills/etc): ")

    date = datetime.now().strftime("%Y-%m-%d")
    expense_id = datetime.now().strftime("%H%M%S")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                ["ID", "Date", "Description", "Amount", "Category"]
            )

        writer.writerow(
            [expense_id, date, description, amount, category]
        )

    print("\nExpense added successfully!\n")


# View All Expenses
def show_records():
    if not os.path.exists(FILE_NAME):
        print("\nNo expense records found.\n")
        return

    print("\n========== ALL EXPENSE RECORDS ==========")

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(
                f"ID: {row['ID']} | "
                f"Date: {row['Date']} | "
                f"Description: {row['Description']} | "
                f"Amount: ₹{row['Amount']} | "
                f"Category: {row['Category']}"
            )

    print()


# Search Expenses by Category
def search_category():
    category = input("Enter category to search: ")

    if not os.path.exists(FILE_NAME):
        print("\nNo expense records found.\n")
        return

    found = False

    print(f"\nExpenses under '{category}' category:\n")

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Category"].lower() == category.lower():
                print(
                    f"{row['Date']} | "
                    f"{row['Description']} | "
                    f"₹{row['Amount']}"
                )
                found = True

    if not found:
        print("No matching records found.")

    print()


# Calculate Total Spending per Category
def category_summary():
    if not os.path.exists(FILE_NAME):
        print("\nNo expense records found.\n")
        return

    totals = {}

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            totals[category] = totals.get(category, 0) + amount

    print("\n========== CATEGORY SUMMARY ==========")

    for category, total in totals.items():
        print(f"{category}: ₹{total:.2f}")

    print()


# Calculate Monthly Spending
def monthly_summary():
    if not os.path.exists(FILE_NAME):
        print("\nNo expense records found.\n")
        return

    monthly_totals = {}
    count = 0

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            month = row["Date"][:7]
            amount = float(row["Amount"])

            monthly_totals[month] = (
                monthly_totals.get(month, 0) + amount
            )

            count += 1

    print("\n========== MONTHLY SPENDING ==========")

    for month, total in monthly_totals.items():
        print(f"{month}: ₹{total:.2f}")

    print(f"\nTotal Expenses Recorded: {count}")
    print()


# Main Program
while True:
    print("========== PERSONAL EXPENSE MANAGER ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expenses by Category")
    print("4. Category-wise Spending")
    print("5. Monthly Spending Summary")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_record()

    elif choice == "2":
        show_records()

    elif choice == "3":
        search_category()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        monthly_summary()

    elif choice == "6":
        print("\nThank you for using Personal Expense Manager!")
        break

    else:
        print("\nInvalid choice. Please try again.\n")
