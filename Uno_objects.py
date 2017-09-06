class Player(object):
    #write the class definition, #__ = private.
    def __init__(self, name): #this method initializes the attributes
        self._name = name

    # def set_name(self, name):#method accepts argument for player's name
    #     self.__name = name NOT NEEDED.

    # def set_hand(self, hand):# is this a thing? hand will need to be a dictionary
    #     self.__hand = hand{:} #maybe make this a dictionary?
    @property
    def name(self): #method RETURNS the player's name
        return self._name

    # def get_hand(self): #method needed to return hand dictionary, NEEDS WORK>

#to do/HAND? - add dealt hand, play a card, add the discarded cards
#clear() will clear the dictionary
#pop-specific value returned/ popitem- random value returned/ items shows all keys/values
#invitation to start/ instructions to Quit game
#for testing...not working
#need to import deck/hand, etc??
# print("Sonja") #for testing

def main():
    #create the deck from the Deck class
    uno_deck = Deck()

    player_name = input("Ready to play! What's yer name? ")
    #validation, check for empty string
    current_player = Player(player_name)#create an object from the Player class
    print("Welcome", current_player.name, "Let's Play Uno...")
    #create an UNO deck object from the Deck class
    # print(my_name)
    # print("Sonja")
    # print(my_name)

if __name__ == '__main__':
    main()
