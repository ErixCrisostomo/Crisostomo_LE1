#Crisostomo_Erix Steven L.

import os

user_database = {}

#Game Library
game_lib = {
    "Donkey Kong": {"Quantity": 3, "Cost": 2, "Point Cost": 3},
    "Super Mario Bros.": {"Quantity": 5, "Cost": 2, "Point Cost": 3},
    "Tetris": {"Quantity": 2, "Cost": 1, "Point Cost": 3}
}

#Rented Games Library
rented_games = {}

#Register/Sign Up Function
def register():
    print("REGISTER MENU")
    print("Please Input Your Information")
    username = str(input("Username(Leave blank to go back): "))
    if not username:
        return
    if username in user_database:
        print("Username already taken")
        print("Press Enter to Continue...")
        input()
        return
    userbalance = 0
    userpoints = 0
    while True:
        password = str(input("Password(Minimum of 8 characters): "))
        if len(password) >= 8:
            print("Password Saved")
            break
        else:
            print("Password Must Have Minimum of 8 Characters")

    user_database[username] = {
        "username": username,
        "password": password,
        "balance": userbalance,
        "points": userpoints
    }

    print(f"Hello {username}! You have succesfully Registered!")
    print("Press Enter to Continue...")
    input()
    
#Admin Menu
def adminmenu():
    print("ADMIN MENU")
    print("Please Choose an Option")
    print("1. Update Game Library")
    print("2. Log Out")
    admchoice = str(input("Enter Your Choice: "))
    if admchoice == "1":
        updategames()
    elif admchoice == "2":
        confirm = str(input("Confirm Log Out? Yes or No?"))
        if confirm in ["yes", "YES", "Yes"]:
            menu()
        elif confirm in ["no", "NO", "No"]:
            print("Log Out Session Cancelled.")
            print("Press Enter to Continue...")
            input()
            adminmenu()
    else:
        print("Invalid Input")
        print("Press Enter to Continue...")
        input()
        adminmenu()
        
def updategames():
    print("Game Library:")
    games = list(game_lib.keys())
    for i, game in enumerate(games):
        details = game_lib[game]
        print(f"{i+1}. {game}: Quantity - {details['Quantity']}, Cost - {details['Cost']}, Point Cost - {details['Point Cost']}")
    print ("Please Choose an Option:")
    print("1. Remove Game")
    print("2. Add Game")
    print("3. Update/Edit Game")
    print("4. Return to Admin Menu")
    updatechoice = str(input("Enter Your Choice:"))
    if updatechoice == "1":
        gamename = str(input("Enter Game Name to Remove"))
        if gamename in game_lib:
            del game_lib[gamename]
            print(f"{gamename} is Now Removed.")
            print("Press Enter to Continue...")
            input()
            updategames()
        else:
            print("Game Not Found in the Library.")
            print("Press Enter to Continue...")
            input()
            updategames()
    elif updatechoice == "2":
        gamename = str(input("Enter the Name of the Game Name You Wish to Add: "))
        if gamename in game_lib:
            print("Game Already Exsist in the Library.")
            print("Press Enter to Continue...")
            input()
            updategames()
        else:
            quantity = int(input("Enter Quantity Available: "))
            cost = int(input("Enter Cost: "))
            point_cost = int(input("Enter Point Cost: "))
            game_lib[gamename] = {"Quantity": quantity, "Cost": cost, "Point Cost": point_cost}
            print(f"{gamename} is Now Added to the Library.")
            print("Press Enter to Continue...")
            updategames()
    elif updatechoice == "3":
        editchoice = input("Enter Name of the Game You Wish to Modify: ")
        if editchoice in game_lib:
            quantity = int(input("Enter New Quantity Available: "))
            cost = int(input("Enter new cost: "))
            point_cost = int(input("Enter New Point Cost: "))
            game_lib[game]["Quantity"] = quantity
            game_lib[game]["Cost"] = cost
            game_lib[game]["Point Cost"] = point_cost
            print(f"Details for {game} has been Updated.")
            print("Press Enter to Continue...")
            updategames()
        else:
            print("Game Not Found")
            print("Press Enter to Continue...")
            input()
            updategames()
    elif updatechoice == "4":
        print("Returning to Admin Menu...")
        adminmenu()
    else:
        print("Invalid Input")
        print("Press Enter to Continue...")
        input()
        updategames()

#User Menu Function
def usermenu(currentuser):
    print(f"USER MENU\nCurrent User: {currentuser}")
    print("Please Choose an Option")
    print("1. Rent Games")
    print("2. Inventory")
    print("3. Return Games")
    print("4. Balance Management")
    print("5. Redeem Free Game")
    print("6. Log Out")
    choice = input("Please Enter your Choice: ")
    if choice == "1":
        rent(currentuser)
    elif choice == "2":
        inventory(currentuser)
    elif choice == "3":
        returngame(currentuser)
    elif choice == "4":
        balance(currentuser)
    elif choice == "5":
        redeem(currentuser)
    elif choice == "6":
        confirm = str(input("Confirm Log Out? Yes or No?"))
        if confirm in ["yes", "YES", "Yes"]:
            menu()
        elif confirm in ["no", "NO", "No"]:
            print("Log Out Session Cancelled")
            print("Press Enter to Continue...")
            input()
            usermenu(currentuser)
        else:
            print("Invalid Input")
            usermenu(currentuser)
    else:
        print("Invalid Input")
        usermenu(currentuser)

#Admin Log In Function
def adminlog():
    admin_username = "admin"
    admin_password = "adminpass"
    print("Admin Log In")
    print("Please Enter Your Username and Password")
    adminuser = str(input("Admin Username(Leave blank to go back): "))
    if not adminuser:
        adminlog()
    adminpass = str(input("Admin Password: "))
    if adminuser != admin_username:
        print(f"No Admin {adminuser} Name Found")
        adminlog()
    if adminpass == admin_password:
        print(f"Hello {adminuser}! You Have Successfully Logged In!")
        print("Press Enter to Continue...")
        input()
        adminmenu()

#Game Returning Function
def returngame(username):
    print("RETURN GAME MENU")
    print(f"{username}'s Rented Games:")
    rented = rented_games.get(username, [])
    for i, game in enumerate(rented, start=1):
        print(f"{i}. {game}")
    choice = input("Enter Number of the Game You Wish to Return (Leave blank to go back): ")
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(rented):
            game_to_return = rented[choice - 1]
            rented_games[username].remove(game_to_return)
            game_lib[game_to_return]["Quantity"] += 1
            print(f"{game_to_return} Returned Successfully.")
            print("Press Enter to Continue...")
            input()
            returngame(username)
        else:
            print("Invalid input.")
            print("Press Enter to Continue...")
            input()
            returngame(username)
            
    elif not choice:
        pass
    else:
        print("Invalid input.")

#Balance Management Function
def balance(currentuser):
    user_data = user_database.get(currentuser)
    if user_data:
        userbalance = user_data["balance"]
        print(f"Current Balance: {userbalance}")
        balchoice = input("Please Choose an Option")
        print("1. Top-Up Balance")
        print("2. Return to Main Menu")
        print("Enter your Choice: ")
        if balchoice == "1":
            topup = float(input("Amount to Top-Up: "))
            newbal = userbalance + topup
            confirm = str(input("Confirm Top-Up? Yes or No: "))
            if confirm in ["yes", "YES", "Yes"]:
                user_data["balance"] = newbal
                print(f"Top-Up Confirmed\nNew Balance is: {newbal}")
                print("Press Enter to Continue...")
                input()
                usermenu(currentuser)
            elif confirm in ["no", "NO", "No"]:
                print("Top-Up Canceled")
                print("Press Enter to Continue...")
                input()
                balance(currentuser)
            else:
                print("Invalid Input.")
                balance(currentuser)
        elif balchoice == "2":
            print("Returning to Main User Menu...")
            usermenu(currentuser)
        else:
            print("Invalid Input")
            balance(currentuser)

#User Log In Function
def userlog():
    print("USER LOG IN MENU")
    print("Please Input Your Account Information")
    username = str(input("Username: "))
    password = str(input("Password: "))
    if username in user_database and user_database[username]["password"] == password:
        currentuser = username
        print(f"Hello {currentuser}! You Have Successfully Logged In!")
        print("Press Enter to Continue...")
        input()
        usermenu(currentuser)
    elif username not in user_database:
        print("No Account Found")
        print("Press Enter to Continue...")
        input()
    else:
        print("Incorrect Password")
        print("Press Enter to Continue...")
        input()

#Game Rent Function
def rent(username):
    currentuser = username
    print(f"Current User: {currentuser}")
    print(f"Balance: {user_database[username]['balance']}")
    print(f"Points: {user_database[username]['points']}")
    print("Game Library:")
    games = list(game_lib.keys())
    for i, game in enumerate(games):
        details = game_lib[game]
        print(f"{i+1}. {game}: Quantity - {details['Quantity']}, Cost - {details['Cost']}")
    gamechoice = input("Please Enter the Number of the Game You Want to Rent(Leave blank to go back): ")
    if gamechoice.isdigit():
        gamechoice = int(gamechoice)
        if 0 < gamechoice <= len(games):
            game = games[gamechoice - 1]
            if user_database[username]["balance"] < game_lib[game]["Cost"]:
                print("Not Enough Balance")
                print("Press Enter to Continue...")
                input()
                rent(username)
            else:
                user_database[username]["balance"] -= game_lib[game]["Cost"]
                game_lib[game]["Quantity"] -= 1
                rented_games.setdefault(username, []).append(game)
                if game_lib[game]["Cost"] == 2:
                    user_database[username]["points"] += 1
                    print(f"Successfully Rented {game}! 1 Point Added to {currentuser}'s Account")
                    print("Press Enter to Continue...")
                    input()
                    usermenu(currentuser)
                elif game_lib[game]["Cost"] == 1:
                    user_database[username]["points"] += 0.5
                    print(f"Successfully Rented {game}! 0.5 Points Added to {currentuser}'s Account")
                    print("Press Enter to Continue...")
                    input()
                    usermenu(currentuser)
    if not gamechoice:
        usermenu(currentuser)
    if gamechoice != len(games):
        print("Invalid Input. Please Choose a Number Listed on the Choices.")
        print("Press Enter to Continue...")
        input()
        rent(username)
    if gamechoice >> enumerate(games):
        print("Invalid Input. Please Choose a Number Listed on the Choices")
        print("Press Enter to Continue...")
        input()
        rent(username)

#User Inventory Function
def inventory(currentuser):
    print(f"USER INVENTORY")
    print(f"{currentuser}'s Rented Games:")
    rented = rented_games.get(currentuser, [])
    for i, game in enumerate(rented, start=1):
        print(f"{i}. {game}")
    print("Press Enter to go Back to User Menu...")
    input()
    usermenu(currentuser)

#Redeem Games Function
def redeem(username):
    currentuser = username
    print(f"REDEEM FREE GAME RENT")
    print(f"Current User: {currentuser}")
    print(f"Current Points: {user_database[username]['points']}")
    print("Game Library:")
    games = list(game_lib.keys())
    for i, game in enumerate(games):
        details = game_lib[game]
        print(f"{i+1}. {game}: Quantity - {details['Quantity']}, Point Cost - {details['Point Cost']}")
    gamechoice = input("Please Enter the Number of the Game You Want to Rent(Leave blank to go back): ")
    if gamechoice.isdigit():
        gamechoice = int(gamechoice)
        if 0 < gamechoice <= len(games):
            game = games[gamechoice - 1]
            if user_database[username]["points"] < game_lib[game]["Point Cost"]:
                print("Not Enough Points")
                print("Press Enter to Continue...")
                input()
                redeem(username)
            else:
                user_database[username]["points"] -= game_lib[game]["Point Cost"]
                game_lib[game]["Quantity"] -= 1
                rented_games.setdefault(username, []).append(game)
                print(f"Successfully Rented {game}!")
                print("Press Enter to Continue...")
                input()
                usermenu(currentuser)
    if not gamechoice:
        usermenu(currentuser)
    if gamechoice != len(games):
        print("Invalid Input. Please Choose a Number Listed on the Choices.")
        print("Press Enter to Continue...")
        input()
        redeem(username)
    if gamechoice >> enumerate(games):
        print("Invalid Input. Please Choose a Number Listed on the Choices")
        print("Press Enter to Continue...")
        input()
        redeem(username)

#Main Menu Function
def menu():
    while True:
        try:
            print(f"VIDEO GAMES RENTAL STATION")
            print("Please Choose an Option\n1. Register")
            print("2. Admin Log In")
            print("3. User Log In")
            print("4. Exit")
            choice = input("Enter Your Choice: ")
            if choice == "1":
                register()
            elif choice == "2":
                adminlog()
            elif choice == "3":
                userlog()
            elif choice == "4":
                break
        except ValueError:
            print("Invalid Input")
            print("Press Enter to Continue...")
            input()
menu()
