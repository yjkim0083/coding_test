from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0

        for idx, height in enumerate(heights):
            if stack == []: # stack에 없으면
                stack.append([idx, height])
            else:
                width = idx  # 현재 값의 idx 저장
                while stack != [] and stack[-1][1] > height:    # top 값이 height 보다 클 시
                    value = stack.pop()
                    width = value[0]    # 마지막 pop한 히스토그램 idx 갱신
                    size = value[1] * (idx - value[0])  # 넓이 구하기
                    if result < size:   # 최댓값 갱신
                        result = size
                stack.append([width, height])

        for value in stack:     # 스택에 남은 애들 계산
            size = value[1] * (len(heights) - value[0]) # 기준은 길이 N으로
            if result < size:
                result = size
        return result





s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))