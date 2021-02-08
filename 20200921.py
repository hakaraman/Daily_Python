def justify_text(words, k):
    result = []
    line = []
    i = 0
    while i < len(words):
        while len(" ".join(line))+len(words[i]) <= k:
            line.append(words[i])
            i += 1
            if i == len(words):
                break
        result.append(line)
        line = []
    for i, item in enumerate(result):
        j=0
        while len(" ".join(item)) < k:
            item[j] += " "
            j += 1
            if j >= len(item)-1:
                j = 0
        result[i] = " ".join(item)
    return result

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog","1234567890"] 
k = 16
for i in justify_text(words, k):
    print(f"\'{i}\'")