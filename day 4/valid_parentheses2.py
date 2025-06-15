def is_valid_parentheses(s):
    box = []
    
    for char in s:
        if char == '(':
            box.append(')')
        elif char == '{':
            box.append('}')
        elif char == '[':
            box.append(']')
        else:
            if not box or box.pop() != char:
                return False
                
    return not box
