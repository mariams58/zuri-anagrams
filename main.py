# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    l1 = len(word)
    l2 = len(anagram)
    count = 0
    while l1==l2:
        for i in word:
            for j in anagram:
                if i == j:
                    count += 1
                    word.replace(i, "", 1)
                    anagram.replace(j,"",1)
    if count == l1:
        return True
        print(word, "and", anagram, "are anagrams.")
    
    else:
        return False

print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))