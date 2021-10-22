#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program print 10 random numbers and the largets number

import random


def largest_number(random_numbers):
    # This function calculate maximum number
    counter = 0
    final_number = 0

    # process
    for counter in range(1, len(random_numbers)):
        # output
        print("The random number {0} is: {1}".format(counter, random_numbers[counter]))

        if random_numbers[counter] > final_number:
            final_number = random_numbers[counter]

    return final_number


def main():
    # This function calculate average
    number = []
    big_number = 0
    counter = 0

    # heading
    print("Here is the list of random numbers:")
    print("")

    # process
    for counter in range(0, 11):
        random_numbers = random.randint(0, 100)
        number.append(random_numbers)

    # call functions
    big_number = largest_number(number)

    # output
    print("")
    print("The largest number is: {0}".format(big_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
