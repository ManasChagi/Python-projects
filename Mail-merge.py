with open("./Input/Letters/starting_letter.txt") as letter:
    x = letter.read()
    with open("./Input/Names/invited_names.txt") as names:
        for name in names:
            name = name.strip("\n")
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt.", "w") as new:
                new.write(x.replace("[name]", name))
              
