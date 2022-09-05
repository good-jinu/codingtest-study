import math

T = int(input())
for i in range(T):
    message_list = input()
    n = int(math.sqrt(len(message_list)))
    message = ''
    for j in range(n-1, -1, -1):
        for index in range(0, len(message_list), n):
            unit_word = message_list[index : index+n]
            message += unit_word[j]

    print(message)