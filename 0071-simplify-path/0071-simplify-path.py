class Solution:

    def simplifyPath(self, path: str) -> str:
        filename = ""
        q = []

        def handleFilename(filename: str, q: List[int]):
            if filename != '':
                if filename == '.':
                    filename = ''
                elif filename == '..':
                    if len(q) > 0:
                        q.pop()
                else:
                    q.append(filename)

        i = 0
        while i < len(path):
            if path[i] != '/':
                filename += path[i]
            else:
                handleFilename(filename, q)
                filename = ''
            i += 1
        
        handleFilename(filename, q)

        return f"/{"/".join(q)}"
                