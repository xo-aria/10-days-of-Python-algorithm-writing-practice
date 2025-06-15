def valid_parentheses(text):
    box = []
    parents = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for char in text:
        if char in ['(', '[', '{']:
            box.append(char)
        else:
            if not box:
                return False
            
            last_open = box.pop()

            if parents[char] != last_open:
                return False
            
    return len(box) == 0

print(valid_parentheses('({})'))
print(valid_parentheses('({[})'))