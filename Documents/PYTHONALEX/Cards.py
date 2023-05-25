
#List , If for LOOP,INT.
cards = ['Ace ','Jack','Queen','King','Spades','Hearts','Clubs','Diamonds']

points=0
for x in range (6):
    import random
    random.shuffle(cards) # shuffle
    print("current card is ", cards[0]) # Pick the 1st Card 

    random.shuffle(cards) #Shuffle Again 
    # Let the player geuss what card is at position 0
    answer =str(input('can you geuss next card ?:'))

    # Check if the card user entered is same as card as index 0
    if answer == cards [0]:
      print('correct',cards [0])
      points = points+ 2
    else: 
        print('Its wrong ! Card was  ',cards[0])

print("Game Over. You scored ",points)
