import sys

# Complete the findDigits function below.
def findDigits(n):
    temp = n
    count = 0
    while temp > 0:
        digit = int(temp%10)
        temp = int(temp/10)
        if digit > 0 and n % digit == 0:
            count = count + 1
    return count

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(str(result) + '\n')
