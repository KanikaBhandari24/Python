PLACEHOLDER = "[name]"
with open("/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/Project23-Mail Merge/Input/Names/invited.txt") as file:
    names = file.readlines() #turns into list

with open("/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/Project23-Mail Merge/Input/Letters/starting.txt") as letter:
    content = letter.read()
    for name in names:
        stripped=name.strip()
        new=content.replace(PLACEHOLDER, stripped)
        with open(f"/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/Project23-Mail Merge/Output/ReadyToSend/LetterFor{stripped}.txt", "w") as invite:
            invite.write(new)
