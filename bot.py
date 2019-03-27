

def initialize():
    print("Welcome to THE CACHE SIMULATION")
    print("Pick a card... any card...")
    print("Just kidding...")
    print("Here are your ACTUAL options: ")

    ask()


def input_threshold(input):

    # handling case of actual alphabet letters
    # entered in as user input

    # if not an actual letter, then ask again
    if input.isalpha():
        print("You entered: " + input)
    else:
        print("Please enter an appropriate response...")
        return ask()


def ask():
    
    ask = input("(R)ead, (W)rite, or (D)isplay Cache ? ")
    # take options and invoke threshold method
    input_threshold(ask)
 