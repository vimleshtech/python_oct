import pandas as pd

data = pd.read_csv(r'C:\Users\vkumar15\Desktop\Python\test.csv')
print(data)

print(data.columns)

d = data.values # convert df to lish

#print(d[0])
#print(d[0][9])
total = 0
for r in d:
     
     total += r[9]
     print(total)
     

print(total)

print('kmeans ..')
out = []
for r in d:
     print (r[9]/total)
     out.append(r[9]/total)
     #print(total)
     


#classification
ran = max(out) - min(out)
c = ran / 2

myout=[]

temp =min(out)
for i in range(0,2):
     cul=[]
     r1 =temp     
     r2 = c
     
     for item in out:
          if item >= r1 and item <r2:
               cul.append(item)

     myout.append(cul)
     temp = r2
     c = c+c

print(myout)



               
                    


     







     



