n = int(input()) # 입력받을 횟수
word_list = []
for i in range(n):
    S = input()
    word_list.append((len(S), S)) # len(S), S 둘다에 대해서 정렬해주기 위해서 둘다 입력받아줌.

word_set = set(word_list) # 중복되는 애들 제거

word_list_final = list(word_set) # 다시 리스트로 받아서
word_list_final.sort() # sort()적용

for word in word_list_final:
    print(word[1]) # 튜플에 들어있는 것중 뒤에거(S) 문자열만 프린트.