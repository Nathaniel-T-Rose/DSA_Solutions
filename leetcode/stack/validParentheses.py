def isValid(self, s: str) -> bool:
    close_open={'}':'{',']':'[',')':'('}
    stack=[]
    for char in s:
        if char in ')}]':
            if stack == [] or stack.pop()!=close_open[char]:
                return False
        else:
            stack.append(char)
    return stack==[]