# lottery ticket

#imports
import random

import time
dots = [".",".","."]

# variables
import time

first_ticket_cost = 10
first_ticket_winnings = 50
first_ticket_chances_nuo = 1
first_ticket_chances_iki = 4

second_ticket_cost = 50
second_ticket_winnings = 900
second_ticket_chances_nuo = 1
second_ticket_chances_iki = 15

third_ticket_cost = 100
third_ticket_winnings = 100000
third_ticket_chances_nuo = 1
third_ticket_chances_iki = 100



#deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? Type q if you would like to exit. $")
        if amount != "q":
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("Amount must be greater than 0.")
            else:
                print("Please enter a number.")
        else:
            exit()

    return amount

#get bet
def get_tickets(amount):

    print("\nWhat lottery ticket would you like to buy? \n")
    print(f"first ticket's odds are {first_ticket_chances_nuo} - {first_ticket_chances_iki} and costs ${first_ticket_cost}, but if you win you'll get ${first_ticket_winnings}")
    time.sleep(1)
    print(f"second ticket's odds are {second_ticket_chances_nuo} - {second_ticket_chances_iki} and costs ${second_ticket_cost}, but if you win you'll get ${second_ticket_winnings}")
    time.sleep(1)
    print(f"third ticket's odds are {third_ticket_chances_nuo} - {third_ticket_chances_iki} and costs ${third_ticket_cost}, but if you win you'll get ${third_ticket_winnings}\n")
    while True:
        ticket = input("What ticket would you like? 1, 2, 3? ")
        if ticket.isdigit():
            ticket = int(ticket)
            if ticket == 1 or ticket == 2 or ticket == 3:
                how_much_tickets = input("How much tickets would you like? ")

                if how_much_tickets.isdigit():
                    how_much_tickets = int(how_much_tickets)
                    if how_much_tickets > 0:
                        if ticket == 1:
                            if first_ticket_cost * how_much_tickets > amount:
                                youneed = first_ticket_cost * how_much_tickets
                                print(f"You don't have enough $ to buy the ticket. Your balance is ${amount}. You need ${youneed}")
                            else:
                                youneed = first_ticket_cost * how_much_tickets
                                amount = amount - youneed
                                break
                        elif ticket == 2:
                            if second_ticket_cost * how_much_tickets > amount:
                                youneed = second_ticket_cost * how_much_tickets
                                print(f"You don't have enough $ to buy the ticket. Your balance is ${amount}. You need ${youneed}")
                            else:
                                youneed = second_ticket_cost * how_much_tickets
                                amount = amount - youneed
                                break
                        elif ticket == 3:
                            if third_ticket_cost * how_much_tickets > amount:
                                youneed = third_ticket_cost * how_much_tickets
                                print(f"You don't have enough $ to buy the ticket. Your balance is ${amount}. You need ${youneed}")
                            else:
                                youneed = third_ticket_cost * how_much_tickets
                                amount = amount - youneed
                                break
                    else:
                        print("Number can't be 0")
                else:
                    print("Number can't be a word")
            else:
                print("Number has to be 1, 2 or 3")
        else:
            print("Number can't be a word")
    return ticket, how_much_tickets, amount



def getwinnings(ticket, how_much_tickets):
    b = 0
    if ticket == 1:
        for _ in range(how_much_tickets):
            a = random.randint(first_ticket_chances_nuo, first_ticket_chances_iki)
            if a == 1:
                b = b + first_ticket_winnings
    if ticket == 2:
        for _ in range(how_much_tickets):
            a = random.randint(second_ticket_chances_nuo, second_ticket_chances_iki)
            if a == 1:
                b = b + second_ticket_winnings
    if ticket == 3:
        for _ in range(how_much_tickets):
            a = random.randint(third_ticket_chances_nuo, third_ticket_chances_iki)
            if a == 1:
                b = b + third_ticket_winnings
    return b

amount = deposit()

while True:
    ticket, how_much_tickets, amount = get_tickets(amount)
    c = getwinnings(ticket, how_much_tickets)
    print("Calculating")
    for dot in dots:
        print(dot, end="")
        time.sleep(1)
    print(f"\nYour balance was {amount}")
    print(f"You won ${c}")
    amount = amount + c
    if amount == 0:
        exit()
    print(f"Your balance is: ${amount}\n")
    y = input("Press q if you would like to quit, press Enter if you would like to keep playing. ")
    if y == "q":
        exit()