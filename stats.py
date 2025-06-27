def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def sorted_count(characters):
    sorted = []
    for c in characters:
        sorted.append({"char": c, "num": characters[c]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
    
# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]