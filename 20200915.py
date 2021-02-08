"""
This is an interview question asked by by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

def find_sentence(s, dictionary):
    starts = {0: ''}
    for i in range(len(s) + 1):
        new_starts = starts.copy()
        for start_index, _ in starts.items():
            word = s[start_index:i]
            if word in dictionary:
                new_starts[i] = word
        starts = new_starts.copy()

    result = []
    current_length = len(s)
    if current_length not in starts:
        return None
    while current_length > 0:
        word = starts[current_length]
        current_length -= len(word)
        result.append(word)

    return list(reversed(result))

### recursive solution
def find_sentence1(dictionary, s):
    sentence, valid = find_sentence_helper(dictionary, s)
    if valid:
        return sentence

def find_sentence_helper(dictionary, s):
    if len(s) == 0:
        return [], True
    for i in range(len(s) + 1):
        prefix, suffix = s[:i], s[i:]
        if prefix in dictionary:
            rest, valid = find_sentence_helper(dictionary, suffix)
            if valid:
                return [prefix] + rest, True
    return [], False

#baris
def find_words(s, lst):
    words = {0: ''}
    for i in range(len(s)+1):
        for j in list(words.keys()):
            if s[j:i] in lst:
                words[i] = s[j:i]                
    k = len(s)
    if k not in words.keys():
        return None  
    result = []
    while k > 0:
        result.append(words[k])
        k -= len(result[-1])
    return result[::-1]


words = ['quick' , 'brown', 'the', 'fox', 'theremin']

B = "thereminquickbrownfox"
print(find_sentence(B, words))
print(find_words(B, words))