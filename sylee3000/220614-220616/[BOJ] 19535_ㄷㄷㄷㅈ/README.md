# [BOJ] 19535_ㄷㄷㄷㅈ

문제 링크 : https://www.acmicpc.net/problem/19535

----------------
## 문제 요약
![image](https://user-images.githubusercontent.com/102509777/173734584-dbb39831-9688-4c84-ae64-b26b167f794f.png)
  - 노드가 네 개인 트리는 그림과 같이 ㄷ 모양과 ㅈ 모양, 총 두 종류만 존재한다.
  - N개의 노드와 N-1개의 간선이 주어질 때, 다음 규칙에 따라 출력결과를 내는 문제
    - D-트리 : ‘ㄷ’이 ‘ㅈ’의 3배보다 많은 트리, D 출력
    - G-트리 : ‘ㄷ’이 ‘ㅈ’의 3배보다 적은 트리, G 출력
    - DUDUDUNGA-트리 : ‘ㄷ’이 ‘ㅈ’의 정확히 3배만큼 있는 트리, DUDUDUNGA 출력 

## 접근 방식
  - ㄷ 모양 : 두 노드가 이어져 있고, 각각 연결된 간선이 두 개 이상
  - ㅈ 모양 : 한 노드에 세 개 이상의 간선이 연결
  - ㄷ 모양은 간선으로, ㅈ 모양은 노드로 찾는다
