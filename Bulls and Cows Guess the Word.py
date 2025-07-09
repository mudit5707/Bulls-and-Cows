#the guessing part
import time
F = open("Word.txt","r")
W = F.readline()
L = len(W)
print("Bulls and Cows")
time.sleep(1)
print("Guess the",L,"lettered word")
time.sleep(1)
print("If you get a bull, one of the letters is correct AND in correct place")
print("If you get a cow, one of the letters is correct, but in incorrect place")
time.sleep(3)
print("Beware, that neither the word nor your guesses contain a word with double letters")
time.sleep(1)
print("Let's play Bulls and Cows...you have 10 guesses. Let's go!")
print()
time.sleep(1)
for i in range(10):
    print("Guess ",(i+1),":",sep="")
    G = input().lower()
    C,B = 0,0
    for j in range(L):
        if G[j] in W:
            if G[j] == W[j]:
                B+=1
            else:
                C+=1
    if B == L:
        print("Congratulations! You have guessed the word!")
        print(W)
        break
    print(C,"Cows and",B,"Bulls")
    print()
else:
    print("You have exhausted your guesses")
    print("The word was",W)
