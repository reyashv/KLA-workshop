from PIL import Image,ImageChops
import numpy as np
import csv
image1 = Image.open("wafer_image_1.png")
image2 = Image.open("wafer_image_2.png")
new_image = Image.new('RGB',(2*image1.size[0], image1.size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1.size[0],0))

image3 = Image.open("wafer_image_3.png")
image4 = Image.open("wafer_image_4.png")
new_image2 = Image.new('RGB',(2*image3.size[0], image3.size[1]), (250,250,250))
new_image2.paste(image3,(0,0))
new_image2.paste(image4,(image3.size[0],0))

new_image3 = Image.new('RGB',(2*new_image.size[0], new_image.size[1]), (250,250,250))
new_image3.paste(new_image,(0,0))
new_image3.paste(new_image2,(new_image.size[0],0))

image5 = Image.open("wafer_image_5.png")
new_image4 = Image.new('RGB',(new_image3.size[0]+image5.size[0], new_image3.size[1]), (250,250,250))
new_image4.paste(new_image3,(0,0))
new_image4.paste(image5,(new_image3.size[0],0))
#new_image4.show()

b1=np.asarray(image1)
b2=np.asarray(image2)
a1=np.asarray(image3)
a2=np.asarray(image4)
a3=np.asarray(image5)
b3=b1-b2
b4=b1-a1
b5=b1-a2
b6=b1-a3
b7=b2-a1
b8=b2-a2
b9=b2-a3
b10=a1-a2
b11=a1-a3
b12=a2-a3
diff = Image.fromarray(b3)
diff1 = Image.fromarray(b4)
diff2 = Image.fromarray(b5)
diff3 = Image.fromarray(b6)
diff4 = Image.fromarray(b7)
diff5 = Image.fromarray(b8)
diff6 = Image.fromarray(b9)
diff7 = Image.fromarray(b10)
diff8 = Image.fromarray(b11)
diff9 = Image.fromarray(b12)
l=[]
def common_member(a, b):
    result = [i for i in a if i in b]
    return result
# 
pim = diff.convert('RGB')
im  = np.array(pim)
black=[0,0,0]
X,Y = np.where(np.all(im!=black,axis=2))
l=[]
for i in range(0,len(X)):
    t=()
    t=t+(X[i],Y[i])
    l.append(t)
cm=[]
#
pim=diff1.convert('RGB')
im=np.array(pim)
X,Y = np.where(np.all(im!=black,axis=2))
l1=[]
for i in range(0,len(X)):
    t=()
    t=t+(X[i],Y[i])
    l1.append(t)

ll=[]
cm=common_member(l,l1)
for i in cm:
    i=(1,)+i
    ll.append(i)


l2=[]
cm2=[]
#
pim = diff2.convert('RGB')
im  = np.array(pim)
black=[0,0,0]
X,Y = np.where(np.all(im!=black,axis=2))
for i in range(0,len(X)):
    t=()
    t=t+(X[i],Y[i])
    l2.append(t)

l4=[]
cm2=common_member(l1, l2)
for i in cm2:
    i=(1,)+i
    l4.append(i)
ll2=[]

cmm=common_member(l, l2)
for i in cmm:
    i=(1,)+i
    ll2.append(i)

#
pim=diff3.convert('RGB')
im=np.array(pim)
X,Y = np.where(np.all(im!=black,axis=2))
l3=[]
l19=[]
l20=[]
l21=[]
for i in range(0,len(X)):
    t=()
    t=t+(X[i],Y[i])
    l3.append(t)
cm3=common_member(l,l3)
for i in cm3:
    i=(1,)+i
    l19.append(i)
cm7=common_member(l1,l3)
for i in cm7:
    i=(1,)+i
    l20.append(i)
   
cm8=common_member(l2,l3)
for i in cm8:
    i=(1,)+i
    l21.append(i)

#
pim = diff4.convert('RGB')
im  = np.array(pim)
black=[0,0,0]
n=[]
X,Y = np.where(np.all(im!=black,axis=2))
l5=[]
for i in range(0,len(X)):
    t=()
    t=t+(X[i],Y[i])
    l5.append(t)
cmp=common_member(l, l5)
for i in cmp:
    i=(2,)+i
    n.append(i)

#
pim=diff5.convert('RGB')
im=np.array(pim)
ll1=[]
X,Y = np.where(np.all(im!=black,axis=2))
l6=[]
for i in range(0,len(X)):
    t=()
    t=t+(X[i],Y[i])
    l6.append(t)
cm4=common_member(l5, l6)
for i in cm4:
    i=(2,)+i
    ll1.append(i)
n1=[]
cmp1=common_member(l, l6)
for i in cmp1:
    i=(2,)+i
    n1.append(i)

l8=[]
#
pim = diff6.convert('RGB')
im  = np.array(pim)
black=[0,0,0]
l7=[]
X,Y = np.where(np.all(im!=black,axis=2))
for i in range(0,len(X)):
    t=()
    t=t+(X[i],Y[i])
    l7.append(t)
cm5=common_member(l5, l7)
for i in cm5:
    i=(2,)+i
    l8.append(i)
l23=[]
l24=[]
cm9=common_member(l, l7)
for i in cm9:
    i=(2,)+i
    l23.append(i)  
    
cm10=common_member(l6, l7)
for i in cm10:
    i=(2,)+i
    l24.append(i)  

    
#
pim=diff7.convert('RGB')
im=np.array(pim)
X,Y = np.where(np.all(im!=black,axis=2))

l9=[]
for i in range(0,len(X)):
    t=()
    t=t+(X[i],Y[i])
    l9.append(t) 


cm6=[]
#
pim = diff8.convert('RGB')
im  = np.array(pim)
black=[0,0,0]
X,Y = np.where(np.all(im!=black,axis=2))

l10=[]
l11=[]
for i in range(0,len(X)):
    t=()
    t=t+(X[i],Y[i])
    l10.append(t)
cm6=common_member(l9, l10)
for i in cm6:
    i=(3,)+i
    l11.append(i)
lists=l4+ll+ll2+l19+l20+l21
lists1=n+ll1+n1+l8+l23+l24
with open('sample.csv','w') as f:
    writer = csv.writer(f,delimiter=",")
    for tup in lists:
        writer.writerow(tup)
    for tup in lists1:
        writer.writerow(tup)
    for tup in l11:
        writer.writerow(tup)

#print(l8)
#print(l11)
#
'''pim=diff9.convert('RGB')
im=np.array(pim)
X,Y = np.where(np.all(im!=black,axis=2))
for i in range(0,len(X)):
    f.write("(")
    f.write(str(X[i]))
    f.write(",")
    f.write(str(Y[i]))
    f.write(")")
    f.write("\n")''' 
    
f=open("C:\\Users\\91994\\Downloads\\Workshop_Problem\\Level_1_Input_Data\\input.json","r")
a=f.read()

