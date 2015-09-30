#! /usr/bin/env/python3
from datetime import date

yearToday = date.today().year


def yearWhen100():
	name = str(input("Please enter your name: "))
	age = int(input("Please enter your age: "))
	year100 = yearToday + (100 - age)
	message = name.capitalize() + ", you will turn 100 in the year " + str(year100) + "\n"
	print (message)
	repeatAmount = int(input("How many copies would you like of this message: "))
	print (message * repeatAmount)


if __name__ == "__main__":
	yearWhen100()
