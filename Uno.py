from UnoCardClass import Deck, Card
from Uno_objects import Player

player_list = []
discard_pile = []
draw_pile = None
game_won = False


def game_loop():

    global draw_pile
    global game_won
    draw_pile = Deck()
    game_won = False
    draw_pile.shuffleDeck()

    number_of_bots = process_player_count_input()

    player_list.append(Player("Human"))
    for i in range(number_of_bots):
        player_list.append(Player("Bot" + str(i+1), bot=True))
    discard_pile.append(draw_pile.removeAndReturnCard(0))
    for player in player_list:
        for i in range(10):
            player.hand.addCardToHand(draw_pile.removeAndReturnCard())
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
    p_c = str(input("How many players to play against?"))
    if not p_c.isdigit():
        print("Please enter only a number.")
        return process_player_count_input()
    else:
        return int(p_c)


def turn_loop(player_id):
    if draw_pile.get_card_count() == 0:
        for i in range(len(discard_pile[:-2])):
            draw_pile.append(discard_pile.pop(i))
        draw_pile.shuffleDeck()
    for player in player_list:
        if player.hand.get_card_count() == 0:
            global game_won
            game_won = True
            return
    # This loop will run perpetually until the game is over.
    # It is meant to serve as a single turn for a single player.
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
    top_card = discard_pile[-1]
    pick = str(pick)
    if not pick.isdigit():
        print("Invalid input. Please enter the number card you want to play, from the list above.")
        return validate_card_choice(input("Pick a card to play: "), hand)
    pick_id = int(pick)
    if hand.get_card_count() <= pick_id:
        print("Invalid input. Please enter the number card you want to play, from the list above.")
        return validate_card_choice(input("Pick a card to play: "), hand)
    card = hand.deck[pick_id]
    if not card.isCardPlayable(top_card):
        print("Card cannot be played! Choose another card.")
        return validate_card_choice(input("Pick a card to play: "), hand)
    return pick_id


def bot_logic(hand, top_card):
    for i in range(hand.get_card_count()):
        card = hand.deck[i]
        if card.isCardPlayable(top_card):
            return i


def list_player_cards(player_id):
    card_string = ''
    hand = player_list[player_id].hand
    for i in range(hand.get_card_count()):
        card = str(hand.deck[i])
        if i > 0 and i % 4 != 0:
            card_string += "\t"
        elif i % 4 == 0:
            card_string += "\n"
        card_string += str(i) + ": " + card
    return card_string


def draw_until_playable(hand, top_card, bot=False):
    playable = False
    card_count = 0
    for card in hand.deck:
        if card.isCardPlayable(top_card):
            playable = True
    if not playable:
        print("No playable cards! Drawing until playable...")
    while not playable:
        card_count += 1
        hand.addCardToHand(draw_pile.removeAndReturnCard())
        for card in hand.deck:
            if card.isCardPlayable(top_card):
                playable = True
    if card_count > 0:
        print("Drew " + str(card_count) + " cards!")
    return


game_loop()