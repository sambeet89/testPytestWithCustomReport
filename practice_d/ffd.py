


s = "()[]{}"
open_brackets = "([{"


brackets_pairs = {
    "(": ")",
    "[": "]",
    "{": "}"
}# [{()}]()




stack = []

for char in s:
    if char in open_brackets:
        stack.append(char)
    else:
        # If stack is empty when we see a closing bracket, it's invalid
        if not stack:
            print("not valid")
            exit()
        # Pop the last opened bracket and check if it matches
        last_opened = stack.pop()
        if brackets_pairs[last_opened] != char:
            print("not valid")
            exit()

# After processing all characters, stack should be empty for valid brackets
if stack:
    print("not valid")
else:
    print("valid")

    

      
        





