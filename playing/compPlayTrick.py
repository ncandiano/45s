from dealing import *
def compPlayTrick(hand, playedCards, trump, ptakes):
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
    playedValues = trumpChecks.playHandValue(playedCards, trump)
    for key in playedValues:
        if trump in key or key == 'AH' or trickTrump in key:
            newValue = {key: playedValues[key]-12}
            playedValues.update(newValue)
    def throwHighOn(trumpDHand):
        for key in trumpDHand:
            if trumpDHand[key] == min(trumpDHand.itervalues()):
                card = str(key)
        return card
    def throwLowOn(trumpDHand):
        for key in trumpDHand:
            if trumpDHand[key] == max(trumpDHand.itervalues()):
                card = str(key)
        return card
    def beatItOn(trumpDHand, playedValues):
        tHand = {}
        for key in trumpDHand:
            if trumpDHand[key] < min(playedValues.itervalues()):
                newCard = {key: dHand[key]}
                tHand.update(newCard)
            for key in tHand:
                if tHand[key] == max(tHand.itervalues()):
                    card = str(key)
        return card
    def saveItOn(trumpDHand):
        saveItHand = {}
        for key in trumpDHand:
            if trumpDHand[key] != min(trumpDHand.itervalues()):
                newCard = {key: trumpDHand[key]}
                saveItHand.update(newCard)
            for key in saveItHand:
                if saveItHand[key] == min(saveItHand.itervalues()):
                    card = str(key)
        return card
    def throwHighTT(trickTrumpDHand):
        for key in trickTrumpDHand:
            if trickTrumpDHand[key] == min(trickTrumpDHand.itervalues()):
                card = str(key)
        return card
    def throwLowTT(trickTrumpDHand):
        for key in trickTrumpDHand:
            if trickTrumpDHand[key] == max(trickTrumpDHand.itervalues()):
                card = str(key)
        return card
    def throwHighOff(offDHand):
        for key in offDHand:
            if offDHand[key] == min(offDHand.itervalues()):
                card = str(key)
        return card
    def throwLowOff(offDHand):
        for key in offDHand:
            if offDHand[key] == max(offDHand.itervalues()):
                card = str(key)
        return card
    def splitCompHand(hand, trump, trickTrump):
        trumpHand = []
        trumpDHand = {}
        trickTrumpHand = []
        trickTrumpDHand = {}
        offHand = []
        offDHand = {}
        dHand = trumpChecks.playHandValue(hand, trump)
        if trickTrump == trump or trickTrump == '':
            trumpHand = [i for i in hand if trump in i or i == 'AH']
            for key in trumpHand:
                newCard = {key: (dHand[key]-12)}
                trumpDHand.update(newCard)
            offHand = [i for i in hand if trump not in i and i != 'AH']
            for key in offHand:
                newCard = {key: dHand[key]}
                offDHand.update(newCard)
            return trumpHand, trumpDHand, trickTrumpHand, trickTrumpDHand, offHand, offDHand, dHand
        else:
            trumpHand = [i for i in hand if trump in i or i == 'AH']
            if len(trumpHand) > 0:
                for key in trumpHand:
                    newCard = {key: (dHand[key]-12)}
                    trumpDHand.update(newCard)
            offHand = [i for i in hand if trump not in i and trickTrump not in i or i != 'AH']
            if len(offHand) > 0:
                for key in offHand:
                    newCard = {key: dHand[key]}
                    offDHand.update(newCard)
            trickTrumpHand = [i for i in hand if trickTrump in i and i != 'AH']
            for key in trickTrumpHand:
                newCard = {key: (dHand[key]-12)}
                trickTrumpDHand.update(newCard)
            return trumpHand, trumpDHand, trickTrumpHand, trickTrumpDHand, offHand, offDHand, dHand
    trumpHand, trumpDHand, trickTrumpHand, trickTrumpDHand, offHand, offDHand, dHand = splitCompHand(hand, trump, trickTrump)
    if len(hand) > 1:
        if len(playedCards) > 0:
            if trickTrump == trump or trickTrump == '':
                if len(playedCards) == 1:
                    if len(trumpDHand) > 0:
                        if min(trumpDHand.itervalues()) < min(playedValues.itervalues()):
                            if max(trumpDHand.itervalues()) <= -27:
                                if len(offDHand) > 0:
                                    card = throwLowOff(offDHand)
                                    return card
                                else:
                                    card = beatItOn(trumpDHand, playedValues)
                                    return card
                            else:
                                card = beatItOn(trumpDHand, playedValues)
                                return card
                        else:
                            card = throwLowOn(trumpDHand)
                            return card
                    else:
                        card = throwLowOff(offDHand)
                        return card
                elif len(playedCards) == 2:
                    if len(trumpDHand) > 0:
                        if playedValues[playedCards[0]] < playedValues[playedCards[1]]:
                            if max(trumpDHand.itervalues()) <= -27:
                                if len(offDHand) > 0:
                                    card = throwLowOff(offDHand)
                                    return card
                                else:
                                    card = throwLowOn(trumpDHand)
                                    return card
                            else:
                                card = throwLowOn(trumpDHand)
                                return card
                        else:
                            if len(trumpDHand) > 1:
                                if max(trumpDHand.itervalues()) < min(playedValues.itervalues()):
                                    card = saveItOn(trumpDHand)
                                    return card
                                elif min(trumpDHand.itervalues()) < min(playedValues.itervalues()):
                                    card = throwHighOn(trumpDHand)
                                    return card
                                else:
                                    card = throwLowOn(trumpDHand)
                                    return card
                            else:
                                card = throwHighOn(trumpDHand)
                                return card
                    else:
                        if len(offHand) > 0:
                            card = throwLowOff(offDHand)
                            return card
                        else:
                            card = throwLowOn(trumpDHand)
                            return card
                elif len(playedCards) == 3:
                    if len(trumpDHand) > 0:
                        if playedValues[playedCards[1]] == min(playedValues.itervalues()):
                            if max(trumpDHand.itervalues()) <= -27:
                                if len(offDHand) > 0:
                                    card = throwLowOff(offDHand)
                                    return card
                                else:
                                    card = throwLowOn(trumpDHand)
                                    return card
                            else:
                                card = throwLowOn(trumpDHand)
                                return card
                        else:
                            if min(trumpDHand.itervalues()) < min(playedValues.itervalues()):
                                card = beatItOn(trumpDHand, playedValues)
                                return card
                            else:
                                card = throwLowOn(trumpDHand)
                                return card
                    else:
                        if len(offDHand) > 0:
                            card = throwLowOff(offDHand)
                            return card
                        else:
                            card = throwLowOn(trumpDHand)
            elif trickTrump != trump:
                if len(playedCards) == 1:
                    if len(trickTrumpDHand) > 0:
                        card = throwLowTT(trickTrumpDHand)
                        return card
                    elif len(offDHand) > 0:
                        card = throwLowOff(offDHand)
                        return card
                    else:
                        card = throwLowOn(trumpDHand)
                        return card
                elif len(playedCards) == 2:
                    if len(trumpDHand) > 0:
                        if min(trumpDHand.itervalues()) < min(playedValues.itervalues()):
                                card = throwHighOn(trumpDHand)
                                return card
                        else:
                            if len(trickTrumpDHand) > 0:
                                card = throwLowTT(trickTrumpDHand)
                                return card
                            elif len(offDHand) > 0:
                                card = throwLowOff(offDHand)
                                return card
                            else:
                                card = throwLowOn(trumpDHand)
                                return card
                    elif len(trickTrumpDHand) > 0:
                        if min(trickTrumpDHand.itervalues()) < min(playedValues.itervalues()):
                            card = throwHighTT(trickTrumpDHand)
                            return card
                        else:
                            card = throwLowTT(trickTrumpDHand)
                            return card
                    else:
                        if len(offHand) > 0:
                            card = throwLowOff(offDHand)
                            return card
                        elif len(trickTrumpDHand) > 0:
                            card = throwLowTT(trickTrumpDHand)
                            return card
                        else:
                            card = throwLowOn(trumpDHand)
                            return card
                elif len(playedCards) == 3:
                    if playedValues[playedCards[1]] == min(playedValues.itervalues()):
                        if len(trickTrumpDHand) > 0:
                            card = throwLowTT(trickTrumpDHand)
                            return card
                        elif len(offDHand) > 0:
                            card = throwLowOff(offDHand)
                            return card
                        else:
                            card = throwLowOn(trumpDHand)
                            return card
                    else:
                        if len(trickTrumpDHand) > 0:
                            if min(trickTrumpDHand.itervalues()) < min(playedValues.itervalues()):
                                card = throwHighTT(trickTrumpDHand)
                                return card
                            else:
                                if len(trumpDHand) > 0:
                                    if min(trumpDHand.itervalues()) < min(playedValues.itervalues()):
                                        card = beatItOn(trumpDHand, playedValues)
                                        return card
                                    else:
                                        card = throwLowTT(trickTrumpDHand)
                                        return card
                                else:
                                    if len(trickTrumpDHand) > 0:
                                        card = throwLowTT(trickTrumpDHand)
                                        return card
                                    elif len(offDHand) > 0:
                                        card = throwLowOff(offDHand)
                                        return card
                        elif len(trumpDHand) > 0:
                                if min(trumpDHand.itervalues()) < min(playedValues.itervalues()):
                                    card = beatItOn(trumpDHand, playedValues)
                                    return card
                                else:
                                    if len(offDHand) > 0:
                                        card = throwLowOff(offDHand)
                                        return card
                                    else:
                                        card = throwLowOn(trumpDHand)
                                        return card
                        else:
                            card = throwLowOff(offDHand)
                            return card
        else:
            if len(hand) == 5:
                if len(trumpDHand) > 0:
                    if len(trumpDHand) > (.8*len(hand)):
                        if min(trumpDHand.itervalues()) < -36:
                            if ptakes < 4:
                                card = throwHighOn(trumpDHand)
                                return card
                            else:
                                card = throwLowOn(trumpDHand)
                                return card
                        else:
                            card = throwLowOn(trumpDHand)
                            return card
                    else:
                        card = throwLowOff(offDHand)
                        return card
                else:
                    card = throwLowOff(offDHand)
                    return card
            if len(hand) >= 3:
                if len(trumpDHand) > 0:
                    if len(trumpDHand) > (.6*len(hand)):
                        if min(trumpDHand.itervalues()) < -29:
                            if ptakes < 3:
                                card = throwHighOn(trumpDHand)
                                return card
                            else:
                                card = throwLowOn(trumpDHand)
                                return card
                        elif min(trumpDHand.itervalues()) < -23:
                            card = throwLowOn(trumpDHand)
                            return card
                        else:
                            if len(offDHand) > 0:
                                card = throwLowOff(offDHand)
                                return card
                            else:
                                card = throwLowOn(trumpDHand)
                                return card
                    else:
                        if len(offDHand) > 0:
                            card = throwLowOff(offDHand)
                            return card
                        else:
                            card = throwLowOn(trumpDHand)
                            return card
                else:
                    card = throwLowOff(offDHand)
                    return card
            if len(hand) >= 3:
                if len(trumpDHand) > 0:
                    if len(trumpDHand) > (.6*len(hand)):
                        if min(trumpDHand.itervalues()) < -23:
                            card = throwHighOn(trumpDHand)
                            return card
                        else:
                            card = throwLowOff(offDHand)
                            return card
                    else:
                        card = throwLowOff(offDHand)
                        return card
                else:
                    card = throwLowOff(offDHand)
                    return card
            elif len(hand) == 2:
                if len(trumpDHand) > 0:
                    if len(trumpDHand) >= (.5*len(hand)):
                        card = throwHighOn(trumpDHand)
                        return card
                    else:
                        card = throwLowOff(offDHand)
                        return card
                else:
                    card = throwLowOff(offDHand)
                    return card
            elif len(hand) == 1:
                card = hand[0]
                return card
    else:
        card = hand[0]
        return card
