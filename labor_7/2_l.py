def get_word_set(word):
    return set(filter(lambda c: c.isupper() and c.isalpha(), word))

def main():
    # Define selected words
    words = ["Hello", "World", "Python"]

    # Get sets of uppercase letters for each word
    sets = [get_word_set(word) for word in words]

    # Find union of all sets
    union_set = set().union(*sets)

    # Print results
    print("Sets of uppercase letters for each word:", sets)
    print("Union of all sets:", union_set)

if __name__ == '__main__':
    main()