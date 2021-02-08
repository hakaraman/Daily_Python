"""
This is an interview question asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""
def encode1(s):
    prevchar = s[0]
    result = ""
    count = 1
    for i in range(1,len(s)):
        if s[i] != prevchar:
            result += str(count)+prevchar
            count = 0
            prevchar = s[i]
        count += 1
    result += str(count)+prevchar
    return result

def encode2(s):
    result = s[0]
    count = 1
    for i in range(1,len(s)):
        if s[i] != result[-1]:
            result = result[:-1]+str(count)+result[-1]+s[i]
            count = 1
        else:
            count += 1
    result = result[:-1]+str(count)+result[-1]
    return result

def encode(s):
    chars = [s[0]]
    numbers = [0]

    for item in s:
        if item != chars[-1]:
            chars.append(item)
            numbers.append(1)
        else:
            numbers[-1] += 1

    return "".join([str(i)+j for i,j in zip(numbers,chars)])

def decode(s):
    result = ""
    count = 0
    for i in s:
        if i.isdigit():
            count = count*10 + int(i)
        else:
            result += count * i
            count = 0
    return result

def encoding_decoding(text):
    text_1 = text + "**"
    if text.isalpha():
        decoded = []
        count = 1
        i = 0
        while i < len(text):
            
            if text_1[i] == text_1[i+1]:
                count += 1
            else:
                decoded.append(count)
                decoded.append(text[i])
                count = 1
            i += 1
        return "".join([str(i) for i in decoded])
    elif text[0].isdigit():
        encoded = []
        for i in range(0, len(text), 2):
            encoded.append(int(text[i])*text[i+1])
        return "".join([str(i) for i in encoded])

s = "XAAAABBBCCDAAAAAAAAA"
encoded = encode(s)
if encoded == encode2(s):
    print("encoded eşit")
print(1, encoded)
print(2, encode1(s))
print(3, encoding_decoding(s))
decoded = decode(encoded)
if s == decoded:
    print("eşitler")
print(decoded)
print(encoding_decoding(encoded))
