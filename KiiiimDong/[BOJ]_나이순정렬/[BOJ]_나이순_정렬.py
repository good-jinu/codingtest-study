# 1. 입력받을 준비 
n = int(input()) # 회원 수 
customer_list = [] # 회원정보 담을 리스트

# 2. 회원정보 담기
for i in range(n):
    a, b = input().split()
    customer_list.append([int(a), b, i]) # 회원나이, 이름, 등록순서 기록

# 3. 회원정보 정렬
customer_list.sort(lambda x:[x[0], x[2]]) # 회원나이와 등록순서를 기준으로 정렬

# 4. 회원정보 출력(나이, 이름)
for customer in customer_list:
    print(customer[0], customer[1]) # 나이, 이름