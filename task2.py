from collections import deque

def is_palindrome(text: str) -> bool:
    d = deque(text)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True

print(is_palindrome("radar"))  # True
print(is_palindrome("raddar"))  # True
print(is_palindrome("hello"))  # False