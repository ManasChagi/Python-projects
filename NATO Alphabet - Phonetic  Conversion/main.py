import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
print("Welcome to Alphabet - Phonetic conversion")

phonetic_dict = { row.letter : row.code for (index, row) in df.iterrows()}
user_input = input("Enter a word: ").upper()
list1 = [*user_input]
# Method- 1
# new =[]
# for each in list1:
#     for (index,row) in df.iterrows():
#         if each == row.letter:
#             new.append(row.code)
# print(new)

# Method-2
output_list = [phonetic_dict[letter] for letter in list1]
print(output_list)
