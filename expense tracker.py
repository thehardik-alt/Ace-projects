# Simple Expense Tracker

expenses = []

while True:
    print("\n1. Add Expense | 2. View Expenses | 3. Show Summary | 4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        description = input("Description: ")

        # Save the expense as a dictionary
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
        }
        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("\n--- All Expenses ---")
            for item in expenses:
                print(
                    f"Amount: {item['amount']} | Category: {item['category']} | Description: {item['description']}"
                )

    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total_spent = 0
            category_totals = {}

            # Calculate total and category breakdown
            for item in expenses:
                total_spent += item["amount"]
                cat = item["category"]

                if cat in category_totals:
                    category_totals[cat] += item["amount"]
                else:
                    category_totals[cat] = item["amount"]

            print(f"\nTotal amount spent: {total_spent}")
            print("\nAmount spent in each category:")
            for cat, amt in category_totals.items():
                print(f"- {cat}: {amt}")

            # Find the highest spending category
            highest_category = ""
            highest_amount = 0

            for cat, amt in category_totals.items():
                if amt > highest_amount:
                    highest_amount = amt
                    highest_category = cat

            print(
                f"\nHighest spending category: {highest_category} ({highest_amount})"
            )

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, please choose between 1 and 4.")
