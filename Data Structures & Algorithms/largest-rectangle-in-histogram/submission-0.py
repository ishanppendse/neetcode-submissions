class Stack:
    def __init__(self):
        self.s = []
    
    def push(self, elem):
        self.s.append(elem)
    
    def pop(self):
        return self.s.pop()
    
    def peek(self):
        if len(self.s) == 0:
            return None
        return self.s[-1]

def get_minstack(heights):
    minstack = [len(heights) for _ in range(len(heights))]
    stack = Stack()
    for i, height in enumerate(heights):
        while stack.peek() is not None:
            top_height, top_i = stack.peek()
            if height < top_height:
                stack.pop()
                minstack[top_i] = i
            else:
                break
        stack.push((height, i))
    return minstack


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        minstack = get_minstack(heights)
        minstack_reverse = get_minstack(heights[::-1])[::-1]
        minstack_reverse = [len(minstack_reverse)-i-1 for i in minstack_reverse]
        # print(minstack)
        # print(minstack_reverse)
        area = 0
        for i, height in enumerate(heights):
            # print(f"i is {i} and area is {height*(minstack[i]-i)}")
            area = max(area, height*((minstack[i]-i) + (i-minstack_reverse[i]-1)))
        return area
        