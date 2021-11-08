import sys

def about():
  print("""About: A simple text based tip calculator developed primarily for a small project to learn python.""")

def tip_calculator():
  total_bill = float(input("What was the total bill?\n$"))
  tip_percentage = int(input("What percentage tip would you like to give? Example Format: 10, 12, or 15?\n"))
  people_split = int(input("How many people to split the bill?\n"))

  calculation = (total_bill / people_split) * (tip_percentage / 100 + 1)

  answer = round(calculation, 2)
  answer = "{:.2f}".format(calculation)

  print(f"Each person should pay ${answer}")
  print("Thank you for using Tip Calculator!")

def main():

  print("Welcome to Tip Calculator v1!")
  input_selection = input("Enter 1 to start Tip Calculator,\n Enter 2 to read about,\nEnter 3 to exit program.\n")

  while True:
    if input_selection == "1":
      tip_calculator()
      break
    elif input_selection == "2":
      about()
      break
    elif input_selection == "3":
      sys.exit()
    else:
      input_selection = input("That is not a valid selection.\nEnter 1 to start Tip Calculator,\nEnter 2 to read about,\nEnter 3 to exit program.\n")
      continue
 

if __name__ == "__main__":
  main()