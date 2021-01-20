class Solution:
    def isValid(self, s: str) -> bool:
        
        length = len(s)
        stack = list()
        
        myMap = { ")" : "(", "}" : "{", "]" : "[" }
        
        mySet = set()
        mySet.add("(")
        mySet.add("{")
        mySet.add("[")
        
        for i in range(length):
            if s[i] in mySet:
                stack.append(s[i])
            else:
                if(not stack):
                    return False
                n = stack.pop()
                if(myMap[s[i]] != n):
                    return False
        if(stack):
            return False
        else:
            return True