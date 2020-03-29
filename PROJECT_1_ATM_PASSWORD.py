# PROJECT NAME: ATM MACHINE
# PROJECT DEVELOPER: G.L JAY
# PROOJECT CONTRIBUTORS: G.L JAY

name = input("Please enter your name: ")
atm_pin = str(5252)
pin = ""
no_of_trials = 0
trials_limit = 3
out_of_trials = False
type_of_account = input("please enter your account type: ")
savings_account = "Savings"
current_account = "Current"


while pin != atm_pin and not (out_of_trials):
    if no_of_trials < trials_limit:
        pin = input("Enter your ATM PIN: ")
        no_of_trials += 1
    else:
        out_of_trials = True

if out_of_trials:
    print("Incorrect PIN! \n Maximum Trials reached. \nPlease Proceed to the bank for further instructions ")
else:
    print("PIN Correct")

print("Welcome to Diamond Bank " + name.upper())

print("_____________________________________________________________________________")

if type_of_account == savings_account:
    print("Your withdrawal limit is #20,000")
elif type_of_account == current_account:
    print("Your withdrawal limit is #100,000")
else:
    print("You entered an incorrect account type ")

print("______________________________________________________________________________")


option_typ = "Account Information, Balance Enquiry, Transfer Funds, Withdrawl Funds, Exit"
option_type = ""
option_type1 = "Account Information"
option_type2 = "Balance Enquiry"
option_type3 = "Transfer Funds"
option_type4 = "Withdraw Funds"
option_type5 = "Exit"
user = ""
user_1 = ""
user_2 = ""
amount = str(2000000000)
confirm = ""
fin = ""

print("Here are your options: " + option_typ)

if type_of_account == savings_account:
    option_type = input("Enter an option: ")
    if option_type == option_type1:
        print("Dear " + name.upper() + " Your " +
              type_of_account + " Account Balance is " + amount)
    elif option_type == option_type2:
        print("Dear " + name.upper() + " Your " +
              type_of_account + " Account Balance is " + amount)
    elif option_type == option_type3:
        user_1 = input("Enter Receipients Account Number: ")
        user = input("Enter Recepients Name: ")
        user_2 = input("Enter Amount: ")
        print("You are transferring " + user.upper() + " the sum of #"+user_2)
        confirm = input("confirm with either a \"YES\" or \"NO\"" + ": ")
        if confirm == "YES":
            print("TRANSFER SUCCESSFUL")
        else:
            print("TRANSFER UNSUCCESSFUL")
    elif option_type == option_type4:
        fin = input("Enter Amount: ")
        print("Please Wait....................")
        print("Take Your Cash, Thank You.")
    elif option_type == option_type5:
        print("Good bye " + name +
              " We hope to see you some other time. Have a lovely week!")
    else:
        print("Time Out")
