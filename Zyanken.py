'''
Created on 2019/10/09

@author: t17cs026
'''
import random
a = random.randint(0,2)
b = random.randint(0,2) 
s = a 
t = b 
e='判定'
if s == 0:
    c = 'グー'
elif s == 1:
    c = 'チョキ'
elif  s == 2:
    c='パー'
if t == 0:
    d = 'グー'
elif t == 1:
    d = 'チョキ'
elif t  == 2:
    d='パー'
if ((s == 0) and  (t == 0)) or ((s == 1) and (t == 1)) or ((s == 2) and (t == 2)):
    e = '引き分け'
elif ((s == 0) and (t == 1)) or ((s == 1) and (t == 2)) or ((s == 2 ) and (t == 0)):
    e = 'Aの勝ち'
else :
    e = 'Bの勝ち' 
print('Aの手:',c,'Bの手:',d,e)

