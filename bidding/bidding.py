import os
hT = {'5H': -35, 'JH': -20, 'KH': -10, 'QH': -9, '10H': -8, '9H': -7, '8H': -6, '7H': -5, '6H': -4, '4H': -3, '3H': -2, '2H': -1}
dT = {'5D': -35, 'JD': -20, 'AD': -12, 'KD': -10, 'QD': -9, '10D': -8, '9D': -7, '8D': -6, '7D': -5, '6D': -4, '4D': -3, '3D': -2, '2D': -1}
sT= {'5S': -35, 'JS': -20, 'AS': -12, 'KS': -10, 'QS': -9, '2S': -8, '3S': -7, '4S': -6, '6S': -5, '7S': -4, '8S': -3, '9S': -2, '10S': -1}
cT= {'5C': -35, 'JC': -20, 'AC': -12, 'KC': -10, 'QC': -9, '2C': -8, '3C': -7, '4C': -6, '6C': -5, '7C': -4, '8C': -3, '9C': -2, '10C': -1}
hO = {'2H': 11, '3H': 10, '4H': 9, '5H': 8, '6H': 7, '7H': 6, '8H': 5, '9H': 4, '10H': 3, 'JH': 2, 'QH': 1, 'KH': 0}
dO = {'AD': 12, '2D': 11, '3D': 10, '4D': 9, '5D': 8, '6D': 7, '7D': 6, '8D': 5, '9D': 4, '10D': 3, 'JD': 2, 'QD': 1, 'KD': 0}
sO = {'AS': 3, '2S': 4, '3S': 5, '4S': 6, '5S': 7, '6S': 8, '7S': 9, '8S': 10, '9S': 11, '10S': 12, 'JS': 2, 'QS': 1, 'KS': 0}
cO = {'AC': 3, '2C': 4, '3C': 5, '4C': 6, '5C': 7, '6C': 8, '7C': 9, '8C': 10, '9C': 11, '10C': 12, 'JC': 2, 'QC': 1, 'KC': 0}
aceH = {'AH': -18}
suits = {'H': 'Hearts', 'D': 'Diamonds', 'S': 'Spades', 'C': 'Clubs'}
bidList = []
def assignValue(list):
    #takes cards dealt and assigns value, before or after bidding round#
    #gives back a list, ranking each of the 4 suits as a number#
    #list will be in order Spades, Clubs, Hearts, Diamonds#
    H = 0
    C = 0
    S = 0
    D = 0
    for i in list:
        if i in hT:
            H += hT[i]
        if i in cT:
            C += cT[i]
        if i in sT:
            S += sT[i]
        if i in dT:
            D += dT[i]
    if 'AH' in list:
        H -= 15
        S -= 13
        D -= 13
        C -= 13
    ranks = {'h': H, 's': S, 'd': D, 'c': C}
    for key in ranks:
        if ranks[key] == min(H, S, D, C):
            return key, ranks[key]
def biddingOrder(string):
    if string == 'P1':
        return ['P2', 'P3', 'P4', 'P1']
    elif string == 'P2':
        return ['P3', 'P4', 'P1', 'P2']
    elif string == 'P3':
        return ['P4', 'P1', 'P2', 'P3']
    elif string == 'P4':
        return ['P1', 'P2', 'P3', 'P4']
def getDealer(lastDealer):
    if lastDealer == 'P1':
        return 'P2'
    if lastDealer == 'P2':
        return 'P3'
    if lastDealer == 'P3':
        return 'P4'
    if lastDealer == 'P4':
        return 'P1'
def isValidBid(int, bidList):
    validBids = [15, 20, 25, 30, 0]
    if int not in validBids:
            print ''
            print 'Invalid bid. Valid bids are: '
            print ''
            for item in bidList:
                print item
            print ''
            print 'Try again stupid.'
            print ''
            return False
    elif int != 0 and len(bidList) != 0 and int <= max(bidList):
            print ''
            print 'Someone already bid that!'
            print ''
            return False
    else:
        return True
def compBid(hand, bidList, bidCount):
    suit, handStrength = assignValue(hand)
    bid = 0
    if bidCount == 0:
        maxBid = 0
    else:
        maxBid = max(bidList)
    if maxBid < 30:
        if handStrength > -25:
            bid = 0
        elif handStrength <= -25 and handStrength > -36:
            bid = 15
        elif handStrength <= -37 and handStrength > -51:
            if maxBid == 15:
                bid = 20
            else:
                bid == 15
        elif handStrength <= -51 and handStrength > -61:
            if maxBid <=20:
                bid = 0
            else:
                bid = 20
        elif handStrength <= -61 and handStrength >= -69:
            if maxBid < 20:
                bid = 20
            else:
                bid = 25
        elif handStrength <= -70:
            if maxBid < 25:
                bid = 25
            else:
                bid = 30
    if bid == 0 and maxBid == 0 and bidCount == 3:
        bid = 15
        print 'The Dealer Got Bagged!'
        print ''
        return bid
    elif bid <= maxBid:
        bid = 0
        return bid
    else:
        return bid
def getPlayerBid(hand1, bidList, bidCount):
    if bidCount == 0:
        maxBid = 0
    else:
        maxBid = max(bidList)
    if bidCount == 3 and maxBid == 0:
        print '--------------------------------------------'
        print 'You got bagged!'
        print 'Your bid is 15 like it or not!'
        print '--------------------------------------------'
        print ''
        bid1 = 15
    else:
        print '--------------------------------------------'
        print 'Your Cards: ' + " ".join(hand1)
        print '--------------------------------------------'
        print ''
        try:
            bid1 = int(raw_input('What\'s your bid?(Enter 0 to pass): '))
            print '------------------------------------------------------'
        except ValueError:
            print ''
            print 'Bid again! Try a number this time!'
            print ''
            return getPlayerBid(hand1, bidList, bidCount)
        bidCheck = isValidBid(bid1, bidList)
        if bidCheck == False:
            return getPlayerBid(hand1, bidList, bidCount)
        elif bidCheck == True and bid1 == 0 and bidCount < 3:
            print ''
            print 'Player 1 Passes!'
            print ''
        else:
            print ''
            print 'Player 1 bids: ' + str(bid1)
            print ''
    return bid1
def playerChooseTrump(hand):
    print '--------------------------------------------'
    print 'Your Cards: ' + " ".join(hand)
    print '--------------------------------------------'
    print ''
    trump = ''
    suits = ['H', 'S', 'C', 'D']
    while True:
        trump = raw_input('You win the bid! Choose your suit!(H,S,C,or D): ').upper()
        if trump in suits:
            return trump
        else:
            print 'Y U No follow simple instructions??'
            print ''
            return playerChooseTrump(hand)
def compChooseTrump(hand):
    suit, handStrength = assignValue(hand)
    return suit.upper()
def bidRound(dealer, hand1, hand2, hand3, hand4, t1Score, t2Score):
    os.system('cls' if os.name == 'nt' else 'clear')
    print '--------------------------------------------'
    print 'Your Team Score: ' + str(t1Score)
    print ''
    print 'Opponents Score: ' + str(t2Score)
    print '--------------------------------------------'
    print ''
    print 'Time to bid!'
    print ''
    bidList = []
    bidOrder = biddingOrder(dealer)
    bid1 = 0
    bid2 = 0
    bid3 = 0
    bid4 = 0
    bidCount = 0
    trump = ''
    winner = ''
    for i in range(len(bidOrder)):
        if bidOrder[i] == 'P1':
            bid1 = getPlayerBid(hand1, bidList, bidCount)
            bidList.append(bid1)
            bidCount += 1
        elif bidOrder[i] == 'P2':
            bid2 = compBid(hand2, bidList, bidCount)
            bidList.append(bid2)
            bidCount += 1
            if bid2 == 0:
                print 'Player 2 Passes!'
                print ''
            else:
                print 'Player 2 bids: ' + str(bid2)
                print ''
        elif bidOrder[i] == 'P3':
            bid3 = compBid(hand3, bidList, bidCount)
            bidList.append(bid3)
            bidCount += 1
            if bid3 == 0:
                print 'Your Partner Passes!'
                print ''
            else:
                print 'Your Partner bids: ' + str(bid3)
                print ''
        elif bidOrder[i] == 'P4':
            bid4 = compBid(hand4, bidList, bidCount)
            bidList.append(bid4)
            bidCount += 1
            if bid4 == 0:
                print 'Player 4 Passes!'
                print ''
            else:
                print 'Player 4 bids: ' + str(bid4)
                print ''
    winningBid = max(bidList)
    if bid1 == winningBid:
        winner = 'P1'
        trump = playerChooseTrump(hand1)
        print ''
        print 'Player 1 goes %d in %s' % (winningBid, suits[trump])
    elif bid2 == winningBid:
        winner = 'P2'
        trump = compChooseTrump(hand2)
        print 'Player 2 goes %d in %s' % (winningBid, suits[trump])
    elif bid3 == winningBid:
        winner = 'P3'
        trump = compChooseTrump(hand3)
        print 'Your Partner goes %d in %s' % (winningBid, suits[trump])
    elif bid4 == winningBid:
        winner = 'P4'
        trump = compChooseTrump(hand4)
        print 'Player 4 goes %d in %s' % (winningBid, suits[trump])
    print ''
    return winner, trump, winningBid
