import collections
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def label_to_position(label):
            r = (label-1)//n
            if r%2==0:
                c = (label-1)%n
            else:
                c = (n-1)-(label-1)%n
            return (n-1)-r, c
        
        visit, q = set([1]), collections.deque([(1,0)])
        
        while q:
            label, count = q.popleft()
            r,c =label_to_position(label)
            if board[r][c]!=-1:
                label=board[r][c]
            if label==n*n:
                return count     
            for step in range(1, 7):
                new_label=label+step
                if new_label<=n*n and new_label not in visit:
                    q.append( (new_label, count+1))
                    visit.add(new_label)
        return -1