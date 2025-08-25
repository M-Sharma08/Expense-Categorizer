# Expense Categorizer Application
# A simple personal finance tracker to manage monthly expenses
# Author: Meemansa Sharma
# Date: July 30,2025
from expense_class import Expense
import calendar
import datetime
import random

def main():
    """
    Main function that controls the flow of the expense categorizer application
    """
    print("        💰 Welcome to Expense Categorizer! 💰         ")
    print(" We will help you to add and categorize your expenses,\n analyse your monthly budget amounts \n and help you with a summarized plan and tips.")
    print("-" * 50)
    # Get user's monthly budget with error handling
    try:
        total_budget = int(input("Enter your monthly budget in Rupees: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    # First expense entry
    expense=user_input()
    saving_data(expense)
    # Loop to add multiple expenses
    while True:
        x=input("Do you want to continue adding expense? Please Answer in Yes or No.  ")
        if x in ["YES","yes","Y","Yes","y"]:
                expense=user_input()
                saving_data(expense)
        else:
            break
    print("-" * 50)
    # Category-wise expense report option
    x=input("Do you want to check category wise expense report? ")
    if x in ["YES","yes","Y","Yes","y"]:
         summarizing_data(total_budget)
    print("-" * 50)
    # Complete expense report option
    z=input("Do you want to check whole expense report? ")
    if z in ["YES","yes","Y","Yes","y"]:
         view_data()
    print("-" * 50)   
    print(" Thank You for using Expense Categorizer! ❤️ ")
    # User feedback collection
    while True:
        try:
            x = int(input("Kindly give feedback out of 5: "))
            if 1 <= x <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Enter a valid integer.")

    if x>=3:
        print("Thank You for your valuable feedback. Have a good day. 😊")
    elif x<3:
        print("Thank you for your valuable feedback. We will try to improve the app experience. 🙏🏻")
    print("-" * 50)
    tip()

def user_input():
    """
    Function to collect expense details from user
    Returns: Expense object with user-provided data
    """
    # Fetching data from user
    expense_name=input("Enter amount spent at:  ")
    expense_amount=int(input("Enter amount spent in Rupees:  "))
    categories=["Home 🏡","Commute 🚗","Work 🏢","Food 🥪","Shopping 🛍️","Miscellaneous 🏷️"]
    for i, n in enumerate(categories):
            print(f" {i+1} : {n}")
    input_category=int(input("Enter the category option:  "))
    expense_category=categories[input_category-1]
    expense=Expense(name=expense_name,category=expense_category,amount=expense_amount)
    print(expense)
    return(expense)


def saving_data(expense:Expense):
    """
    Function to save expense data to CSV file
    Parameters: expense - Expense object to be saved
    """
    # Saving the data in csv file
    with open("expense_categorizer_data.csv","a",encoding="utf-8") as f:
         f.write(f"{expense.name},{expense.amount},{expense.category}\n")
         print("Record Updated! ✅")


def summarizing_data(budget):
    """
    Function to analyze expenses by category and calculate budget insights
    Parameters: budget - user's monthly budget amount
    """
    expenses: list[Expense] = []
    with open("expense_categorizer_data.csv", "r",encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)
        # Group expenses by category
        amount_by_category = {}
        for expense in expenses:
            key = expense.category
            if key in amount_by_category:
                amount_by_category[key] += expense.amount
            else:
                amount_by_category[key] = expense.amount

        for key, amount in amount_by_category.items():
                print(f"  {key}: Rs.{amount:.2f}")
        else:
            pass

    # Calculate and display budget analysis   
    total_spent = sum([x.amount for x in expenses])
    print(f" Total Spent 💸: Rs.{total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f" Budget Remaining 💳: Rs.{remaining_budget:.2f}")

    # Calculate daily budget for remaining days in month
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    if remaining_days > 0:
         daily_budget = remaining_budget / remaining_days
    else:
         daily_budget = 0
    print(f" Budget Per Day 💵: Rs.{daily_budget:.2f}")


def view_data():
     """
    Function to display all expense records in tabular format
    """
     print(f"{'Name':<15}{'Amount':<15}{'Category':<15}")
     print("-" * 50)
     with open ("expense_categorizer_data.csv", "r",encoding="utf-8") as f:
          x=f.readlines()
          for i in x:
               fields=i.strip().split(",")
               n,a,c=fields
               print(f"{n:<15}{a:<15}{c:<15}")

def tip():
     """
    Function that randomizes the quote of the day
    """
     a=["Budgeting only has one rule, do not go over the budget.","Budgeting your money is the key to having enough.",
        "A budget is telling your money where to go instead of wondering where it went.",
        "When money realises its in good hands it wants to stay and multiply in those hands.",
        "Budgeting is not for those without money but for everyone who wants to ensure that their money is enough."]
     print("TIP Of The Day: ",random.choice(a))
     
# Run the main function when script is executed
if __name__ == "__main__":
    main()
