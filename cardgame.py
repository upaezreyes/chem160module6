from cards import *
ntrials = 10000   # number of trials
awins = 0   # to keep track wins

for i in range(ntrials):
    adeck=deck()     # creates  a deck on adeck
    adeck.shuffle()   # shuffles the deck
    ascore = 0    # keep track of ascore
    bscore = 0    # keep track of bscore

    while adeck.cardsleft()>2:     # the loop will break when 2 cards are left
        acard1 = adeck.dealcard()   # get a value for acard1
        acard2 = adeck.dealcard()   # get a value for acard2
        bcard = adeck.dealcard()    # get a value for acard2

        if acard1.value() > bcard.value() or acard2.value() > bcard.value():
            ascore += 1   
        else:
            bscore += 1
    if ascore > bscore:
        awins += 1
print("Player A win percentage=",awins/ntrials)




    
