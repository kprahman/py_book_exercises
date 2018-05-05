class Card:

    ## Class attributes are defined outside methods, and can be accessed
    ## from any of the methods in the class.
    ## think of this as 'base data.' generally, i do not want to edit this!
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf","2","3","4","5","6","7","8","9","10", "Jack", "Queen", "King", "Ace" ]

    def __init__(self, suit = 0, rank = 0):
        """Suit: [0] = Clubs, [1] = Diamonds, [2] = Hearts, [3] = Spades"""
        self.suit = suit
        self.rank = rank    

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4): ## for every suit
            for rank in range(1,14): ## for every card within a suit
                self.cards.append(Card(suit,rank)) ## add the card to the list

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + \
                str(self.cards[i]) + "\n" ## even though its 52 lines,
        return s                          ## this is actually just 1 string

    def print_deck(self):
        for card in self.cards:
            print(card)

    def shuffle_long(self):
        """shows logic behind shuffling. take an unshuffled card
        and replace it with a random one within the range"""
        import random
        rng = random.Random()
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = rng.randrange(i,num_cards) ## choose a card that hasnt been shuffled yet
            (self.cards[i], self.cards[j]) = (self.cards[j],self.cards[i]) ## switch!

    def shuffle(self):
        import random
        rng = random.Random()
        rng.shuffle(self.cards)

    def remove(self,card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []
red_deck = Deck()
print(red_deck)
