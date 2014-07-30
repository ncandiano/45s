from playing import *
import os
def playGame():
    playerScore = 0
    opponentScore = 0
    dealers = ['P1', 'P2', 'P3', 'P4']
    x = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    print 'Welcome to the Confounding Game of 45s!'
    print ''
    print 'The game ends at 120 points!'
    print ''
    print 'Let\'s Go!'
    while playerScore < 120 and opponentScore < 120:
        t1Score, t2Score, bidder, bidSet = playHand.playHand(dealers[x], playerScore, opponentScore)
        playerScore += t1Score
        opponentScore += t2Score
        x += 1
        if x == 4:
            x = 0
    else:
        if playerScore >= 120 and opponentScore < 120:
            print 'You Won! Final score: ' + str(playerScore) + ' You! ' + str(opponentScore) + ' Them!'
            print ''
        elif opponentScore >= 120 and playerScore < 120:
            print 'You Lost! Final score: ' + str(playerScore) + ' You! ' + str(opponentScore) + ' Them!'
            print ''
        else:
            if bidder == 'Team 1' and bidSet == 'Made':
                print 'Bidder went out!'
                print ''
                print 'You won! Final score: ' + str(playerScore) + ' You! ' + str(opponentScore) + ' Them!'
                print ''
            elif bidder == 'Team 2' and bidSet == 'Made':
                print 'Bidder went out!'
                print ''
                print 'You Lost! Final score: ' + str(playerScore) + ' You! ' + str(opponentScore) + ' Them!'
                print ''
                print '--------------------------------------------'
                print ''
    a = raw_input('Would you like to play again?').upper()
    if a == 'Y':
        return playGame()
    else:
        print 'Thanks for playing!'
if __name__=="__main__":
    playGame()
