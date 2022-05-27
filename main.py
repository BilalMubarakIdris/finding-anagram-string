# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(len(word) == len(anagram)):
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)
        
        if(sorted_word == sorted_anagram):
            print("Both words are anagram")
        else:
            print("Both words are not anagram")
    else:
        print(word + " and " + anagram + " are not equal in lenght so theay can't be anagram")

str1 = input("Please enter word1: ")
str2 = input("Please enter word2: ")
# printing spaces
print()
word = str1.lower();
anagram = str2.lower();

find_anagram(word, anagram)