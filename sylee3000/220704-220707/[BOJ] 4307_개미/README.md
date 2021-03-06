# [BOJ] 4307_개미

문제 링크 : https://www.acmicpc.net/problem/4307

---------------
## 문제 요약
  - 개미 여러 마리가 길이가 lcm인 막대 위에 있다. 
  - 각 개미의 이동 속도는 모두 일정하며, 1cm/s이다. 개미가 막대의 마지막까지 걸어간다면, 개미는 그 즉시 떨어지게 된다. 또, 두 개미가 만나게 된다면, 방향을 반대로 바꾸어 걸어가게 된다.
  - 가장 처음에 막대 상에서 개미의 위치를 알고 있다. 하지만, 개미가 어느 방향으로 움직이는 지는 알 수가 없다. 
  - 이때, 모든 개미가 땅으로 떨어질 때까지 가능한 시간 중 가장 빠른 시간과 느린 시간을 구하는 프로그램을 작성하시오.

## 접근 방식
  - 개미 두 마리가 만났을 때 방향을 바꾸지만, 결과적으로는 그냥 지나가는 것과 같다는 것을 알 수 있다.
  - 가장 빠른 시간은 중앙에 가장 가까운 개미가 가장자리로 바로 가는 경우, 가장 느린 시간은 가장자리에 가장 가까운 개미가 막대기 반대쪽까지 가는 경우
