# BFS(Breadth First Search)



- 시작점의 인접한 정점들을 먼저 모두 방문한 후에
  방문한 정점을 시작점으로하여
  다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선 탐색을 진행하므로,
  선입선출형태의 자료구조인 큐(Queue)를 활용

```python
def BFS(G, v):  # 그래프 G, 탐색시작점 v.
    visited = [0]*n  # n: 정점의 개수
    queue = []  # 큐 생성
    queue.append(v)  # 시작점 v를 큐에 삽입.
    while queue:
        t = queue.pop(0)  # 큐의 첫번째 원소 반환
        if not visited[t]:  # 방문하지않은 곳이라면
            visited[t] = True
            visit(t)
        for i in G[t] :  # t와 연결된 모든 선에 대해서
            if not visited[i]:
                queue.append(i)
```

- 초기상태: visited array 초기화, Q생성, 시작점 enqueue
- dequeue(start). visited[start] = true, start 접점 enqueue



visited라는 list에 시작점으로부터 거리를 저장하려면?

```python
def BFS(G,v):
    visited =[0]* n
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1  # 이렇게 작성할 경우 시작점, 연결되지않은 점 외에는 시작점으로부터 거리로 저장됨.
```









```
슈도코드 구현할 때 queue =[v]가 아니라 빈 리스트를 선언하고 queue.append(v) 하는 이유가 있을까???
- python 뿐만 아니라 다른 언어에서도 활용가능한 basic
```

![image-20210303171012749](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210303171012749.png)