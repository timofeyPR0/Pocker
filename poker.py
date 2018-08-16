from random import shuffle
color = dict(zip(['s','c','h','d'],['♠','♣','♥','♦']))
number = dict(zip([i for i in range(13)],['1','2','3','4','5','6','7','8','9','J','Q','K','A']))
def newDeck():
    deck = []
    for i in ['s','c','h','d']:
        for j in range(13):
            deck.append([j,i])
    shuffle(deck)
    return deck
def card(pair):
    global color, number
    return number[pair[0]]+color[pair[1]]
def distr(players,deck):
    cards = []
    for i in range(players):
        cards.append([deck[0],deck[1]])
        deck.pop(0)
        deck.pop(0)
    return cards
def game(cash,blind):
    dealer = cycle % n
    bank = blind*3
    allin = set()
