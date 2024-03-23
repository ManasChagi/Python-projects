import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
print("Welcome to Alphabet - Phonetic conversion")
phonetic_dict = { row.letter : row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    try:
        user_input = input("Enter a word: ").upper()
        list1 = [*user_input]
        output_list = [phonetic_dict[letter] for letter in list1]
    except KeyError:
        print("Sorry only letters in the word please.")
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()

# Method- 1
# new =[]
# for each in list1:
#     for (index,row) in df.iterrows():
#         if each == row.letter:
#             new.append(row.code)
# print(new)

# Method-2
# output_list = [phonetic_dict[letter] for letter in list1]
# print(output_list)
