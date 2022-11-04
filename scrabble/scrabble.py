import random


with open ('dictionary.txt') as f:
    contents = f.read()

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


