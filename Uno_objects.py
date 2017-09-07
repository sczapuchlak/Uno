from UnoCardClass import Hand

class Player:
    #write the class definition, #__ = private.
    def __init__(self, name, hand=None, bot=False): #this method initializes the attributes
        self.__name = name
        if hand is None:
            hand = Hand()
        self.hand = hand
        self.bot = bot

    def set_name(self, name):#method accepts argument for player's name
        self.__name = name

    # def set_hand(self, hand):# is this a thing? hand will need to be a dictionary
    #     self.__hand = hand{:} #maybe make this a dictionary?

    def get_name(self): #method RETURNS the player's name
        return self.__name

    # def get_hand(self): #method needed to return hand dictionary, NEEDS WORK>

#to do/HAND? - add dealt hand, play a card, add the discarded cards
#clear() will clear the dictionary
#pop-specific value returned/ popitem- random value returned/ items shows all keys/values

#for testing...not working
def main():
    my_name = Player("Sonja")
    print(my_name)

if __name__ == '__main__':
    main
