def check_parentheses(str):
    l2 = []
    for bracket in str:
        if bracket == "(" or bracket == "[" or bracket == "{":
            l2.append(bracket)
        elif bracket == ")":
            x = l2.pop()
            if x == "{" or x == "[":
                return False
        elif bracket == "]":
            x = l2.pop()
            if x == "(" or x =="{":
                return False
        elif bracket == "}":
            x = l2.pop()
            if x == "(" or x =="[":
                return False
    else:
        return True
        


