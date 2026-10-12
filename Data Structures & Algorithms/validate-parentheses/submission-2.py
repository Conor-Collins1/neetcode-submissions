class Solution:
    def isValid(self, s: str) -> bool:

        # normal = 0
        # square = 1
        # squig = 2

        seen = []
        size = 0
        i = 0
        for c in s:

            if c == "(":
                seen.append(0)
                size += 1
            elif c == "[":
                seen.append(1)
                size += 1
            elif c == "{":
                seen.append(2)
                size += 1
            elif size == 0:
                return False
            
            
            
            
            if c == ")":
                if seen[(size - 1)] == 0:
                    seen.pop()
                    size -= 1
                else:
                    return False
            if c == "]":
                if seen[(size - 1)] == 1:
                    seen.pop()
                    size -= 1
                else:
                    return False
            if c == "}":
                if seen[(size - 1)] == 2:
                    seen.pop()
                    size -= 1
                else:
                    return False


        if size == 0 :
            return True
        else:
            return False

                

        