import random
import matplotlib .pyplot as plt
import numpy as np

liste1=[]
liste2=[]


for i in range(4):
    x=random.randint(1,10);
    y=random.randint(1,10);
    liste1.append(x);
    liste2.append(y);

print(liste2[0])
print(liste1[0])
b=a*liste1[0]+liste2[0]
print(b)

#plt.plot(liste1,liste2)
