import collections
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        mut_dic=["T","A","C","G"]
        deque=collections.deque([(startGene,0)])
        solutions=[startGene]
        if startGene==endGene:
            return 0
        if bank==[]:
            return -1
        if endGene not in bank:
            return -1
        while deque:
            info=deque.popleft()
            gene,count=info
            #print("gene",gene)
            for i,letter in enumerate(gene):
                for new_letter in mut_dic:
                    if new_letter==gene[i]:
                        continue
                    if i==0:
                        mut=new_letter+gene[1:]
                    else:
                        mut=gene[:i]+new_letter+gene[i+1:]
                    #print(i, mut)
                    #print(mut, endGene, mut==endGene)
                    if mut==endGene:
                        print("hi")
                        return count+1
                    if mut not in solutions and mut in bank:
                        deque.append((mut,count+1))
                        solutions.append(mut)
        #print(solutions)
        return -1
        