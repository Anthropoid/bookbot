character_count = {}
character_count_list = []
word_list = []

def main():

    # Make a dictionary of each character in a text file and the number of occurences of that character
    create_character_count()

    # Convert character count dictionary to a list of dictionaries-- one character and its count per dictionary
    for k in character_count:
        character_count_list.append({"Character": k,"Count": character_count[k]})

    #Sort the character count list (of dictionaries) in descending order
    character_count_list.sort(reverse=True, key=sort_on)

    print(f"Ya got {word_count} words in this heckin' book.")
    print("Here's your heckin' sorted alphabetical character count:")
    for item in character_count_list:
        if item["Character"].isalpha():
            print(f"The '{item["Character"]}' character was found {item["Count"]} times")


def create_character_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    lowercase = file_contents.lower()
    for character in lowercase:
        if character not in character_count:
            character_count[character] = 1
        else: character_count[character] += 1
    return character_count

def sort_on(dict):
    return dict["Count"]

def get_word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count

word_count = get_word_count()

main()