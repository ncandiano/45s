from dealing import *
from playing import compPlayTrick
from bidding import *
def playerTrick(trump, playedCards, hand, bid):
    while True:
        print ''
        card = raw_input('Which card would you like to play? ').upper()
        if len(playedCards) == 0:
            if card in hand:
                print ''
                print 'Player plays: ' + card
                return card
            else:
                print 'You don\'t have that card!'
                print ''
                return playerTrick(trump, playedCards, hand, bid)
        elif len(playedCards) > 0:
            leadCard = playedCards[0]
            if trump in leadCard or leadCard == 'AH':
                if card in hand:
                    if trumpChecks.trumpCheckReneg(leadCard, card, hand, trump) == True:
                        print ''
                        print 'Player plays: ' + card
                        return card
                    else:
                        print ''
                        print 'Learn about renegging, try again!'
                        print ''
                        return playerTrick(trump, playedCards, hand, bid)
                else:
                    print ''
                    print 'You don\'t have that card!'
                    print ''
                    return playerTrick(trump, playedCards, hand, bid)
            elif trump not in leadCard:
                if len(leadCard) == 2:
                    trickTrump = leadCard[1]
                elif len(leadCard) == 3:
                    trickTrump = leadCard[2]
                if card in hand:
                    if trumpChecks.trickTrumpCheckReneg(card, hand, trickTrump, trump) == True:
                        print ''
                        print 'Player plays: ' + card
                        return card
                    else:
                        print ''
                        print 'Gotta follow off-suit, try again!'
                        print ''
                        return playerTrick(trump, playedCards, hand, bid)
                else:
                    print ''
                    print 'You don\'t have that card!'
                    print ''
                    return playerTrick(trump, playedCards, hand, bid)
def trickOrder(winner):
    if winner == 'P2':
        return ['P2', 'P3', 'P4', 'P1']
    elif winner == 'P3':
        return ['P3', 'P4', 'P1', 'P2']
    elif winner == 'P4':
        return ['P4', 'P1', 'P2', 'P3']
    elif winner == 'P1':
        return ['P1', 'P2', 'P3', 'P4']
def playTrick(winner, hand1, hand2, hand3, hand4, dHand2, dHand3, dHand4, trump, bid, trickCount, p1takes, p2takes, p3takes, p4takes, pTeamTricks, cTeamTricks, bidder):
    if bidder == 'P1':
        winString = 'You'
    elif bidder == 'P2':
        winString = 'Player 2'
    elif bidder == 'P3':
        winString = 'Your Partner'
    elif bidder == 'P4':
        winString = 'Player 4'
    suits = {'H': 'Hearts', 'D': 'Diamonds', 'S': 'Spades', 'C': 'Clubs'}
    playedCards = []
    trickOrd = trickOrder(winner)
    trickCount -= 1
    print '--------------------------------------------'
    print 'Your team\'s tricks so far: ' + str(pTeamTricks)
    print 'The other team\'s tricks so far: ' + str(cTeamTricks)
    print winString + ' ' 'bid ' + str(bid) + ' in ' + suits[trump]
    print '--------------------------------------------'
    print 'Your Cards: ' + ' '.join(hand1)
    print '--------------------------------------------'
    for i in range(len(trickOrd)):
        if trickOrd[i] == 'P1':
            card1 = playerTrick(trump, playedCards, hand1, bid)
            playedCards.append(card1)
            hand1.remove(card1)
        elif trickOrd[i] == 'P2':
            card2 = compPlayTrick.compPlayTrick(hand2, playedCards, trump, p4takes)
            print ''
            print 'Player 2 plays ' + card2
            playedCards.append(card2)
            hand2.remove(card2)
            del dHand2[card2]
        elif trickOrd[i] == 'P3':
            card3 = compPlayTrick.compPlayTrick(hand3, playedCards, trump, p1takes)
            print ''
            print 'Your Partner plays ' + card3
            playedCards.append(card3)
            hand3.remove(card3)
            del dHand3[card3]
        elif trickOrd[i] == 'P4':
            card4 = compPlayTrick.compPlayTrick(hand4, playedCards, trump, p2takes)
            print ''
            print 'Player 4 plays ' + card4
            playedCards.append(card4)
            hand4.remove(card4)
            del dHand4[card4]
    return hand1, hand2, hand3, hand4, dHand2, dHand3, dHand4, card1, card2, card3, card4, playedCards, trickCount
