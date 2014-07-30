import random
from time import sleep
import trumpChecks
cards = ['AS', 'KS', 'QS', 'JS', '10S', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S',\
         'AD', 'KD', 'QD', 'JD', '10D', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D',\
         'AC', 'KC', 'QC', 'JC', '10C', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C',\
         'AH', 'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H']
usedDeck = []
hand1 = []
hand2 = []
hand3 = []
hand4 = []
kitty = []
hands= ''
def splitHands(list):
    hand1 = []
    hand2 = []
    hand3 = []
    hand4 = []
    a = len(list)
    if a == 2:
        for i in range(len(list[0])):
            hand1.append(list[0][i])
        for i in range(len(list[0])):
            hand2.append(list[1][i])
    elif a == 3:
        for i in range(len(list[0])):
            hand1.append(list[0][i])
        for i in range(len(list[0])):
            hand2.append(list[1][i])
        for i in range(len(list[0])):
            hand3.append(list[2][i])
    elif a == 4:
        for i in range(len(list[0])):
            hand1.append(list[0][i])
        for i in range(len(list[1])):
            hand2.append(list[1][i])
        for i in range(len(list[2])):
            hand3.append(list[2][i])
        for i in range(len(list[3])):
            hand4.append(list[3][i])
    return hand1, hand2, hand3, hand4
def dealHand(numPlayers):
    random.shuffle(cards)
    usedDeck = list(cards)
    n = int(numPlayers)
    kitty = []
    hands = [[] for _ in range(n)]
    hand1 = []
    hand2 = []
    hand3 = []
    hand4 = []
    y = range(len(hands))
    for x in range(0, 3):
        kitty.append(usedDeck.pop(0))
    for i in y:
        while len(hands[i]) < 5:
            for x in range(len(hands)):
                hands[x].append(usedDeck.pop(0))
    else:
        hand1, hand2, hand3, hand4 = splitHands(hands)
    return hand1, hand2, hand3, hand4, hands, kitty, usedDeck
def dealAgain(hands, usedDeck):
    p1takes = 0
    p2takes = 0
    p3takes = 0
    p4takes = 0
    if len(hands[0]) < 5:
        p1takes = 5 - len(hands[0])
    if len(hands[1]) < 5:
        p2takes = 5 - len(hands[1])
    if len(hands[2]) < 5:
        p3takes = 5 - len(hands[2])
    if len(hands[3]) < 5:
        p4takes = 5 - len(hands[3])
    for i in range(len(hands)):
        while len(hands[i]) < 5:
            hands[i].append(usedDeck.pop(0))
    hand1, hand2, hand3, hand4 = splitHands(hands)
    return hand1, hand2, hand3, hand4, p1takes, p2takes, p3takes, p4takes
def addKitty(hand, kitty):
    hand = list(set(hand + kitty))
    return hand
def playerDumpCards(hand):
    while len(hand) > 1:
        print 'Your Cards: ' + " ".join(hand)
        sleep(.1)
        a = raw_input('Wanna dump some cards?(Enter Y for yes, N for no.): ').upper()
        if a == 'Y':
            cardsToLose = raw_input('Which ones?').upper()
            cardsToLose = cardsToLose.split()
            for item in cardsToLose:
                if item in hand:
                    hand.remove(item)
                else:
                    print item + ' is not in your hand.'
            print 'Your Cards: ' + " ".join(hand)
            b = raw_input('Did you miss any?(Enter Y for yes, N for no.)').upper()
            if b == 'Y':
                playerDumpCards = True
            elif b == 'N':
                return hand
            else:
                print 'Not sure what you meant...'
                playerDumpCards = True
        elif a == 'N':
            if len(hand) > 5:
                print 'You can\'t keep that many cards, guy. 5 max.'
                playerDumpCards == True
            else:
                return hand
        else:
            print 'Thought I made this pretty simple.'
            playerDumpCards == True
    else:
        return hand
def modHands(winner, kitty, hand1, hand2, hand3, hand4, trump, usedDeck):
    hands = [[], [], [], []]
    if winner == 'P1':
        hand1 = addKitty(hand1, kitty)
    elif winner == 'P2':
        hand2 = addKitty(hand2, kitty)
    elif winner == 'P3':
        hand3 = addKitty(hand3, kitty)
    elif winner == 'P4':
        hand4 = addKitty(hand4, kitty)
    dhand1 = trumpChecks.playHandValue(hand1, trump)
    dhand2 = trumpChecks.playHandValue(hand2, trump)
    dhand3 = trumpChecks.playHandValue(hand3, trump)
    dhand4 = trumpChecks.playHandValue(hand4, trump)
    print '--------------------------------------------'
    print 'Your cards: ' + ' '.join(hand1)
    print '--------------------------------------------'
    print ''
    a = raw_input('Auto trim hand?(Y or N) ').upper()
    if a == 'Y':
        dhand1, hand1 = trumpChecks.compTossCards(dhand1, hand1, trump)
    else:
        hand1 = playerDumpCards(hand1)
    dhand2, hand2 = trumpChecks.compTossCards(dhand2, hand2, trump)
    dhand3, hand3 = trumpChecks.compTossCards(dhand3, hand3, trump)
    dhand4, hand4 = trumpChecks.compTossCards(dhand4, hand4, trump)
    hands[0] = hand1
    hands[1] = hand2
    hands[2] = hand3
    hands[3] = hand4
    hand1, hand2, hand3, hand4, p1takes, p2takes, p3takes, p4takes = dealAgain(hands, usedDeck)
    dhand2 = trumpChecks.playHandValue(hand2, trump)
    dhand3 = trumpChecks.playHandValue(hand3, trump)
    dhand4 = trumpChecks.playHandValue(hand4, trump)
    return hand1, hand2, hand3, hand4, dhand2, dhand3, dhand4, p1takes, p2takes, p3takes, p4takes
