class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dir_name = ""
        for ch in path:
            if ch == "/":
                if dir_name == "..":
                    if stack:
                        stack.pop()
                elif dir_name and not dir_name == ".":
                    stack.append(dir_name)
                dir_name = ""
            else:
                dir_name += ch
        if dir_name == "..":
            if stack:
                stack.pop()
        elif dir_name and not dir_name == ".":
            stack.append(dir_name)
        dir_name = ""
        
        return "/" + "/".join(stack)