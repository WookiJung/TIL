# 2차원 array에서 BFS, DFS활용

## 예제 1 - DFS

ex) N x M 크기의 배열이 주어졌을 때 연속된 1의 개수는 몇개인지 세어보기. DFS를 이용해서.



N = 7, M=7
0000011
0000000
0011100
0010111
0110010
0011100
0000000
이 주어졌을 때

```python
direction = [[1, 0], [0,1], [-1,0], [0,-1]]
def DFS(r,c):
    global cnt
    # 해당 arr[r][c] 자리값이 1이므로 방문했다는 흔적을 남기고 카운트를 1증가.
    arr[r][c] = 0
    cnt += 1
    
    for i in range(4):
        dr = r+ direction[i][0]
        dc = c + direction[i][1]
        
        if 0<= dr < N and 0<= dc < N:
            if arr[dr][dc]:
                DFS(dr,dc)
                


N, M = int(input().split())
arr = [list(map(int, input().split())) for _ range(N)]  # 행의 길이만큼 반복

for i in range(N):
    for j in range(M):
        if arr[i][j] ==1:
            cnt = 0
            DFS(i,j)
            print(cnt)
```



백준-단지번호붙이기 정답맞은거 검사맡기. 토마토도.

## 예제 2. BFS

토마토 문제 BFS. Q를 array로풀기