45s
===

Trump card game/first python game project. Command line based

This is a team game, alternating players are on a team. In this game, player is automatically player 1, player 3 is the partner.
5 cards are dealt to each player, and 3 to a 'Kitty'
In any hand, each of the 5 "tricks" is worth 5 points, except the high card trick is worth 10.
First player after the dealer bids, bids can be 15, 20, 25, 30, or pass.
If everyone passes to the dealer, the dealer must go 15.
Once the bidder calls suit, they get the kitty.
Game offers the option of manually dumping cards, or using the auto-trim.
Cards are dealt back out to 5 each.

In suit card order applies only to trump suit.
Card order for in suit is:
5, J, Ace of Hearts, Ace of Suit, K, Q <--In ALL suits.
2 is higher than 10 in black 
10 is higher than 2 in red.
Card order for non-trump is:
K, Q, J <--- In ALL suits
2 is higher than 10 in black
10 is higher than 2 in red. (Ace of diamonds is lowest off-suit card.

Renegging:
If the 5 is thrown in Trump Suit, trump must follow if in hand. (Ace of Hearts is treated as trump.
If the Jack is lead in Trump Suit, trump must follow, but the 5 may be withheld.
if the Ace of Hearts is lead in Trump Suit, trump must follow, but the 5 or Jack may be withheld.
If any other trump is lead, trump must follow, but the 5, Jack, or Ace of Hearts may be withheld.
If off-suit is lead, player must follow off-suit if in hand.

If a team misses their bid, they are penalized the whole amount of their bid.
Game ends at 120 points. If both teams cross 120 at the same time, then the bidding team wins.
