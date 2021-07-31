from collections import namedtuple
from random import shuffle

Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "clubs diamonds hearts spades".split()

    def __init__(self):
        self._card = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]

    def __repr__(self):
        return f'FrenchDeck(Card([2-9, J, Q, K, A], [{",".join(self.suits)}]))'

    def shuffle(self):
        shuffle(self._card)


def spade_high(card: Card) -> int:
    suit_values = dict(clubs=1, diamonds=2, hearts=3, spades=4)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return (rank_value * len(suit_values)) + suit_values[card.suit]


deck = FrenchDeck()
print(*deck, sep="\n")
print()
deck.shuffle()
print(*deck, sep="\n")
print()
print(*sorted(deck, key=spade_high), sep="\n")

print(deck)
