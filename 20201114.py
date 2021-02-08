def plusOne1(digits):
    return [int(i) for i in str(int("".join([str(i) for i in digits]))+1)]

def plusOne2(digits):
    s = "".join([str(i) for i in digits])
    leftzeros = len(s) - len(str(int(s)))
    return [0]*leftzeros + [int(i) for i in str(int(s)+1)]

def plusOne(digits):
    if digits[-1] != 9:
        digits[-1] += 1
    else:
        i=-1
        while -i <= len(digits) and (digits[i] == 9):
            digits[i] = 0
            i -= 1
        if i+1 == -len(digits):
            digits = [1] + digits
        else:
            digits[i] += 1
    return digits

lst = [9,9]
print(plusOne1(lst))