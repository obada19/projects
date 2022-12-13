m = 1
gray_code = ['0', '1']

def getGrayCode(n):
    global m

    while (m < n):
        m += 1
        reversed_code = sorted(gray_code, reverse=True)
        for i in range(len(gray_code)):
            gray_code[i] = '0' + gray_code[i]
        for i in range(len(gray_code)):
            reversed_code[i] = '1' + reversed_code[i]
        for j in range(len(reversed_code)):
            gray_code.append(reversed_code[j])

    return print(gray_code)


getGrayCode(3)