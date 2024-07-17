import pandas

data=pandas.read_csv("/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/Project-25 Nato Alphabet Project/alphabet.csv")
# print(data)

#1. Create a dictionary in this format:
new={row.letter: row.code for (index, row) in data.iterrows()}
# print(new)

#2. Create a list of the phonetic code words from a word that the user inputs.
word=input("Enter a word: ").upper()
dict={new[letter] for letter in word}
print(dict)