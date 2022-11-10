#!/usr/bin/env python3
# Created By: Minab Berhane
# Date: November 08 2022
# This program gives the sum of a positive number


def main():
    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0

    # get the user number as a string
    user_number_string = input("Enter a positive number: ")
    print("")

    # catches any invaild input
    try:
        # Changing string to integer
        user_number = int(user_number_string)
        # Check to see if they inputed a postive number
        if user_number > 0:
            # calculate the sum of all numbers from 0 to user number
            while loop_counter <= user_number:
                sum = sum + loop_counter
                print("Tracking {0} times through loop.".format(loop_counter))
                loop_counter = loop_counter + 1

            print("")
            print("The sum of the numbers from 0 to {} is: {}.".format(user_number, sum))
        else:
            print("You entered a negative number, please try again.")
    except Exception:
        print("\033[1;35;38mThis is not an integer")
    finally:
        print()
        print("\033[1;35;38mThanks for playing")


if __name__ == "__main__":
    main()
