def anagram(s1,s2):
    s1 = s1.replace(" ",'').lower()
    s2 = s2.replace(" ",'').lower()

    if len(s1) != len(s2):
        return "It's not an Anagram!"

    word_count = {}

    for letter in s1:
        if letter in word_count:
            word_count[letter] += 1
        else:
            word_count[letter] = 1
    
    print(word_count)

    for letter in s2:
        if letter in word_count:
            word_count[letter] -= 1
        else:
            word_count[letter] = 1
    
    print(word_count)

    for i in word_count:
        if word_count[i] != 0:
            return "It's not an Anagram!"
    
    return "Hurray! It's an Anagram."

if __name__ == "__main__":
    string1 = input("Enter the 1st string: ")
    string2 = input("Enter the 2nd string: ")


    print(anagram(string1,string2))