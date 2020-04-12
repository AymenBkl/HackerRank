wincard = input()
rounds = int(input())
player1,player2 = 0,0
for r in range(rounds):
    plays = input().split(" ")
    if plays[0] == wincard :
        player1 = 13
    else :
        player1 = 0
    if plays[2] == wincard :
        player2 = 13
    else:
        player2 = 0
    if player1 + int(plays[1]) > player2 + int(plays[3]):
        print("Player 1 wins")
    elif player1 + int(plays[1]) < player2 + int(plays[3]):
        print("Player 2 wins")
    else :
        print("Draw")