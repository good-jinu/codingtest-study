MOD = 1000000000
n = int(input())
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(n+1)]

# 길이가 1인 경우 0을 제외한 모든 수에 개수 1을 더함
for k in range(1, 10):
    dp[1][k][1 << k] = 1

for length in range(n):
    for last in range(10):
        for bit in range(1024):
            # 마지막 수가 9보다 작을 경우 1을 더한 숫자의 비트맵에 값을 더한다.
            if last < 9:
                next_bit = bit | (1 << (last + 1))
                dp[(length + 1)][last + 1][next_bit] += dp[length][last][bit]
                dp[(length + 1)][last + 1][next_bit] %= MOD
            
            # 마지막 수가 0보다 클 경우 1을 뺀 숫자의 비트맵에 값을 더한다.
            if last > 0:
                next_bit = bit | (1 << (last - 1))
                dp[(length + 1)][last - 1][next_bit] += dp[length][last][bit]
                dp[(length + 1)][last - 1][next_bit] %= MOD

answer = 0
for last in range(10):
    # 길이가 n인 0~9까지의 숫자가 모두 포함된 테이블 위치의 값을 모두 더한다.
    answer += dp[n][last][1023]
    answer %= MOD

print(answer)