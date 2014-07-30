from dealing import *
from bidding import *
from playing import playTricks
import os
def playHand(dealer, playerScore, opponentScore):
    player1Winners = {}
    player2Winners = {}
    player3Winners = {}
    player4Winners = {}
    winComp = {}
    t1Score = 0
    t2Score = 0
    trickCount = 5
    pTeamTricks = 0
    cTeamTricks = 0
    hand1, hand2, hand3, hand4, hands, kitty, usedDeck = dealing.dealHand(4)
    winner, trump, bid = bidding.bidRound(dealer, hand1, hand2, hand3, hand4, playerScore, opponentScore)
    hand1, hand2, hand3, hand4, dHand2, dHand3, dHand4, p1takes, p2takes, p3takes, p4takes = dealing.modHands(winner, kitty, hand1, hand2, hand3, hand4, trump, usedDeck)
    bidder = winner
    os.system('cls' if os.name == 'nt' else 'clear')
    print '--------------------------------------------'
    print 'Dealer says: '
    print 'You took ' + str(p1takes)+ ' cards.'
    print 'Player 2 took ' + str(p2takes)+ ' cards.'
    print 'Your Partner took ' + str(p3takes)+ ' cards.'
    print 'Player 4 took ' + str(p4takes)+ ' cards.'
    print '--------------------------------------------'
    while trickCount > 0:
        hand1, hand2, hand3, hand4, dHand2, dHand3, dHand4, card1, card2, card3, card4, playedCards, trickCount = playTricks.playTrick(winner, hand1, hand2, hand3, hand4, dHand2, dHand3, dHand4, trump, bid, trickCount, p1takes, p2takes, p3takes, p4takes, pTeamTricks, cTeamTricks, bidder)
        winVal, winner, winCard = trumpChecks.scoreTrick(playedCards, card1, card2, card3, card4, trump)
        if winner == 'P1':
            winString = 'You'
            pTeamTricks += 1
        elif winner == 'P2':
            winString = 'Player 2'
            cTeamTricks += 1
        elif winner == 'P3':
            winString = 'Your Partner'
            pTeamTricks += 1
        elif winner == 'P4':
            winString = 'Player 4'
            cTeamTricks += 1
        print ''
        print '--------------------------------------------'
        if winner == 'P2' or winner == 'P3' or winner == 'P4':
            print winString + ' ' + 'wins the trick with the ' + winCard
        else:
            print winString + ' ' + 'win the trick with the ' + winCard
        print '--------------------------------------------'
        print ''
        if winner == 'P1':
            player1Winners.update(winVal)
        if winner == 'P2':
            player2Winners.update(winVal)
        if winner == 'P3':
            player3Winners.update(winVal)
        if winner == 'P4':
            player4Winners.update(winVal)
    else:
        if len(player1Winners) > 0:
            for key in player1Winners:
                t1Score += 5
                if player1Winners[key] == min(player1Winners.itervalues()):
                    p1Best = {key: player1Winners[key]}
                    winComp.update(p1Best)
        else:
            player1Winners = {}
            p1Best = {}
        if len(player2Winners) > 0:
            for key in player2Winners:
                t2Score += 5
                if player2Winners[key] == min(player2Winners.itervalues()):
                    p2Best = {key: player2Winners[key]}
                    winComp.update(p2Best)
        else:
            player2Winners = {}
            p2Best = {}
        if len(player3Winners) > 0:
            for key in player3Winners:
                t1Score += 5
                if player3Winners[key] == min(player3Winners.itervalues()):
                    p3Best = {key: player3Winners[key]}
                    winComp.update(p3Best)
        else:
            player3Winners = {}
            p3Best = {}
        if len(player4Winners) > 0:
            for key in player4Winners:
                t2Score += 5
                if player4Winners[key] == min(player4Winners.itervalues()):
                    p4Best = {key: player4Winners[key]}
                    winComp.update(p4Best)
        else:
            player4Winners = {}
            p4Best = {}
        for key in winComp:
            if winComp[key] == min(winComp.itervalues()):
                if key in p1Best.keys() or key in p3Best.keys():
                    t1Score += 5
                elif key in p2Best.keys() or key in p4Best.keys():
                    t2Score += 5
        if bidder == 'P1' or bidder == 'P3':
            bidder = 'Team 1'
            if t1Score < bid:
                t1Score = (bid*-1)
                bidSet = 'Set'
                print '--------------------------------------------'
                print 'Team 1 was set! ' + str(t1Score) + ' points awarded.'
                print ''
                print 'Team 2 scored ' + str(t2Score) + ' points.'
                print '--------------------------------------------'
                print ''
                try:
                    raw_input("Press enter to continue")
                except SyntaxError:
                    pass
            else:
                bidSet = 'Made'
                print '--------------------------------------------'
                print 'Team 1 made their bid! ' + str(t1Score) + ' points awarded.'
                print ''
                print 'Team 2 scored ' + str(t2Score) + ' points.'
                print '--------------------------------------------'
                print ''
                try:
                    raw_input("Press enter to continue")
                except SyntaxError:
                    pass
        else:
            bidder = 'Team 2'
            if t2Score < bid:
                bidSet = 'Set'
                t2Score = (bid*-1)
                print '--------------------------------------------'
                print 'Team 2 was set! ' + str(t2Score) + ' points awarded.'
                print ''
                print 'Team 1 scored ' + str(t1Score) + ' points.'
                print '--------------------------------------------'
                print ''
                try:
                    raw_input("Press enter to continue")
                except SyntaxError:
                    pass
            else:
                bidSet = 'Made'
                print '--------------------------------------------'
                print 'Team 2 made their bid! ' + str(t2Score) + ' points awarded.'
                print ''
                print 'Team 1 scored ' + str(t1Score) + ' points.'
                print '--------------------------------------------'
                print ''
                try:
                    raw_input("Press enter to continue")
                except SyntaxError:
                    pass
        return t1Score, t2Score, bidder, bidSet
