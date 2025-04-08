def is_matching_pair(opening, closing):
    return (opening == '(' and closing == ')') or \
           (opening == '{' and closing == '}') or \
           (opening == '[' and closing == ']')

def are_brackets_balanced(s):
    stack = []

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or not is_matching_pair(stack.pop(), ch):
                return False

    return len(stack) == 0

def main():
    s = input()

    if are_brackets_balanced(s):
        print("Brackets are balanced.")
    else:
        print("Brackets are not balanced.")

if __name__ == "__main__":
    main()
