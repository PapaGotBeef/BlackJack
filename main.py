from Card import Card
from Deck import Deck
from Hand import Hand
from BlackJack import BlackJack
from Game import CardGame
def deal_dem_cards_boi():
    player = input("What's your name?")
    cards = input('How many cards do you want')
    deck = Deck()
    deck.shuffle()
    hand = Hand(player)
    deck.deal([hand],5)
    print(hand)
#deal_dem_cards_boi()
def game_time():
    i=1
    players=[]
    response =0
    while True:
        try:
            response = int(input("How many Players would like to play? Maximum number of players is 5."))
            if response > 5:
                print("Please enter an integer between 1 and 5")
            elif response < 1:
                print("Please enter an integer between 1 and 5")
            else:
                break
        
        except:
            print("Please enter an integer between 1 and 5")
                              
        
        
        

    for x in range(response):
         name = input("what is player "+str(i)+ "'s name?")
         players.append(name)
         i+=1
    game = BlackJack()
    game.Play(players)

game_time()

