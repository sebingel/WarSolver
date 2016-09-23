class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def pushtobottom(self, item):
        # self.items.insert(0, item)
        self.push(item)


class InputGetter:
    def __init__(self):
        self.__initial = True
        self.__content = []

    def getinput(self):
        return input()

        # if self.__initial:
        #     self.__initial = False
        #     with open("tc2.txt") as f:
        #         self.__content = f.readlines()
        #
        #     for i in range(len(self.__content)):
        #         if "\n" in self.__content[i]:
        #             self.__content[i] = self.__content[i][:-1]
        #
        # return self.__content.pop(0)


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


inp = InputGetter()

cardsPlayerOne = Stack()
cardsPlayerTwo = Stack()

n = int(inp.getinput())  # the number of cards for player 1
for i in range(n):
    cardsPlayerOne.push(inp.getinput())  # the n cards of player 1
m = int(inp.getinput())  # the number of cards for player 2
for j in range(m):
    cardsPlayerTwo.push(inp.getinput())  # the m cards of player 2

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

turnCount = 0
pat = False

while cardsPlayerOne.size() > 0 and cardsPlayerTwo.size() > 0:
    turnCount += 1

    cardPlayerOne = cardsPlayerOne.pop()
    cardPlayerTwo = cardsPlayerTwo.pop()

    cardsAtStakePlayerOne = [cardPlayerOne]
    cardsAtStakePlayerTwo = [cardPlayerTwo]

    result = comparecards(cardPlayerOne, cardPlayerTwo)

    while result == 0:
        # here starts the war
        if cardsPlayerOne.size() < 3 or cardsPlayerTwo.size() < 3:
            print("PAT")
            pat = True
            break

        cardsAtStakePlayerOne.append(cardsPlayerOne.pop())
        cardsAtStakePlayerOne.append(cardsPlayerOne.pop())
        cardsAtStakePlayerOne.append(cardsPlayerOne.pop())
        cardsAtStakePlayerTwo.append(cardsPlayerTwo.pop())
        cardsAtStakePlayerTwo.append(cardsPlayerTwo.pop())
        cardsAtStakePlayerTwo.append(cardsPlayerTwo.pop())

        cardPlayerOne = cardsPlayerOne.pop()
        cardPlayerTwo = cardsPlayerTwo.pop()

        cardsAtStakePlayerOne.append(cardPlayerOne)
        cardsAtStakePlayerTwo.append(cardPlayerTwo)

        result = comparecards(cardPlayerOne, cardPlayerTwo)

    if result == -1:  # player 1 won
        for card in cardsAtStakePlayerOne:
            cardsPlayerOne.pushtobottom(card)
        for card in cardsAtStakePlayerTwo:
            cardsPlayerOne.pushtobottom(card)
    elif result == 1:  # player 2 won
        for card in cardsAtStakePlayerOne:
            cardsPlayerTwo.pushtobottom(card)
        for card in cardsAtStakePlayerTwo:
            cardsPlayerTwo.pushtobottom(card)

if not pat:
    if cardsPlayerOne.size() < 1:
        print("2 " + str(turnCount))
    if cardsPlayerTwo.size() < 1:
        print("1 " + str(turnCount))
