class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        last_dir=""
        for i, s in enumerate(path):
            if s!="/":
                last_dir+=s
            if s=="/" or i==len(path)-1 :
                if last_dir=="..":
                    if stack!=[]:
                        stack.pop()
                elif last_dir!=".":
                    if last_dir!="":
                        stack.append(last_dir)
                last_dir=''
        if last_dir!='':
            stack.append(last_dir)
        return "/"+"/".join(stack)