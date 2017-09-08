from UnoCardClass import Deck, Card
from Uno_objects import Player

player_list = []
discard_pile = []
draw_pile = None
game_won = False


def game_loop():
    # This is the game loop.  This runs once per game and sets up all the variables.
    # These variables are global and defined at the top.  We want to make sure we don't accidentally create local ones.
    global draw_pile
    global game_won
    # Create a new deck
    draw_pile = Deck()
    game_won = False
    draw_pile.shuffleDeck()
    # Get the desired player count
    number_of_bots = process_player_count_input()
    # Append the human player
    player_list.append(Player("Human"))
    for i in range(number_of_bots):
        player_list.append(Player("Bot" + str(i+1), bot=True))
    discard_pile.append(draw_pile.removeAndReturnCard(0))
    for player in player_list:
        try:
            for i in range(7):
                player.hand.addCardToHand(draw_pile.removeAndReturnCard())
        except IndexError:
            # Not enough cards for this many players.
            player_list.clear()
            draw_pile = None
            discard_pile.clear()
            print("That's too many players!")
            return game_loop()
    turn_loop(0)
    if game_won:
        victor = None
        for player in player_list:
            if player.hand.get_card_count() == 0:
                victor = player
        print("Game over! " + victor.get_name() + " has won!")
    input("Press [ENTER] to play again!")
    player_list.clear()
    draw_pile = None
    discard_pile.clear()
    game_loop()


def process_player_count_input():
    # Process the input for the number of bots to play against.
    p_c = str(input("How many players to play against?"))
    if not p_c.isdigit():
        print("Please enter only a number.")
        return process_player_count_input()
    else:
        return int(p_c)


def turn_loop(player_id):
    # This loop will run perpetually until the game is over.
    # It is meant to serve as a single turn for a single player.
    for player in player_list:
        if player.hand.get_card_count() == 0:
            global game_won
            game_won = True
            return
    player = player_list[player_id]
    top_card = discard_pile[-1]
    hand = player.hand
    print(player.get_name() + "'s turn.")
    print("Top card is a " + str(top_card) + ".")
    if player.bot:
        # Do bot logic
        draw_until_playable(hand, top_card, True)
        print(player.get_name() + " has " + str(hand.get_card_count()) + " cards.")
        card = bot_logic(hand, top_card)
        print(player.get_name() + " played a " + str(hand.deck[card]))
        discard_pile.append(hand.removeAndReturnCard(card))
    else:
        # We are a human player; so provide the inputs.
        draw_until_playable(hand, top_card)
        print("Cards in your hand:")
        print(list_player_cards(player_id))
        card = validate_card_choice(input("Pick a card to play: "), hand)
        print("You played a " + str(hand.deck[card]))
        discard_pile.append(hand.removeAndReturnCard(card))
    print("\n----------\n")
    player_id += 1
    player_id %= len(player_list)
    turn_loop(player_id)


def validate_card_choice(pick, hand):
    # Ensures the player input corresponds to a valid and playable card.
    top_card = discard_pile[-1]
    pick = str(pick)
    if not pick.isdigit():
        print("Invalid input. Please enter the number card you want to play, from the list above.")
        return validate_card_choice(input("Pick a card to play: "), hand)
    pick_id = int(pick) - 1
    if hand.get_card_count() <= pick_id:
        print("Invalid input. Please enter the number card you want to play, from the list above.")
        return validate_card_choice(input("Pick a card to play: "), hand)
    card = hand.deck[pick_id]
    if not card.isCardPlayable(top_card):
        print(str(card) + " cannot be played! Choose another card.")
        return validate_card_choice(input("Pick a card to play: "), hand)
    return pick_id


def bot_logic(hand, top_card):
    # Bot just chooses the first card they can play.
    for i in range(hand.get_card_count()):
        card = hand.deck[i]
        if card.isCardPlayable(top_card):
            return i


def list_player_cards(player_id):
    # Returns a string formatted to cleanly show all the cards in a player's hand
    card_string = ''
    hand = player_list[player_id].hand
    for i in range(hand.get_card_count()):
        card = str(hand.deck[i])
        if i > 0 and i % 4 != 0:
            card_string += "\t"
        elif i % 4 == 0:
            card_string += "\n"
        card_string += str(i +1) + ": " + card
    return card_string


def draw_until_playable(hand, top_card, bot=False):
    # Draws cards continuously until a valid playable card is in the hand.
    playable = False
    card_count = 0
    for card in hand.deck:
        if card.isCardPlayable(top_card):
            playable = True
    if not playable:
        print("No playable cards! Drawing until playable...")
    while not playable:
        reshuffle_discards()
        card_count += 1
        hand.addCardToHand(draw_pile.removeAndReturnCard())
        for card in hand.deck:
            if card.isCardPlayable(top_card):
                playable = True
    if card_count > 0:
        print("Drew " + str(card_count) + " cards!")
    return


def reshuffle_discards():
    # Shuffles the discard pile and uses that for the draw pile, leaving the top card
    if draw_pile.get_card_count() == 0:
        for i in range(len(discard_pile[:-2])):
            draw_pile.addCardToHand(discard_pile.pop(0))
        draw_pile.shuffleDeck()


game_loop()