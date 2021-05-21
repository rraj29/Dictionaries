locations = {0: "You are sitting in front of a computer, learning python.",
             1: "You are standing at the end of a road before a small brick building.",
             2: "You are at the top of a hill.",
             3: "You are inside a building, a well house for a small stream.",
             4: "You are in a valley beside a stream.",
             5: "You are in a forest."}

exits = {0: {"Q": 0},
         1: {"W": 2,"E": 3,"N": 5,"S": 4,"Q": 0},
         2: {"N": 5,"Q": 0},
         3: {"W": 1,"Q": 0},
         4: {"W": 1,"N": 2,"Q": 0},
         5: {"W": 2,"S": 1,"Q": 0}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "WEST": "W",
              "EAST": "E"}


loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())
    # available_exits = ""
    # for direction in exits[loc].keys():
    #     available_exits += direction + ", "

    print(locations[loc])

    if loc==0:
        break

    direction = input("Available exits are " + available_exits).upper()
    print()
    #Parse the user input with vocabulary dictionary, if needed
    if len(direction) > 1:      #more than 1 letter, so check vocab
        # for word in vocabulary: #does it contain a word that we know
        #     if word in direction:
        #         direction = vocabulary[word]
        words = direction.split(" ")
        for word in words:  # this is more efficient as we are searching for the man word in user's input
            if word in vocabulary:      #rather than the whole dictionary,
                direction = vocabulary[word]    #coz if the dictionary was long, it would be very less efficient
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You can't go in that direction.")
