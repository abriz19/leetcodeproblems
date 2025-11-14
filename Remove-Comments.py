class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_block = False
        new_line = []
        
        for line in source:
            i = 0
            if not in_block:
                new_line = []  # reset when not in a block
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i:i+2] == '/*':
                    in_block = True
                    i += 2
                elif in_block and i + 1 < len(line) and line[i:i+2] == '*/':
                    in_block = False
                    i += 2
                elif not in_block and i + 1 < len(line) and line[i:i+2] == '//':
                    break  # ignore rest of the line
                elif not in_block:
                    new_line.append(line[i])
                    i += 1
                else:
                    i += 1
            if not in_block and new_line:
                res.append(''.join(new_line))
        
        return res
