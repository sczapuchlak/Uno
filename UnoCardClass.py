import random

class Card(object):
    #this class deck will represent the uno card class
    cardColor = ['Red', 'Yellow', 'Green', 'Blue']
    cardNumber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, color , number):
        self.color = color
        self.number = number

   #this returns a string which is readable to display the card name
    def __str__(self):
        return 'A %s %s' % (Card.cardColor[self.color],
                             Card.cardNumber[self.number])

    # this will return true if the other card is playable on top of this card
    # if it is not playable it will return false
    def isCardPlayable(self, other):
        return (self.cardColor == other.cardColor or
                self.cardNumber == other.cardNumber)

#this class defines and makes the deck
class Deck(object):

    def __init__(self):
        self.deck = []
        # adds all the cards to the deck
        for color in range(4):
            for number in range(1, 10):
                card = Card(color, number)
                self.deck.append(card)

    # this returns a string which is readable for the user
    def __str__(self):
        readableString = []
        for card in self.deck:
            readableString.append(str(card))
        return '\n'.join(readableString)

    #adds a card to the deck
    def addCardToHand(self, card):
        self.deck.append(card)

    #this shuffles the deck
    def shuffleDeck(self):
        random.shuffle(self.deck)

    #removes a card from the deck, don't know if we need this right now, but just in case
    def removeCardFromHand(self, card):
        self.deck.remove(card)

    #this removes and returns the index card from deck
    def removeAndReturnCard(self, i=-1):
        return self.deck.pop(i)


    #this puts n amount of cards in the hand
    def drawCards(self, hand, num):
        for i in range(num):
            hand.addCardToHand(self.removeAndReturnCard())

#this class represents a hand of playing cards
class Hand(Deck):
    def __init__(self, label=''):
        super().__init__()
        self.deck = []
        self.label = label

#this calls to main
if __name__ == '__main__':

    deck = Deck()
    deck.shuffleDeck()
    hand = Hand()
    deck.drawCards(hand,5)
    print(hand)