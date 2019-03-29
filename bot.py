
def initialize():
    print("Welcome to THE CACHE SIMULATION")
    print("Pick a card... any card...")
    print("Just kidding...")
    print("Here are your ACTUAL options: ")


def switch(user_input, cache):

    options = dict(
        r=cache.read_byte,
        w=cache.write_byte,
        d=cache.display_cache,
    )

    return options.get(user_input, None)()

def input_threshold(user_input, cache):

    options = ["r", "w", "d"]
    # handling case of actual alphabet letters
    # entered in as user input
    user_input = user_input.lower()
    # if not an actual letter, then ask again
    if user_input.isalpha():
        if user_input in options:
            return switch(user_input, cache)
        else:
            print("Please enter an appropriate response...")
            return ask()
    else:
        print("Please enter an appropriate response...")
        return ask()


def ask():
    
    ask = input("(R)ead, (W)rite, or (D)isplay Cache ? ")
    # take options and invoke threshold method
    # input_threshold(ask, cache)
    return ask
 