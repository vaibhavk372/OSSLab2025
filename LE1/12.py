#12. Write a python script to make word guessing game. The game runs as follows:

def guess_game():
    attempt=0
    j=0
    count=0
    word=input("Enter a word of challenge:")
    list=[None]*len(word)
    while attempt<=len(word):
        print("Guess the word:")
        print("The word is",end=' ')
        k=0
        for i in range(0,len(word)):
                if i==list[k] and attempt>0:
                    print(word[i],end='')
                    k=k+1
                else:
                    print("*",end='')
                    k=k+1
        print(" its length is ",len(word))
        print("You have ",len(word)-attempt," attemps left")
        if attempt<len(word):
            char=input("Enter a character(lowercase):")
        while len(char)>1:
            print("Try again:")
            char=input("Enter a character(lowercase):")
        for i in range (0,len(word)):
            if word[i]==char:
                list[i]=i
        attempt=attempt+1
    final=input("Enter the word according to you:")
    if len(word)==len(final):
        for i in range (0,len(final)):
            if word[i]==final[i]:
                count=count+1
    if count==len(final):
        print("Correct!!")
    else:
        print("wrong answer!")
guess_game()
