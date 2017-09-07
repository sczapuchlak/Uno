from UnoCardClass import Deck, Hand, Card

class Player(object):
    #write the class definition, #__ = private.
    def __init__(self, name, hand): #this method initializes the attributes
        self._name = name
        self._hand = hand

    # def set_name(self, name):#method accepts argument for player's name
    #     self.__name = name NOT NEEDED.

    # def set_hand(self, hand):# is this a thing? hand will need to be a dictionary
    #     self.__hand = hand{:} #maybe make this a dictionary?
    @property
    def name(self): #method RETURNS the player's name
        return self._name

    # def draw_card(self, deck):


    # def play_card(self):

    # def get_hand(self): #method needed to return hand dictionary, NEEDS WORK>

#clear() will clear
#invitation to start/ instructions to Quit game

# print("Test") #for testing

def main():
    #create the deck from the Deck class
    uno_deck = Deck()
    # print(uno_deck) #un comment for testing.  it works.
    player_name = input("Ready to play! What's yer name? ")
    #validation, check for empty string
    current_player = Player(player_name, Hand())#create an object from the Player class
    print("Welcome", current_player.name + ",", "here are your cards...")
    #create a hand for the current player
    uno_deck.drawCards(current_player._hand, 5)
    print(current_player._hand) #comment to keep the hand hidden
    # print("Sonja")
    # print(my_name)

if __name__ == '__main__':
    main()
