def Roshaembo():
    import random as r
    a = "Rock"
    b = "Paper"
    c = "Scissors"
    # myList = ['Rock', 'Paper', 'Scissor']
    myList = ["a", "b", "c"]
    User_input = str(input("Choose a given option where a = {}, b = {}, c = {}: ".format(a, b, c)))
    k = r.choice(myList)
    if k == "a":
        m = "Rock"
    elif k == "b":
        m = "Paper"
    else:
        m = "scissors"
    print("Computer's output:",m)
    if k == User_input:
        print("It's a tie")
        p = (input("For playing again enter 1, for quitting enter 2: "))
        if p == '1':
            Roshaembo()
        elif p == '2':
            print("The Game has come to an END \nThanks for playing")
        else:
            while True:
                print("Error")
    elif User_input == "a" and k == "b":
        print("Computer wins by Paper enveloping rock")
        p = (input("For playing again enter 1, for quitting enter 2: "))
        if p == '1':
            Roshaembo()
        elif p == '2':
            print("The Game has come to an END \nThanks for playing")
        else:
            while True:
                print("Error")
    elif User_input == 'a' and k == 'c':
        print("You won using rock to destroy scissors")
        p = (input("For playing again enter 1, for quitting enter 2: "))
        if p == '1':
            Roshaembo()
        elif p == '2':
            print("The Game has come to an END \nThanks for playing")
        else:
            while True:
                print("Error")
    elif User_input == 'b' and k == 'a':
        print("User won using paper to envelop rock")
        p = (input("For playing again enter 1, for quitting enter 2: "))
        if p == '1':
            Roshaembo()
        elif p == '2':
            print("The Game has come to an END \nThanks for playing")
        else:
            while True:
                print("Error")
    elif User_input == 'b' and k == 'c':
        print("Computer won using scissors to cut through paper")
        p = (input("For playing again enter 1, for quitting enter 2: "))
        if p == '1':
            Roshaembo()
        elif p == '2':
            print("The Game has come to an END \nThanks for playing")
        else:
            while True:
                print("Error")
    elif User_input == 'c' and k == 'a':
        print("Computer won using rocks to destroy scissors")
        p = (input("For playing again enter 1, for quitting enter 2: "))
        if p == '1':
            Roshaembo()
        elif p == '2':
            print("The Game has come to an END \nThanks for playing")
        else:
            while True:
                print("Error")
    elif User_input == 'c' and k == 'b':
        print("User won using scissors to cut through paper")
        p = (input("For playing again enter 1, for quitting enter 2: "))
        if p == '1':
            Roshaembo()
        elif p == '2':
            print("The Game has come to an END \nThanks for playing")
        else:
            while True:
                print("Error")
    else:
        print("Error retry by typing the correct Input as described above")
        Roshaembo()


Roshaembo()     
