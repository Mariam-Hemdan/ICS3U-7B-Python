#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : Dec 2019
# This program calculates the running total of a list


def main():
    total = []
    while True:
        number = input("Enter how many numbers are in the list? ")

        print()

        try:
            number_as_int = int(number)
            for loop_counter in range(0, number_as_int):
                item = input("Enter the number: " + str(loop_counter+1) + ": ")
                item_int = int(item)
                total.append(item_int)
            running_total = [sum(total[0:loop_counter+1]) for loop_counter in
                             range(0, len(total))]
            print()
            print("The number in the list are :{0}".format(total))
            print("The Running Total is:{0}".format(running_total))
            break

        except Exception:
            print("This number is not an integer")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
