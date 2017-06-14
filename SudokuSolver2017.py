from __future__ import print_function
from random import choice
from time import time
from itertools import izip
import pdb
try:
    from Tkinter import *
except NameError:
    pass
except ImportError:
    pass


Input=[1,7,0,0,2,3,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,8,4,9,2,6,0,4,6,0,0,5,7,0,0,8,2,0,9,6,0,0,0,4,5,3,0,0,5,0,4,8,1,0,9,4,7,1,0,8,3,0,0,0,1,0,3,7,0,6,0,4]

print(len(Input))
#Standart-1,7,0,0,2,3,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,8,4,9,2,6,0,4,6,0,0,5,7,0,0,8,2,0,9,6,0,0,0,4,5,3,0,0,5,0,4,8,1,0,9,4,7,1,0,8,3,0,0,0,1,0,3,7,0,6,0,4
#Easy-7,4,0,0,0,0,8,6,2,6,1,0,2,8,0,0,5,9,0,2,9,0,7,0,1,0,0,4,9,0,6,2,7,0,0,3,0,0,7,4,5,0,9,2,0,5,0,2,1,0,0,0,7,6,9,3,6,0,1,0,2,0,8,0,7,0,8,0,9,3,1,0,0,0,8,3,4,0,6,9,0
#0,6,0,8,0,4,3,0,0,0,0,9,0,0,7,0,4,8,0,8,4,0,3,0,7,0,0,9,0,0,7,0,2,0,3,0,0,0,2,3,0,9,0,0,0,0,0,0,0,0,0,2,0,9,5,0,0,0,2,0,1,0,0,4,0,0,5,0,0,0,8,0,6,0,7,0,1,0,0,2,0
#0,0,0,9,0,6,1,5,0,0,0,0,4,1,0,9,0,0,0,1,9,0,0,5,0,0,4,1,9,0,7,0,0,0,0,5,3,0,8,1,0,4,0,0,0,0,7,0,0,0,9,0,4,1,9,0,0,8,0,0,4,0,0,7,0,1,0,0,0,5,2,0,0,2,3,0,9,0,0,7,8
#Most Hard Sudok In The World-8,0,0,0,0,0,0,0,0,0,0,3,6,0,0,0,0,0,0,7,0,0,9,0,2,0,0,0,5,0,0,0,7,0,0,0,0,0,0,0,4,5,7,0,0,0,0,0,1,0,0,0,3,0,0,0,1,0,0,0,0,6,8,0,0,8,5,0,0,0,1,0,0,9,0,0,0,0,4,0,0
#Second Most Hard Sudoku In The World-0,0,5,3,0,0,0,0,0,8,0,0,0,0,0,0,2,0,0,7,0,0,1,0,5,0,0,4,0,0,0,0,5,3,0,0,0,1,0,0,7,0,0,0,6,0,0,3,2,0,0,0,8,0,0,6,0,5,0,0,0,0,9,0,0,4,0,0,0,0,3,0,0,0,0,0,0,9,7,0,0

Rows=[Input[0:9],Input[9:18],Input[18:27],Input[27:36],Input[36:45],Input[45:54],Input[54:63],Input[63:72],Input[72:]]

Time1=time()      

def Converter(self): #Convert Row to Cell
    return list(izip(self[0], self[1], self[2], self[3], self[4], self[5], self[6], self[7], self[8]))

def Print(self): #Print Values
    def Prin(x):
        print(x,end="  ")
    [(map(Prin, x), print("\n")) for x in self]

def TrueFalser(self):
    def TF(x):
        if x==0: return False
        else: return True
    return [map(TF, x) for x in self]

def Cubik(data): 
    if len(data)!=81:
        self,i=[],0
        for x in data:
            for x in data[i]:
                self.append(x)
            i+=1
    else:
        self=data
    Cubik=[self[0:3]+self[9:12]+self[18:21],
         self[3:6]+self[12:15]+self[21:24],
         self[6:9]+self[15:18]+self[24:27],
         self[27:30]+self[36:39]+self[45:48],
         self[30:33]+self[39:42]+self[48:51],
         self[33:36]+self[42:45]+self[51:54],
         self[54:57]+self[63:66]+self[72:75],
         self[57:60]+self[66:69]+self[75:78],
         self[60:63]+self[69:72]+self[78:]]
    return Cubik

def Cubik2Val(self):  
    Val=[[self[0][0],self[0][1],self[0][2],self[1][0],self[1][1],self[1][2],self[2][0],self[2][1],self[2][2]],
         [self[0][3],self[0][4],self[0][5],self[1][3],self[1][4],self[1][5],self[2][3],self[2][4],self[2][5]],
         [self[0][6],self[0][7],self[0][8],self[1][6],self[1][7],self[1][8],self[2][6],self[2][7],self[2][8]],
         [self[3][0],self[3][1],self[3][2],self[4][0],self[4][1],self[4][2],self[5][0],self[5][1],self[5][2]],
         [self[3][3],self[3][4],self[3][5],self[4][3],self[4][4],self[4][5],self[5][3],self[5][4],self[5][5]],
         [self[3][6],self[3][7],self[3][8],self[4][6],self[4][7],self[4][8],self[5][6],self[5][7],self[5][8]],
         [self[6][0],self[6][1],self[6][2],self[7][0],self[7][1],self[7][2],self[8][0],self[8][1],self[8][2]],
         [self[6][3],self[6][4],self[6][5],self[7][3],self[7][4],self[7][5],self[8][3],self[8][4],self[8][5]],
         [self[6][6],self[6][7],self[6][8],self[7][6],self[7][7],self[7][8],self[8][6],self[8][7],self[8][8]]]
    return Val

Print(Rows)

print("Starting Solving...")

Cells=Converter(Rows) 
Cubiks=Cubik(Input)

Informaton=[] #Head Massiv

def information(title_to_write,input_values,replace,Information=[]): 
    i,j=0,0
    if replace: 
        for x in input_values:
            for x in input_values[i]:
                input_values[i][j]={'%s' % title_to_write: input_values[i][j]}
                j+=1
            j=0
            i+=1
        return input_values
    else: 
        for x in Information:
            for x in Information[i]:
                Information[i][j]['%s' % title_to_write]=input_values[i][j]
                j+=1
            j=0
            i+=1
        return Information


Information=information('Rows', Rows, True) 
Information=information('Cells', Cells, False,Information=Information)
Information=information('Cubiks', Cubiks, False,Information=Information)
del Input,Rows, Cells, Cubiks 


def Valuer(title_to_write,key_to_extract,input_values): 
    output_values=[[y['%s' % key_to_extract] for y in x] for x in input_values] 
    def small_function(line):
        i=0
        for x in line:
            if line[i]==0:
                for x in range(9):
                    if line.count(x+1)==0:
                        try:
                            line[i].append(x+1)
                        except AttributeError:
                            line[i]=[x+1]
            i+=1
        return line
    output_values=map(small_function,output_values) 
    output_values=information('%s' % title_to_write, output_values, False, input_values)
    return output_values

Information=Valuer("Values_Rows","Rows",Information)
Information=Valuer("Values_Cells","Cells",Information)
Information=Valuer("Values_Cubiks","Cubiks",Information)


General_Values,data_Row,data_Cell,data_Cubik=[],[],[],[]

data=[[[y['%s' % key_to_extract] for y in x] for x in Information] for key_to_extract in ['Values_Rows','Values_Cells','Values_Cubiks']] 
data_Row,data_Cell,data_Cubik=data[0],data[1],data[2]

data_Cell,data_Cubik=Converter(data_Cell),Cubik2Val(data_Cubik) 
[list(x) for x in data_Cell] 


i,j=0,0
for x in data_Row: 
    General_Values.append([]) 
    for x in data_Row[i]:
        General_Values[i].append([])
        for x in range(9):
            try:
                if data_Row[i][j].count(x+1)==1: 
                    try:
                        if data_Cell[i][j].count(x+1)==1:
                            try:
                                if data_Cubik[i][j].count(x+1)==1:
                                        General_Values[i][j].append(x+1) 
                            except:
                                General_Values[i][j].append(data_Cubik[i][j])
                                break
                    except: 
                        General_Values[i][j].append(data_Cell[i][j])
                        break
            except: 
                General_Values[i][j].append(data_Row[i][j])
                break
        j+=1
    i+=1
    j=0

Path_Values_Cell=Converter(General_Values) 
Path_Values_Cubik=Cubik2Val(General_Values)

Information=information('Path_Values_Row',General_Values,False,Information) 
Information=information('Path_Values_Cell',Path_Values_Cell,False,Information)
Information=information('Path_Values_Cubik',Path_Values_Cubik,False,Information)

[[[i.pop(keys) for keys in ['Values_Rows','Values_Cells','Values_Cubiks']] for i in x] for x in Information]
del General_Values,data,data_Row,data_Cell,data_Cubik,Path_Values_Cell,Path_Values_Cubik



def Last_Hero(axis,key_to_extract): 
    axis,i=[x[key_to_extract] for x in axis],0 
    for x in axis:
        try: 
            if len(x)==1:
                axis[i]=x[0]
        except:
            pass
        i+=1
    return axis



def Check_axis(axis_Values):
    i=0 
    for x in axis_Values:
        for x in range(10)[1:]:
            try:
                if axis_Values[i].count(x)>1:
                    return True
            except:
                pass
        i+=1
    return False

def Alone_Detector(Information):
    axis_X,axis_Y,axis_Cubik,i=[[i['Path_Values_Row'] for i in x] for x in Information],[[i['Path_Values_Cell'] for i in x] for x in Information],[[i['Path_Values_Cubik'] for i in x] for x in Information],0 
    i,j=0,0
    for x in axis_X:
        for x in axis_X[i]:
            try:
                for number in axis_X[i][j]: 
                    if axis_X[i].count(number)==0: 
                        z,Alone=0,True 
                        for x in axis_X[i]:
                            try: 
                                for x in axis_X[i][z]:
                                    if axis_X[i][z].count(number)!=0 and z!=j:
                                        Alone=False 
                                        break
                            except:
                                pass
                            if Alone==False:
                                break
                            z+=1
                        if Alone==False: 
                            continue
                        backup=axis_X[i][j][:] 
                        axis_X[i][j]=number 
                        for x in [axis_X,axis_Y,axis_Cubik]: 
                            Error_Report=Check_axis(x) 
                            if Error_Report==True: 
                                axis_X[i][j]=backup[:] 
                                break
                        if Error_Report==True: 
                            continue
            except:
                pass
            j+=1
        i+=1
        j=0
    return axis_X


def Para_or_Trojka(axis,key_to_extract,para_or_trojka): 
    axis,i,data_para=[x[key_to_extract] for x in axis],0,[] 
    for x in axis: 
        try:
            if len(x)==para_or_trojka and axis.count(x)==para_or_trojka :
                data_para.append(x[:])
        except:
            pass
    for x in data_para: 
        for x in axis: 
            if x!=data_para[i]: 
                for j in data_para[i]:
                    try:
                        if x.count(j)==1: 
                            x.remove(j)
                    except:
                        pass
        i+=1
    return axis

for x in range(50):

    data=[[Last_Hero(x,key_to_extract) for x in Information] for key_to_extract in ['Path_Values_Row','Path_Values_Cell','Path_Values_Cubik']]

    Information=information('Path_Values_Row',data[0],False,Information)
    Information=information('Path_Values_Cell',data[1],False,Information)
    Information=information('Path_Values_Cubik',data[2],False,Information)

    data=[[Para_or_Trojka(x,key_to_extract,2) for x in Information] for key_to_extract in ['Path_Values_Row','Path_Values_Cell','Path_Values_Cubik']]

    Information=information('Path_Values_Row',data[0],False,Information) 
    Information=information('Path_Values_Cell',data[1],False,Information)
    Information=information('Path_Values_Cubik',data[2],False,Information)


    data=[[Last_Hero(x,key_to_extract) for x in Information] for key_to_extract in ['Path_Values_Row','Path_Values_Cell','Path_Values_Cubik']]

    Information=information('Path_Values_Row',data[0],False,Information) 
    Information=information('Path_Values_Cell',data[1],False,Information)
    Information=information('Path_Values_Cubik',data[2],False,Information)

    data=[[Para_or_Trojka(x,key_to_extract,3) for x in Information] for key_to_extract in ['Path_Values_Row','Path_Values_Cell','Path_Values_Cubik']]

    Information=information('Path_Values_Row',data[0],False,Information) 
    Information=information('Path_Values_Cell',data[1],False,Information)
    Information=information('Path_Values_Cubik',data[2],False,Information)

    data=[[Last_Hero(x,key_to_extract) for x in Information] for key_to_extract in ['Path_Values_Row','Path_Values_Cell','Path_Values_Cubik']]

    Information=information('Path_Values_Row',data[0],False,Information) 
    Information=information('Path_Values_Cell',data[1],False,Information)
    Information=information('Path_Values_Cubik',data[2],False,Information)


    del data

    
    data_X=Alone_Detector(Information)
    data_Y=Converter(data_X)
    data_Cubik=Cubik(data_X)


    Information=information('Path_Values_Row',data_X,False,Information) 
    Information=information('Path_Values_Cell',data_Y,False,Information)
    Information=information('Path_Values_Cubik',data_Cubik,False,Information)


    
    del data_X,data_Y,data_Cubik

    data=[[[z[key_to_extract] for z in x] for x in Information] for key_to_extract in ['Path_Values_Row','Path_Values_Cell','Path_Values_Cubik']]
    i,j,z=0,0,0
    for x in data:
        for x in data[i]:
            for x in data[i][j]:
                try:
                    for x in data[i][j][z]:
                        if data[i][j].count(x)==1:
                            data[i][j][z].remove(x)
                except:
                    pass
                z+=1
            j+=1
            z=0
        i+=1
        j=0
    Information=information('Path_Values_Row',data[0],False,Information) 
    Information=information('Path_Values_Cell',data[1],False,Information)
    Information=information('Path_Values_Cubik',data[2],False,Information)

    del data
    ###



data,backtrack_information,backtrack_level,Restart=[],[],0,True
i,j=0,0 
for x in Information:
    data.append([])
    for x in Information[i]:
        data[i].append(x['Path_Values_Row'])
        j+=1
    i+=1
    j=0
backup=[]
i=0
for x in data:
    backup.append([])
    for x in data[i]:
        backup[i].append(x)
    i+=1
i,j=0,0
for x in data:
    for x in data[i]:
        try:
            len(x)
            backtrack_information.append([i,j,0,len(x)]) 
        except:
            pass
        j+=1
    i+=1
    j=0
Print(data)
print(len(backtrack_information),' paths')
while Restart!=False:
    ###
    if backtrack_level>=len(backtrack_information): 
        Restart=False
        continue 
    if backtrack_information[backtrack_level][2]<=backtrack_information[backtrack_level][3]-1: 
        data[backtrack_information[backtrack_level][0]][backtrack_information[backtrack_level][1]]=(
             backup[backtrack_information[backtrack_level][0]][backtrack_information[backtrack_level][1]][backtrack_information[backtrack_level][2]])
    else: 
        if backtrack_level<=0:
            break
        data[backtrack_information[backtrack_level][0]][backtrack_information[backtrack_level][1]]=0
        backtrack_information[backtrack_level][2]=0
        backtrack_level-=1
        backtrack_information[backtrack_level][2]+=1
        continue
    i,j=0,0 
    for x in data: 
        for x in data[i]:
            try:
                if len(data[i][j])>0:
                    data[i][j]=0
            except TypeError:
                pass
            j+=1
        i+=1
        j=0
    data_Cell,data_Cubik=Converter(data),Cubik(data) 
    data_Cell=[list(x) for x in data_Cell] 
    for x in [data,data_Cell,data_Cubik]:
        Error_Report=Check_axis(x)
        if Error_Report==True: 
            x[backtrack_information[backtrack_level][0]][backtrack_information[backtrack_level][1]]=0
            backtrack_information[backtrack_level][2]+=1
            del data_Cell,data_Cubik
            break 
    if Error_Report==True: 
        continue
    backtrack_level+=1
    del data_Cell,data_Cubik
    ###
try:
    del data_Cell,data_Cubik
except:
    pass


Time2=time()
print("\n")
Time=Time2-Time1
Print(data)
print("Solve in %i seconds" % Time)
    
        






