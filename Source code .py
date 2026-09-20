balance = 15000.00

while True:
    print("\n=== ATM SIMULATOR (Method 1) ===")
    print("1. Balance Check")
    print("2. Cash Deposit")
    print("3. Cash Withdraw")
    print("4. Exit")
    
    choice = input("Apna option chunein (1-4): ")

    if choice == '1':
        print(f"Aapka balance hai: ₹{balance}")
        
    elif choice == '2':
        dep_amount = float(input("Deposit amount daalein: ₹"))
        balance += dep_amount
        print(f"₹{dep_amount} deposit ho gaya. Naya balance: ₹{balance}")
        
    elif choice == '3':
        with_amount = float(input("Withdraw amount daalein: ₹"))
        if with_amount <= balance:
            balance -= with_amount
            print(f"₹{with_amount} nikal gaye. Naya balance: ₹{balance}")
        else:
            print("Chhama karein! Aapke account me itne paise nahi hain.")
            
    elif choice == '4':
        print("ATM use karne ke liye dhanyawad. Bye!")
        break  # Isse loop turant ruk jayega
        
    else:
        print("Galat option! Kripya 1 se 4 ke beech")


balance = 8000.00
is_running = True  # Yeh flag loop ko chalata hai

while is_running:
    print("\n=== ATM SIMULATOR (Method 2) ===")
    print("1. Check Balance")
    print("2. Add Money")
    print("3. Take Money")
    print("4. Exit")
    
    choice = int(input("Option number enter karein: "))

    if choice == 1:
        print(f"Current Balance: ₹{balance}")
    elif choice == 2:
        amount = float(input("Kitne paise deposit karne hain? ₹"))
        balance += amount
        print("Paisa jama ho gaya!")
    elif choice == 3:
        amount = float(input("Kitne paise nikalne hain? ₹"))
        if amount <= balance:
            balance -= amount
            print("Transaction successful!")
        else:
            print("Insufficient funds!")
    elif choice == 4:
        print("Thank you! Visit again.")
        is_running = False  # Condition False hote hi agli baar loop nahi chalega
    else:
        print("Invalid Choice!")
      
        
        balance = 5000.00
wrong_attempts = 0  # Galat inputs ginne ke liye

while wrong_attempts < 3:
    print("\n=== ATM SIMULATOR (Method 3) ===")
    print("[1] Balance | [2] Deposit | [3] Withdraw | [4] Exit")
    choice = input("Select karein: ")

    if choice == '1':
        print(f"Available Balance: ₹{balance}")
        wrong_attempts = 0 # Sahi input par counter reset
    elif choice == '2':
        balance += float(input("Deposit Amount: ₹"))
        wrong_attempts = 0
    elif choice == '3':
        amt = float(input("Withdraw Amount: ₹"))
        if amt <= balance:
            balance -= amt
            print("Cash collected.")
        else:
            print("No enough money.")
        wrong_attempts = 0
    elif choice == '4':
        print("Logged out successfully.")
        break
    else:
        wrong_attempts += 1
        remaining = 3 - wrong_attempts
        print(f"Galat option! Aapke paas {remaining} mauke bache hain.")

if wrong_attempts == 3:
    print("\nBaar-baar galat input dene ke karan aapka session lock kar diya gaya ha")


  balance = 25000.00
user_wants_to_continue = 'y'

# The loop runs as long as user_wants_to_continue remains 'y' or 'Y'
while user_wants_to_continue.lower() == 'y':
    print("\n=== ATM SIMULATOR (Method 4) ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    
    choice = input("Enter your choice (1-3): ")

    # Conditional statement execution based on choice
    if choice == '1':
        print(f"Your total balance is: ₹{balance:.2f}")
        
    elif choice == '2':
        amount = float(input("Enter deposit amount: ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount:.2f} credited to your account.")
        else:
            print("Invalid input amount.")
            
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: ₹"))
        if amount > balance:
            print("Declined! Insufficient account balance.")
        elif amount <= 0:
            print("Invalid input amount.")
        else:
            balance -= amount
            print(f"₹{amount:.2f} successfully withdrawn.")
            
    else:
        print("Invalid menu choice.")

    # Loop Control Step: This decides whether the loop will run again
    user_wants_to_continue = input("\nDo you want to perform another transaction? (y/n): ")

# This line prints only after the user chooses 'n' and exits the loop
print("\nSession ended. Thank you for using our ATM service !")

        



































































              
