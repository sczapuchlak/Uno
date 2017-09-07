
player_list = []
discard_pile = []
draw_pile = []


def turn_loop(player_id):
    # This loop will run perpetually until the game is over.
    # It is meant to serve as a single turn for a single player.

    card_num = discard_pile[0].cardNumber
    card_color = discard_pile[0].cardColor

    if player_list[player_id].is_bot:
        # Do bot logic
        dummy_bot_logic()
    else:
        # We are a human player; so provide the inputs.
        print("Top card is a " + card_color + " " + card_num + ".\nChoose a card to play:")
        print(list_player_cards(player_id))
        card = validate_card_choice(input("Pick a card to play: "), player_list[player_id].hand)
        print("You played a " + card.cardColor + " " + card.cardNumber)
        discard_pile.reverse()
        discard_pile.append(card)
        discard_pile.reverse()
    player_id += 1
    player_id %= len(player_list)
    turn_loop(player_id)


def validate_card_choice(pick, hand):
    top_card = discard_pile[0]
    pick = str(pick)
    if not pick.isdigit():
        print("Invalid input. Please enter the number card you want to play, from the list above.")
        return validate_card_choice(input("Pick a card to play: "), hand)
    pick_id = int(pick)
    if len(hand) <= pick_id:
        print("Invalid input. Please enter the number card you want to play, from the list above.")
        return validate_card_choice(input("Pick a card to play: "), hand)
    card = hand[pick_id]
    if not card.isCardPlayable(top_card):
        print("Card cannot be played! Choose another card.")
        return validate_card_choice(input("Pick a card to play: "), hand)
    return card


def dummy_bot_logic():
    return


def list_player_cards(player_id):
    card_string = ''
    hand = player_list[player_id].hand
    for i in range(len(hand)):
        if i > 0 and i % 4 != 0:
            card_string += "\t"
        elif i % 4 == 0:
            card_string += "\n"
        card_string += str(i) + ": " + hand[i].cardColor + " " + hand[i].cardNumber
    return card_string
