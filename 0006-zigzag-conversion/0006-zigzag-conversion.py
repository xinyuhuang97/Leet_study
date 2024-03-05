import numpy as np
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lg=len(s)
        if lg<numRows:
            return s
        if numRows==1:
            return s
        if numRows==2:
            value_d3=int(lg/2)
            rest_d3=lg%2
            first_line=[s[i*2] for i in range(lg//2+1*int(rest_d3==1))] 
            second_line=[s[i*2+1] for i in range(int(lg/2))] 
            return ''.join(first_line + second_line)
        numColumns=0
        count=0
        i=lg
        bool_zig_zag=False
        while i>0:
            if bool_zig_zag==True:
                i-=1
                count+=1
                if count==numRows-2:
                    bool_zig_zag=False
            else:
                i-=numRows
                bool_zig_zag=True
                count=0
            numColumns+=1
        matrix=np.chararray((numRows, numColumns),unicode=True)
        
        count=0
        i=lg
        bool_zig_zag=False
        column=0
        row=0
        while i>0:
            if bool_zig_zag==True:
                print(s[lg-i])
                matrix[row, column]=s[lg-i]
                i-=1
                count+=1
                column+=1
                row-=1
                if count==numRows-2:
                    bool_zig_zag=False
                    count=0
                    row=0
            else:
                #print(lg-i, lg-(i-(numRows)) )
                for j in range(lg-i, min(lg-(i-(numRows)),lg) ):
                    #print(s[j],j, i, row, column)
                    matrix[row, column]=s[j]
                    row+=1
                bool_zig_zag=True
                row=numRows-2
                column+=1
                i-=numRows
        #print(matrix)
        string=''.join([matrix[i][j] for i in range(numRows) for j in range(numColumns) if matrix[i][j]!=''])
        #print(string)
        return string
                
                
            