import sys


class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def addatbottom(self, item):
        self.items.insert(0, item)


def getdigitvalue(value):
    if value.isdigit():
        return value
    if value == "J":
        return 11
    if value == "Q":
        return 12
    if value == "K":
        return 13
    if value == "A":
        return 14


def comparecards(card1, card2):
    card1 = int(getdigitvalue(card1[:-1]))
    card2 = int(getdigitvalue(card2[:-1]))

    if card1 > card2:
        return -1
    elif card1 < card2:
        return 1
    else:
        return 0


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cardsPlayerOne = Stack()
cardsPlayerTwo = Stack()

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardsPlayerOne.push(input())  # the n cards of player 1
m = int(input())  # the number of cards for player 2
for j in range(m):
    cardsPlayerTwo.push(input())  # the m cards of player 2

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

count = 0

while cardsPlayerOne.size() > 0 and cardsPlayerTwo.size() > 0:
    count += 1
    cardPlayerOne = cardsPlayerOne.pop()
    cardPlayerTwo = cardsPlayerTwo.pop()

    result = comparecards(cardPlayerOne, cardPlayerTwo)

    if result == -1:  # player 1 won
        cardsPlayerOne.addatbottom(cardPlayerTwo)
    elif result == 1:  # player 2 won
        cardsPlayerTwo.addatbottom(cardPlayerOne)

if cardsPlayerOne.size() < 1:
    print("2 " + str(count))
if cardsPlayerTwo.size() < 1:
    print("1 " + str(count))
