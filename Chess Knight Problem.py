def possible_moves(position) -> list:
    # Create empty list for valid moves to fill, a list of possible distances a knight can travel in the x and y
    # directions and take the two coordinates in the position given and convert them into integers
    valid_moves = []
    spaces = [-2, -1, 1, 2]
    current_x = ord(position[0].upper())
    current_y = int(position[1])

    # Check all valid x tiles within + or - 2 tiles from current x position
    for x_tiles in spaces:

        # Check if the spaces above are within the ascii range A to H
        if (current_x + x_tiles) in range(ord("A"), ord("I")):

            # Check all valid y tiles within + or - 2 tiles from current y position
            for y_tiles in spaces:

                # Check if the spaces above are within 1 and 9 and see if it is an up or down 2 and left or right one
                # or left and right 2 and up or down 1 move
                if ((y_tiles + current_y) in range(1, 9)
                        and ((abs(x_tiles) == 1 and abs(y_tiles) == 2) or (abs(x_tiles) == 2 and abs(y_tiles) == 1))):
                    # If the above conditions are met, put the valid combination into a function that turns the two into
                    # a string
                    valid_moves.append(position_builder(current_x + x_tiles, current_y + y_tiles))

    return valid_moves


def position_builder(x, y) -> str:
    # Take the two positions stated in the previous function, convert the first to ASCII and then smash them together in
    # a string
    move = ""
    move += chr(x)
    move += str(y)

    return move


while True:

    # Ask for the user to input a position of a knight piece on the board and convert it into a list of strings
    # containing the two coordinates or the letter "q" to quit
    current_position = list(input("Enter the knights current position or \"q\" to quit. (Ex: A4, B6, C7): "))

    # Check if the two coordinates are valid
    if (len(current_position) == 2 and (current_position[0].isalpha()
                                        and ord(current_position[0].upper()) in range(ord("A"), ord("I")))
            and (current_position[1].isdigit() and int(current_position[1]) in range(1, 9))):

        # If they are valid, run them through the possible moves function
        moves = possible_moves(current_position)
        print(moves)

    # Usual "q" to quit shenanigans
    elif len(current_position) == 1 and current_position[0].casefold() == "q":
        break

    # If the user enters something it cant use, ask them to enter something valid
    else:
        print("Please enter a valid position")
