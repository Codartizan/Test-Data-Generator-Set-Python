from random import Random

f = file('Card_NBR.txt')
lines = f.read()
f.close()
# print lines


def generateARN():

    def calculateCheckDigit(n):
        mult = 1
        s = 0
        for d in str(n)[::-1]:
            if mult == 1:
                x = int(d)*2
                if x < 9:
                    s += x
                else:
                    for c in str(x):
                        s += int(c)
            else:
                s += int(d)
            mult = mult * -1
        s = s * 9
        check_digit = str(s)[-1]
        return check_digit

    def random_str(random_length=11):
        str = ''
        chars = '0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(random_length):
            str += chars[random.randint(0, length)]
        return str

    xbin = 446666
    julian_date = 5187
    sequence_nbr = random_str()
    digit_nbr = calculateCheckDigit("7%s%s%s" % (xbin, julian_date, sequence_nbr))
    arn_nbr = "7%s%s%s%s" % (xbin, julian_date, sequence_nbr, digit_nbr)

    return arn_nbr

arn = generateARN()
# print arn

print lines, ',', arn
'''
def generateARN(len):
    len = input()
    count = 0
    xbin = 446666
    julian_Date = 5187
    sequence_Nbr = random_str()
    digit_Nbr = calculateCheckDigit("7%s%s%s" % (xbin, julian_Date, sequence_Nbr))
    arn = "7%s%s%s%s" % (xbin, julian_Date, sequence_Nbr, digit_Nbr)
    while (count < len):
        print (arn)
        count = count + 1

    return generateARN
'''

'''
def generateARN(len):
    len = input()
    count = 0
    while (count < len):
        print (arn)
        count  = count +1

    return generateARN

results = generateARN(len)

print results
'''

'''
pch_date = input()
destnAmt = 000000000020
destnCurr = 036
srcAmt = 000000000020
srcCurr = 036
authCode = 000000
cntrlProcDte = 'YDDD'
visaIssBINfromBanks = 000000
'''