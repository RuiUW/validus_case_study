import re

# dictionary to record frequency of char in a word
def char_freq(word):
    freq_dic = {}
    for char in word:
        freq_dic[char] = freq_dic.get(char, 0) + 1
    return freq_dic

def find_anagram(text):
    # split words
    word_list = text.split()
    # remove special characters
    word_list = [re.sub(r'[^a-zA-Z0-9]','',string) for string in word_list]
    # lower case
    word_list = [string.lower() for string in word_list]
    
    # initialize anagram list
    anagram_list = []
    # loop thru word_list
    for word1 in word_list: 
        for word2 in word_list: 
            if word1 != word2 and (char_freq(word1) == char_freq(word2)):
                anagram_list.append(word1)
                anagram_list = list(dict.fromkeys(anagram_list))
    print(anagram_list)
