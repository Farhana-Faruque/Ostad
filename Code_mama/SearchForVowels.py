def contains_vowel(s):
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            print("The string contains a vowel.")
            return
    print("The string does not contain any vowel.")

# Example usage:
input_string = input()
contains_vowel(input_string)
