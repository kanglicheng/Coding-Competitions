```
Refrigerator Letters
Time limit: 2500 ms
Memory limit: 128 MB

You have NN refrigerator magnets, each representing a letter. You want to write the word SS, but you might need to buy some more letters.

Find the minimum number of new magnets you need to buy.

Standard input
The first line contains a single integer NN.

The second line contains NN letters, representing the magnets you already have.

The third line contains the word SS.

Standard output
Print the number of magnets you need to buy on the first line.

Constraints and notes
1 \leq N \leq 1001≤N≤100 
The length of SS is between 11 and 100100 
All the input characters are lowercase letters of the English alphabet
Input	Output	Explanation
6
a b c d e f
aabfe
1
Buying a a magnet will be enough to write aabfe, leaving a d magnet unused.

6
q w e r t y
asdfg
5
None of the 66 letter magnets can be used to write asdfg so you'll need to buy all 55 magnets.
```
def refrigeratorLetters( letters, word):
    d={}
    buy =0
    for l in letters:
        d[l]=1 if l not in d else d[l]+1

    for c in word:
        if c in d and d[c]>0:
            d[c] -=1
        else:
            buy +=1 
    return buy

print refrigeratorLetters(['a', 'b', 'c', 'd', 'e', 'f'], "aabfe")
