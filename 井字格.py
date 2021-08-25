

l1=[' ',' ',' ']

l2=l1
l3=l2

w=''
while True:
    if l1[0]=='*' and l1[1]=='*' and l1[2]=='*':
        break
        w='*'
    if l2[0]=='*' and l2[1]=='*' and l2[2]=='*':
        break
        w = '*'
    if l3[0]=='*' and l4[1]=='*' and l4[2]=='*':
        break
        w = '*'

    if l1[0]=='·' and l1[1]=='·' and l1[2]=='·':
        break
        w='·'
    if l2[0]=='·' and l2[1]=='·' and l2[2]=='·':
        break
        w = '·'
    if l3[0]=='·' and l4[1]=='·' and l4[2]=='·':
        break
        w = '·'



    if l1[0]=='*' and l2[0]=='*' and l3[0]=='*':
        break
        w = '*'
    if l1[1]=='*' and l2[1]=='*' and l3[1]=='*':
        break
        w = '*'
    if l1[0]=='*' and l2[0]=='*' and l3[0]=='*':
        break
        w = '*'
    if l1[2]=='*' and l2[2]=='*' and l3[2]=='*':
        break
        w = '*'

    if l1[0]=='·' and l2[0]=='·' and l3[0]=='·':
        break
        w = '·'
    if l1[1]=='·' and l2[1]=='·' and l3[1]=='·':
        break
        w = '·'
    if l1[2]=='·' and l2[2]=='·' and l3[2]=='·':
        break
        w = '·'


    
    print(l1)
    print(l2)
    print(l3)
    
        #player *
    while True:
        
        data=input('玩家1\n')
        data=data.split(',')
        data1=int(data[0])
        data2=int(data[1])
        if data1<4 and data2<4:
            
            if data1 == 1:
                l1
            if data1 == 2:
                
            if data1 == 3
                
            else:
                print('无效数据')




