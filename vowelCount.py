def input_word():
    word = "1"
    while not word.isalpha():
        word = input("Enter a word (that contains only letters):")
        if not word.isalpha():
            print("Word should contain only letters.")
    word =word.lower()
    return word

def count_vowel(word):
    vowel = 0 
    for character in word:
        if character in "aeiou":
            vowel = vowel + 1
    return vowel

word_1 = input_word()
vowel1 = count_vowel(word)
if vowel1 == 0:
    print("There are no vowels in the word.")
elif vowel1 == 1:
    print("There is one vowel in the word.")
else:
    print("There are",vowel1,"vowels in the word.")
