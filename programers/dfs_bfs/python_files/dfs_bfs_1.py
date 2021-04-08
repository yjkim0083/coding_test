"""
# 타겟 넘버

## 문제 설명

n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

```
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서
타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

## 제한사항
- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

## 입출력 예

numbers	            target	return
--------------------------------
[1, 1, 1, 1, 1]	    3	    5

## 입출력 예 설명
문제에 나온 예와 같습니다.
"""

import collections


def solution(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])

    _idx = 0
    while stack:
        print(f"idx: [{_idx}]   answer: {answer},   stack:{stack}")
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum + number, num_idx + 1))
            stack.append((current_sum - number, num_idx + 1))

        _idx += 1

    return answer


print(solution([1, 2, 3], 4))

# graph = {
#     'A': ['B'],
#     'B': ['A', 'C', 'H'],
#     'C': ['B', 'D'],
#     'D': ['C', 'E', 'G'],
#     'E': ['D', 'F'],
#     'F': ['E'],
#     'G': ['D'],
#     'H': ['B', 'I', 'J', 'M'],
#     'I': ['H'],
#     'J': ['H', 'K'],
#     'K': ['J', 'L'],
#     'L': ['K'],
#     'M': ['H']
# }
#
# def bfs(graph, start_node):
#     visit = list()
#     queue = list()
#
#     queue.append(start_node)
#
#     while queue:
#         node = queue.pop(0)
#         if node not in visit:
#             visit.append(node)
#             queue.extend(graph[node])
#
#     return visit
#
# def bfs2(graph, start_node):
#     visit = {}
#     queue = list()
#
#     queue.append(start_node)
#
#     while queue:
#         node = queue.pop(0)
#         if node not in visit:
#             visit[node] = True
#             queue.extend(graph[node])
#
#     return list(visit.keys())
#
# def dfs(graph, start_node):
#     visit = list()
#     stack = list()
#
#     stack.append(start_node)
#
#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             stack.extend(graph[node])
#
#     return visit
#
# #print(bfs2(graph, 'A'))
# #print(dfs(graph, 'A'))
