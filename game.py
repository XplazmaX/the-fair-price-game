import time

import random

tries = 0

print("Here is the game of the right price, be sure to choose your difficulty.")

print("............................")

print("[1]-A number between 0 and 1000, you have 10 tries")

print("............................")

print("[2]-A number between 0 and 10000, you have 15 tries")

print("............................")

print("[2]-A number between 0 and 100000, you have 20 tries")

print("............................")

choix = input("So you choose which difficulties : ")

if choix == "1" :

	rd = random.randint(0, 1000)	while True :

		number = int(input("Choose a number between 0 and 1000 : "))

		if tries == 10 :

			print("............................")

			print("You lost because you exceeded the 10 tries")

			break

		elif number > rd :

			tries += 1

			print("Your number is greater")

			continue

		elif number < rd :

			tries += 1

			print("Your number is smaller")

			continue

		else :

			print("GG, you found the right number that was",rd)

			break

if choix == "2" :

	rd = random.randint(0, 10000)

	while True :

		number = int(input("Choose a number between 0 and 10000 : "))

		if tries == 15 :

			print("............................")

			print("You lost because you exceeded the 15 tries")

			break

		elif number > rd :

			tries += 1

			print("Your number is greater")

			continue

		elif number < rd :

			tries += 1

			print("Your number is smaller")

			continue

		else :

			print("GG, you found the right number that was",rd)

			break

if choix == "3" :

	rd = random.randint(0, 100000)

	while True :

		number = int(input("Choose a number between 0 and 100000 : "))

		if tries == 10 :

			print("............................")

			print("You lost because you exceeded the 10 tries")

			break

		elif number > rd :

			tries += 1

			print("Your number is greater")

			continue

		elif number < rd :

			tries += 1

			print("Your number is smaller")

			continue

		else :

			print("GG, you found the right number that was",rd)

			break
