
def maxPalindrome(n):

    #Get Maximum and Minimun in n digit
    maxDigit_Number = (10 ** (n)) - 1
    minDigit_Number = (10 ** (n-1))

    max_Pali = 0
    for i in range(maxDigit_Number, minDigit_Number - 1, -1):
        for j in range(maxDigit_Number, minDigit_Number - 1, -1):
            #Checking multiple number to get the biggest Palindrom
            if (i * j < max_Pali):
                break
            number = i * j
            reverse = 0

            #Reverse the number
            while (number != 0):
                reverse = reverse * 10 + number % 10
                number = number // 10

            #Checking if the number the same as the reverse number is true and get the biggest number
            if (i * j == reverse and i * j > max_Pali):
                max_Pali = i * j

    return max_Pali

if __name__ == '__main__':
    n = 3
    print(maxPalindrome(n))
