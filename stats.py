def get_num_words(text):
    words = text.split()
    return len(words)

def character_frequencies(text):
    deduped = text.lower()
    character_counts = {}
    for char in deduped:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]



def sorted_frequencies(frequencies_dict):
    to_sort = []
    for char, num in frequencies_dict.items():
        character_dict = {"char": char, "num": num}
        to_sort.append(character_dict)
    to_sort.sort(reverse=True, key=sort_on)
    return to_sort