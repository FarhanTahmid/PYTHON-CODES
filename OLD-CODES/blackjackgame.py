##Step 1: Import the random module: This will be used to shuffle the deck prior to dealing. Then, declare variables to store suits, ranks and values

import random

suits = ('Hearts', 'Dimonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

#Step 2: Creating a Card Class: maing a class card because of suit and ranks

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + 'of' + self.suit  # Adding a __str__ method because of, when asked to print a Card, it shows and returns a string in the form "Two of Hearts"

##Step 3: Create a Deck Class : Main method of this is written on the copy

######test the whole code########

class Deck:
    def __init__(self):
        self.deck = [] #deck starts with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))           #card object banachhe and list e add korar jonno
    def __str__(self):
        deck_comp = '' #starts with an empty string
        for card in self.deck:
            deck_comp += '\n' +card. __str__()  ##shob gula card er print string add korar jonno (test run korte hobe)
        return 'The deck has:' + deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card

###Step 4: Creating a Hand Class: mainly card er value claculate korar jonno and ace er value jokhon jeta dorkar sheita dekhanor jonno
class Hand:
    def __init__(self):
        self.cards = [] ##deck clas er moton empty list diye start
        self.value = 0  ##zero value diye start hobe
        self.aces = 0   ## ace gular track rakhar jonno first e value 0 dite hoy
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

####Step 5: Create a Chips Class : player er starting chip, bet ar winning er upor track rakhar jonno
# Global variable clear na tai class diye kora

class Chips:
    def __init__(self):
        self.total = 100  ##user input er default value diye set hobe
        self.bet = 0
    def win_bet(self):
        self.total -= self.bet
    def lose_bet(self):
        self.total -= self.bet


###Step 6: bet newar jonno function

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        except ValueError:
            print("Sorry, a bet must be an integer number!")
        else:
            if chips.bet > chips.total:
                prnt("Sorry! yor bet can't be exceeded",chips.total)
            else:
                break

##Step 7: player hit nite chaile function


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace


##Step 8:function prompting the Player to Hit or Stand

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' to hit or 's' to stand ")

        if x[0].lower() == 'h':
            hit(deck,hand)  # hit function define kora

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


##Step 9: card display korar function

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')           #The asterisk * symbol is used to print every item in a collection, and the sep='\n ' argument prints each item on a separate line.
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

##Step 10: game scenarios. winning loosing draw or

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


#### Main code lines, main interface:

while True:
    #opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.\n\
    Stay halal bro!')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()               # remember the default value is 100, agei input dewa hoise

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing:               # recall this variable from hit_or_stand function
        hit_or_stand(deck,player_hand)       # Prompt for Player to Hit or Stand
        show_some(player_hand,dealer_hand)      # Show cards (ekta dealer card hidden thakbe)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    # Inform Player of their chips total
    print("\nPlayer's winnings stand at",player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break

        #Fucking end of the code#
