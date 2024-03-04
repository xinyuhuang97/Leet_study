class Solution:
    def intToRoman(self, num: int) -> str:
        dic={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        roman=[]
        lg=len(str(num))
        if lg==4:
            value=num//1000
            roman+=[value*"M"]
            num=num%1000
        if len(str(num))==3:
            value=num//100
            num=num%100
            if value==9:
                roman+=["C","M"]
            elif value>=5 and value<9:
                roman+=["D","C"*(value-5)]
            
            elif value==4:
                roman+=["C", "D"]
            else:
                roman+=["C"*value]
        if len(str(num))==2:
            value=num//10
            num=num%10
            if value==9:
                roman+=["X", "C"]
            elif value>=5 and value<9:
                roman+=["L","X"*(value-5)]
            elif value==4:
                roman+=["X", "L"]
            else:
                roman+=["X"*value]
        if len(str(num))==1:
            value=num
            if value==9:
                roman+=["I", "X"]
            elif value>=5 and value<9:
                roman+=["V","I"*(value-5)]
            elif value==4:
                roman+=["I", "V"]
            else:
                roman+=["I"*value]
        return("".join(roman))