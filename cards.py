import random

suits = ['DIAMONDS', 'HEARTS', 'SPADES', 'CLUBS']
colors = ['RED', 'BLACK']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card:
    def __init__(self, name, color, suit):
        self.suit = suit
        self.name = name
        self.color = color


class Deck:

    def __init__(self):
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def draw_random(self):
        drawn = random.choice(self.cards)
        self.cards.remove(drawn)
        return drawn

    def draw_value(self, name, color, suit):
        drawn = Card(name, color, suit)
        self.cards.remove(drawn)
        return drawn

    def deal(self, people, hand_size):
        if people * hand_size <= len(self.cards):
            players = []
            for i in range(people):
                deck = Deck()
                deck.cards.append(self.cards.pop())
                players.append(deck)
            for x in range(1, hand_size):
                for player in players:
                    player.cards.append(self.cards.pop())
            return players


def init52(deck):
    for suit in suits:
        for value in values:
            card = Card(value, None, suit)
            if suit == 'DIAMONDS' or suit == 'HEARTS':
                card.color = 'RED'
            else:
                card.color = 'BLACK'
            deck.cards.append(card)
