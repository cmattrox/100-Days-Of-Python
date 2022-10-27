import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {}

for (index, row) in data.iterrows():
    nato_dict[row.letter] = row.code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
word = word.upper()

word_list = [nato_dict[letter] for letter in word]

print(word_list)