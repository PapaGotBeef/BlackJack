from Hand import Hand
from Card import Card
from Game import CardGame

class BlackJack(CardGame):
    def Play(self, names):
        self.hands =[]
        names.append('dealer')
        for name in names:
            self.hands.append(Hand(name))
        

        self.deck.deal(self.hands,2)
        print("------ Cards dealt")
        #self.dealerturn()
        scores = self.round()
        arr = BlackJack.bubbleSort(scores)
    
    def taketurn(self, hand):
           total =0 
           
           print(hand)
           for card in hand.cards:
               if card.rank ==1:
                   totaltest = total
                   totaltest += 11
                   #print(total)
                   if totaltest > 21:
                      total += card.rank
                      #print(total)
                   else:
                      total = totaltest
               elif card.rank >10:
                    total +=10
               else:
                    total += card.rank
               #print(total)
           if total == 21:
                   #print('BLACKJACK! YOU WIN '+ hand.name +'! \n')
                        
                    return(total)
           else:
                        
                    pass
           
           while total < 21 :
                total=0
                
                     
                ans= input(str(hand.name)+ " would you like to stand or hit? type 1 to hit or 2 to stand.")
                if int(ans) == 1:
                    newcard = self.deck.pop()   
                    
                    hand.add(newcard)
                    #print(hand)
                elif int(ans) == 2:
                    print('stand \n')
                    for card in hand.cards:
                        if card.rank ==1:
                            totaltest = total
                            totaltest += 11
                            #print(total)
                            if totaltest > 21:
                                 total += card.rank
                                 #print(total)
                            else:
                                 total = totaltest
                        elif card.rank >10:
                            total +=10
                        else:
                            total += card.rank
                    return(total)
                else:
                    print("please enter 1 or 2 \n")
                  
                for card in hand.cards:
                    if card.rank ==1:
                        totaltest = total
                        totaltest += 11
                        #print(total)
                        if totaltest > 21:
                            total += card.rank
                            #print(total)
                        else:
                            total = totaltest
                    elif card.rank >10:
                        total +=10
                    else:
                        total += card.rank 
                        #print(total)
                if total > 21:
                   print('Bust, you lose '+hand.name+ ' you\'re a loser. \n')
                   return(total)
                elif total == 21:
                     print('BLACKJACK! YOU WIN '+ hand.name +'! \n')
                     break   
                     return(total)
                else:
                        
                    pass
            
               
    def round(self):
        scores =[]
        score={}
        for hand in self.hands:
            total = self.taketurn(hand)
            if total == 21:
                print()
                return('BLACKJACK! '+str(hand.name)+', YOU WIN!')
            else:
                score = {'Name' : str(hand.name), 'Score': total}
                scores.append(score)
        return(scores)


    def print_hands(self):
        for hand in self.hands:
            print(hand)


    def anothercard(self,i):
         if i == 1:
               self.deck.deal(name,1)
         elif i == 2:
               print(stand)
         else:
               print("please enter 1 or 2")
        
   
        
    def dealerturn(self):
        dealer = self.hands[-1]
        #print(dealer)


    



    def bubbleSort(array):
        arr=[]
        winners = []
        for x in array:
            if x['Score'] < 21:
                arr.append(x['Score'])
            
        n = len(arr)
  
    
        for i in range(n-1):
    
  
            for j in range(0, n-i-1):
  
           
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        #print(arr)
        for i in array:
            if i['Score'] == arr[-1]:
                winners.append(i['Name'])
        if len(winners) == 1:
            print('The winner is '+str(winners[0])+' with ' + str(arr[-1]) + ' points!')

        else:
            print("The winners are "+str(winners)+" tied with "+ str(arr[-1])+ " points!")
                

            

        return(arr)