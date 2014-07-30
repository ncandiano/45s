import random
hT = {'5H': -35, 'JH': -20, 'KH': -10, 'QH': -9, '10H': -8, '9H': -7, '8H': -6, '7H': -5, '6H': -4, '4H': -3, '3H': -2, '2H': -1}
dT = {'5D': -35, 'JD': -20, 'AD': -12, 'KD': -10, 'QD': -9, '10D': -8, '9D': -7, '8D': -6, '7D': -5, '6D': -4, '4D': -3, '3D': -2, '2D': -1}
sT= {'5S': -35, 'JS': -20, 'AS': -12, 'KS': -10, 'QS': -9, '2S': -8, '3S': -7, '4S': -6, '6S': -5, '7S': -4, '8S': -3, '9S': -2, '10S': -1}
cT= {'5C': -35, 'JC': -20, 'AC': -12, 'KC': -10, 'QC': -9, '2C': -8, '3C': -7, '4C': -6, '6C': -5, '7C': -4, '8C': -3, '9C': -2, '10C': -1}
hO = {'2H': 11, '3H': 10, '4H': 9, '5H': 8, '6H': 7, '7H': 6, '8H': 5, '9H': 4, '10H': 3, 'JH': 2, 'QH': 1, 'KH': 0}
dO = {'AD': 12, '2D': 11, '3D': 10, '4D': 9, '5D': 8, '6D': 7, '7D': 6, '8D': 5, '9D': 4, '10D': 3, 'JD': 2, 'QD': 1, 'KD': 0}
sO = {'AS': 3, '2S': 4, '3S': 5, '4S': 6, '5S': 7, '6S': 8, '7S': 9, '8S': 10, '9S': 11, '10S': 12, 'JS': 2, 'QS': 1, 'KS': 0}
cO = {'AC': 3, '2C': 4, '3C': 5, '4C': 6, '5C': 7, '6C': 8, '7C': 9, '8C': 10, '9C': 11, '10C': 12, 'JC': 2, 'QC': 1, 'KC': 0}
aceH = {'AH': -18}
def playHandValue(list, trump):
    #assigns final cards for hand their values#
    #cards are rated depending on if trump or offsuit#
    #returns a dict, cards are keys, ratings are values#
    dictHand = {}
    for i in list:
        if trump in i:
            if i in hT:
                newCard = {i: hT[i]}
                dictHand.update(newCard)
            elif i in dT:
                newCard = {i: dT[i]}
                dictHand.update(newCard)
            elif i in cT:
                newCard = {i: cT[i]}
                dictHand.update(newCard)
            elif i in sT:
                newCard = {i: sT[i]}
                dictHand.update(newCard)
        else:
            if i in hO:
                newCard = {i: hO[i]}
                dictHand.update(newCard)
            elif i in dO:
                newCard = {i: dO[i]}
                dictHand.update(newCard)
            elif i in cO:
                newCard = {i: cO[i]}
                dictHand.update(newCard)
            elif i in sO:
                newCard = {i: sO[i]}
                dictHand.update(newCard)
        if i == 'AH':
            dictHand.update({'AH': -18})
    return dictHand
def compTossCards(dHand, hand, trump):
    minCheck = min(dHand.itervalues())
    if minCheck < 0:
        for key in dHand.keys():
            if trump not in key:
                if key != 'AH':
                    del dHand[key]
    else:
        for key, value in dHand.items():
            if value != minCheck:
                del dHand[key]
        if len(dHand) > 1:
            for key in random.sample(dHand.keys(), 1):
                del dHand[key]
        if len(dHand) > 5:
            for key in dHand:
                if dHand[key] == max(dHand.itervalues()):
                    del dHand[key]
    hand = [k for k in hand if k in dHand.keys()]
    return dHand, hand
def trumpCheckReneg(leadCard, card, hand, trump):
    newHand = []
    a = str('5'+trump)
    b = str('J'+trump)
    c = 'AH'
    if a in str(leadCard):
        if trump not in str(card):
            if card == c:
                return True
            elif trump in str(hand):
                return False
            elif c in str(hand):
                return False
            else:
                return True
        else:
            return True
    elif b in str(leadCard):
        newHand = [i for i in hand if i != a]
        if trump not in str(card):
            if card == c:
                return True
            elif trump in str(newHand):
                return False
            elif c in str(newHand):
                return False
            else:
                return True
        else:
            return True
    elif c in str(leadCard):
        newHand = [i for i in hand if i != a and i != b]
        if trump not in str(card):
            if trump in str(newHand):
                return False
            else:
                return True
        else:
            return True
    elif trump in str(leadCard):
        newHand = [i for i in hand if i != a and i != b and i != c]
        if trump not in str(card) and card != c:
            if trump in str(newHand):
                return False
            else:
                return True
        else:
            return True
    else:
        return True
def trickTrumpCheckReneg(card, hand, trickTrump, trump):
    newHand = [i for i in hand if i != 'AH']
    if trump in card or card == 'AH':
        return True
    elif trickTrump not in str(card):
        if trickTrump in str(newHand):
            return False
        else:
            return True
    else:
        return True
def scoreTrick(playedCards, card1, card2, card3, card4, trump):
    trickTrump = ''
    if len(playedCards) > 0:
        leadCard = playedCards[0]
        if leadCard == 'AH':
            trickTrump = trump
        elif trump not in leadCard:
            if len(leadCard) == 2:
                trickTrump = leadCard[1]
            elif len(leadCard) == 3:
                trickTrump = leadCard[2]
    playedValues = playHandValue(playedCards, trump)
    for key in playedValues:
        if trump in key or trickTrump in key or key == 'AH':
            playedValues[key] = playedValues[key] - 12
    trumpHand = []
    trumpDHand = {}
    trickTrumpHand = []
    trickTrumpDHand = {}
    trumpHand = [i for i in playedCards if trump in i or i == 'AH']
    if len(trumpHand) > 0:
        for key in trumpHand:
            newCard = {key: playedValues[key] - 12}
            trumpDHand.update(newCard)
        for key in trumpDHand:
            if trumpDHand[key] == min(trumpDHand.itervalues()):
                winCard = str(key)
                winVal = {key: playedValues[key] - 12}
    else:
        trickTrumpHand = [i for i in playedCards if trickTrump in i and i != 'AH']
        for key in trickTrumpHand:
            newCard = {key: playedValues[key] - 12}
            trickTrumpDHand.update(newCard)
        for key in trickTrumpDHand:
            if trickTrumpDHand[key] == min(trickTrumpDHand.itervalues()):
                winCard = str(key)
                winVal = {key: playedValues[key] - 12}
    if winCard == card1:
        winner = 'P1'
    elif winCard == card2:
        winner = 'P2'
    elif winCard == card3:
        winner = 'P3'
    elif winCard == card4:
        winner = 'P4'
    return winVal, winner, winCard
