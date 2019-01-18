import re
import random
import string
import os
class IIGP_homework:
    def CountString(self,sen,spl='[ ,.?!]'):
        list1 = re.split(spl,sen)
        set1 = set(list1)
        set1.remove('')
        list2 = list(set1)
        dic1 = {}
        for i in range(len(list2)):
            dic1[list2[i]] = 0
            for j in range(len(list1)):
                if list2[i] == list1[j]:
                    dic1[list2[i]] += 1
        print(dic1)
        return dic1
    
    def FourNumberCombine(self):
        dic1 = {}
        n=1
        for i in range(1,5):
            for j in range(1,5):
                for k in range(1,5):
                    if i!=j and j!=k and k!=i:
                        dic1[i+10*j+100*k] = n
                        n+=1
        return dic1
    
    def Bonus(self,profit):
        if profit <= 10:
            return 0.1*profit
        elif profit < 20:
            return 0.1*10+(print-10)*0.075
        elif profit < 40:
            return 0.1*10+10*0.075+(profit-20)*0.05
        elif profit < 60:
            return 0.1*10+10*0.075+20*0.05+(profit-40)*0.03
        elif profit < 100:
            return 0.1*10+10*0.075+20*0.05+20*0.03+(profit-60)*0.015
        else:
            return 0.1*10+10*0.075+20*0.05+20*0.03+40*0.015+(profit-100)*0.01
        
    def MultiplicationTable(self):
        for i in range(1,10):
            for j in range(i,10):
                print("%d*%d=%2d" %(i,j,i*j),end=' ')
            print("")
            #swich line
        return 0
    def SumOfX(self,x):
        i=2
        sum = 0
        while i<=x:
            if i%2==0:
                sum = sum + i
            else:
                sum = sum - i
            i+=1
        return sum
    def MySort(self,nums,Algorithm='bubble'):
        if Algorithm == 'bubble':
            for i in range(len(nums)):
                for j in range(len(nums)-i-1):
                    if nums[j]>nums[j+1]:
                        temp = nums[j]
                        nums[j] = nums[j+1]
                        nums[j+1] = temp
        else:
            nums = self.MergeSort(nums)
      
        return nums
    def MergeSort(self, li):
        if len(li) == 1:
            #print('Len=1')
            return li
        
        #print(len(li))
        mid = len(li)//2 #整数除法

        left = li[:mid]
        right = li[mid:]
        
        l1 = self.MergeSort(left)
        r1 = self.MergeSort(right)
        #print(l1)
        #print(r1)
        return self.Merge(l1,r1)
    def Merge(self, left, right):
        result = []
        
        while len(left)>0 and len(right)>0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        #print(left)
        #print(right)
        result += left
        result += right
        #print(result)
        return result
    
    def GeneActivationCode(self,number,length):
        """
        number: 激活码数量
        length：激活码长度
        """
        result = {}
        source = list(string.ascii_uppercase)+list(string.ascii_lowercase)
        for index in range(0,10):
            source.append(str(index))
        while len(result) < number:
            key= ''
            for index in range(length):
                key += random.choice(source)
            if key in result:
                pass
            else:
                result[key] = 1
        #for key in result:
        #    print(key)
        return result

    def FindAFile(self,Afile,path):
        """
        file:要找的文件类型
        path:找文件的位置
        """
        result = {}
        #key = ''
        files=os.listdir(path)
        #print(files)
        for f in files:
            if f.split('.')[-1] == Afile:
                result[f] = 1
        return result
    
    def FindFile(self,name,path):
        """
        name:要找的文件名字
        path:找文件的位置
        """
        result = {}
        #key = ''
        files=os.listdir(path)
        #print(files)
        for f in files:
            if f == name:
                result['file'] = name
        #print(result)
        return result
    
    def CountProgram(self,name,path):
        """
        input:
            name:程序文件名字
            path:程序文件位置
        return:
            NumOfAnnotate
            NumOfCode
            NumOfBlackLine
        """
        NumOfAnnotate = 0
        NumOfCode = 0
        NumOfBlackLine = 0
        file = self.FindFile(name,path)['file']
        for line in file:
            if line == '' or line == '\n':
                NumOfBlackLine+=1
            elif line == '#':
                NumOfAnnotate+=1
            else:
                NumOfCode+=1
            
        return NumOfAnnotate,NumOfCode,NumOfBlackLine
            
        
        
        
        
    
#homework_01_python_01
sentence = 'One is always on a strange road, watching strange scenery and listening to strange music. Then one day, you will find that the things you try hard to forget are already gone. '
H = IIGP_homework()
H.CountString(sentence)

#homework_01_python_02
H.FourNumberCombine()

#homework_01_python_03
H.Bonus(100)

#homework_01_python_04
H.MultiplicationTable()

#homework_01_python_05
H.SumOfX(100)

#homework_01_python_06
nums = [9,8,7,6,10,4,3,2]
H.MySort(nums,'merge')

#homework_01_python_07
H.GeneActivationCode(10,7)

#homework_01_python_08
path = '/Users/lichen/Documents/GitHub/IIGP2018_homework/homework_01_python'
Afile = 'ipynb'
H.FindAFile(Afile,path)

#homework_01_python_09
path = '/Users/lichen/Documents/GitHub/IIGP2018_homework/homework_01_python'
name = 'homework_01_python.ipynb'
print(H.CountProgram(name,path))