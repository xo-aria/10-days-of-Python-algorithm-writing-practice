# This reverse_string is the same as day 2.
def reverse_string(text):
    rev_text = ""
    for t in text:
        rev_text = t + rev_text
    return rev_text

def palindrome_number_and_text(num):
    if reverse_string(num) == num:
        print(num + ' is palindrome')
        # return True
    else:
        print(num + ' is not palindrome')
        # return False

print(palindrome_number_and_text("11"))
print(palindrome_number_and_text("12"))