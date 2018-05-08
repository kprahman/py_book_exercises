class Card:
    ## Class attributes are defined outside methods, and can be accessed
    ## from any of the methods in the class.
    ## think of this as 'base data.' generally, i do not want to edit this!
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit=0, rank=0):
        """Suit: [0] = Clubs, [1] = Diamonds, [2] = Hearts, [3] = Spades"""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.ranks[self.rank] + " of " + self.suits[self.suit]

    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):  ## for every suit
            for rank in range(1, 14):  ## for every card within a suit
                self.cards.append(Card(suit, rank))  ## add the card to the list

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + \
                str(self.cards[i]) + "\n"  ## even though its 52 lines,
        return s  ## this is actually just 1 string

    def sting_card(self):
        """Converts a card to a string and adds it to a list"""
        card_list = []
        for i in range(len(self.cards)):
            s = str(self.cards[i])
            card_list.append(s)
        return card_list

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
            j = rng.randrange(i, num_cards)  ## choose a card that hasnt been shuffled yet
            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])  ## switch!

    def shuffle(self):
        import random
        rng = random.Random()
        rng.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():  ##inherited from Deck
                break
            card = self.pop()
            hand = hands[i % num_hands]  ## picks a player to deal to.
            hand.add(card)


class Hand(Deck):  ##parentheses indicate that Hand is the child of Deck edit: LOL
    def __init__(self, name=""):
        super().__init__()
        self.cards = []  ## every hand has a set of cards
        self.name = name  ##name of the owner?

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty!\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)

    def add(self, card):
        self.cards.append(card)  # adds the new card to the hand


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


class OldMaidHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]  ## creates a copy of cards.
        ## since self.cards is going to be
        ## modified, we don't want it to control traversal
        for card in original_cards:  ## since self.cards not defined here, inherited from Hand classP
            match = Card(3 - card.suit, card.rank)  ## every card has a suit and a tank attribute.
            if match in self.cards:  ## we're searching for matches in color and rank.
                self.cards.remove(card)  ##if a match is found, remove the card and its match
                self.cards.remove(match)  ##remember is defined in Deck. Removes a card of object from card list
                print("Hand {0} : {1} matches {2}"
                      .format(self.name, card, match))
                count += 1
        return count


class OldMaidGame(CardGame):
    ## OMG init inherited from CG init, so a shuffled deck.
    def remove_all_matches(self):
        count = 0
        for hand in self.hands:  ##for every hand in the game
            count += hand.remove_matches()  ##count the number of matches
        return count  ##count is how we determine when to exit the game. when 50 cards have been matched, we're done.

    def find_neighbor(self, i):
        """Rotates through players until someone has cards"""
        num_hands = len(self.hands)
        for player in range(1, num_hands):
            neighbor = (i + player) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor  ##return ENDS the loop.

    def print_hands(self):
        for hand in self.hands:
            print(hand)

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()  ##ensures next player's choice is random
        return count

    def play(self, names):
        self.deck.remove(Card(0, 11))  ##remove Q Clubs to create Old Maid
        # now make hands
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))
        # deal cards
        self.deck.deal(self.hands)
        print("---------------Cards have been dealt!")
        self.print_hands()
        # remove initial matches
        matches = self.remove_all_matches()
        print("---------------Matches discarded. Let's begin!")
        self.print_hands()
        # play until all 50cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:  # when matches = 25, 50 cards have been matched,
            matches += self.play_one_turn(turn)  # whoever's turn it is gets to play/
            turn = (turn + 1) % num_hands  # round-robin

        print("---------------Game is over!")
        self.print_hands()


game = OldMaidGame()
game.play(["a", "b", "c"])
