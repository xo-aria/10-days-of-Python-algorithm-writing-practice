def reverse_string(text):
    rev_text = ""
    for t in text:
        rev_text = t + rev_text
    return rev_text

print(reverse_string("Hello Darling!"))