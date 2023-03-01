def get_vowels_set(text):
    vowels = set('aeiouAEIOU')
    return set(filter(lambda c: c in vowels, text))

def main():
    # Get input strings from user
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

    # Get vowel sets for each string
    s1 = get_vowels_set(text1)
    s2 = get_vowels_set(text2)

    # Find difference between sets
    s2_minus_s1 = s2 - s1
    s1_minus_s2 = s1 - s2

    # Print results
    print("Vowels in text 1:", s1)
    print("Vowels in text 2:", s2)
    print("Vowels in text 2 but not in text 1:", s2_minus_s1)
    print("Vowels in text 1 but not in text 2:", s1_minus_s2)

if __name__ == '__main__':
    main()