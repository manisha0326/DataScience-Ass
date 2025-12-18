# 4. Ask the user to input a word and count vowels and consonants using a function.

def count_vowels_consonants(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in word:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count


word = input("Enter a word: ")

vowels, consonants = count_vowels_consonants(word)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")


'''
Output:
Enter a word:  Manisha
Vowels: 3
Consonants: 4
'''
