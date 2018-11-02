import time
import math
import os
import shutil


t = time.localtime()
print(t)

print(t.tm_year)
print(t.tm_mon)
print(t.tm_year)
print(t.tm_hour)

print(str(t.tm_year)+'-'+str(t.tm_mon)+'-'+str(t.tm_mday)  )

f=str(t.tm_year)+'-'+str(t.tm_mon)+'-'+str(t.tm_mday)

#create file will date 
a = open(r'C:\Users\vkumar15\Documents\django\poc\dashboard\data\mydata_'+f+'.txt','w')
a.close()

#time.sleep(5)

#wait
for i in range(1,5):
     print(i)
     #me.sleep(2)

#####
print(math.pi )
print(math.pow(2,10) )
print(2**10 )

print(math.sqrt(9))


##
l = os.listdir(r'C:\Users\vkumar15\Desktop')
print(l)

for f in l:
     if f.endswith('.txt'):
          print('---------------------------',f,'--------------------')
          
          s =r'C:\Users\vkumar15\Desktop\\'+f
          
          a = open(s, 'r')
          print(a.read())
          #print(s)
          
     


###copy the file
shutil.copy(r'C:\Users\vkumar15\Desktop\Python Session -28th Oct.txt',r'C:\Users\vkumar15\Documents\django\poc\dashboard\data\\')          


     
     
     


