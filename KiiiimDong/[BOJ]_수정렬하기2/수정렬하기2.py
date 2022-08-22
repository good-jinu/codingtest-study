n = int(input())
number_list = []
for i in range(n):
    number_list.append(int(input()))

number_list = list(set(number_list))
answer_list = sorted(number_list)

for i in range(len(answer_list)):
    print(answer_list[i])