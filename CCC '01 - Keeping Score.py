# get input
# add indication for end of string 
cards = input() + "X"
# initialize variables
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
current_suit = 0
suit_cards = []
total_points = 0
points = 0

print("Cards Dealt              Points")

# loop through cards
for card in cards:
  # skip C
  if card == "C":
    continue

  # if end of a suit
  if card in ["D", "H", "S", "X"]:
    # assign void, singleton, and doubleton points
    points += max(0, 3 - len(suit_cards))
    print(suits[current_suit], *suit_cards, "   ", points)
    total_points += points

    # reset variables for next suit
    points = 0
    suit_cards = []
    current_suit += 1

  # do not include suit indicator as a card
  else:
    # add any card points
    if card == "A": points += 4
    elif card == "K": points += 3
    elif card == "Q": points += 2
    elif card == "J": points += 1

    # add card to suit
    suit_cards.append(card)


print("                       Total", total_points)
