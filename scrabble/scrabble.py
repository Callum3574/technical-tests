import random
import collections

# with open ('dictionary.txt') as f:
#     contents = f.read()

alphabet = {
    'a':1,
    'e':1,
    'i':1,
    'o':1,
    'u':1,
    'l':1,
    'n':1,
    'r':1,
    's':1,
    't':1,
    'd':2,
    'g':2,
    'b':3,
    'c':3,
    'm':3,
    'p':3,
    'f':4,
    'h':4,
    'v':4,
    'w':4,
    'y':4,
    'k':5,
    'j':8,
    'x':8,
    'q':10,
    'z':10
}

bag = ['E','E','E','E','E','E','E','E','E','E','E','E','A','I','A','I','A','I','A','I','A','I','A','I','A','I','A','I','A','I','O','O','O','O','O','O','O','O', 'N','R', 'T', 'N','R', 'T','N','R', 'T','N','R', 'T','N','R', 'T','N','R', 'T', 'L', 'S', 'U', 'D', 'L', 'S', 'U', 'D', 'L', 'S', 'U', 'D', 'L', 'S', 'U', 'D', 'G', 'G','G', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W','Y', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W','Y', 'K', 'J', 'X', 'Q', 'Z']

#shuffle bag so it's random every
random.shuffle(bag)
print(bag)


#function to get value of words
def value_of_words(alphabet, word):
    points = 0
    for i in range(len(word)):
        for [key, value] in alphabet.items():
            if key == word[i]:
                points += value
    return points


#select items out of bag * 7 and returns a bag of tiles
def return_7_tiles(bag):
    player_bag = []
    for i in range(7):
        player_bag.append(bag.pop())
    return player_bag

tiles = return_7_tiles(bag)
tiles_in_string = ''.join(tiles).lower()

#score for this set of tiles
score = value_of_words(alphabet, tiles_in_string)
print(score)

#compare given tiles to words in dict - aim here is to have a counter of each letter that the player has. If this amount of is present in a word in dict, return the word. 
#I've found a collections import, creates dictionary with each char and amount of times it's present

#this returns a dict of all the char as keys, and value of how many times present. ----> The aim here is to compare this to each word in the dict
letters = collections.Counter(tiles_in_string)


#need to loop through the dict and make a collection dict
#this loops through line of text file and return the word as a dict similar to letters above... 
for line in open('dictionary.txt'):
    dict_words = collections.Counter(line)




#compare letters to dict

