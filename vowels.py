vowels = ['o','e','z']
found=[]
word = input('Provide a word to search for all letters:')
for letter in word:
    if letter in vowels:
       if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

