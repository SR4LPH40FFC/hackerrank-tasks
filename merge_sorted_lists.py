def merge(l1, l2):
    l = []
    x = 0
    y = 0

    while True:
        if(x >= len(l1)):
            while(y<len(l2)):
                l.append(l2[y])
                y+=1
            break

        if(y >= len(l2)):
            while(x<len(l1)):
                l.append(l1[x])
                x+=1
            break

        if(l1[x] <= l2[y]):
            l.append(l1[x])
            x+=1
        else:
            l.append(l2[y])
            y+=1

    return l
 
print merge( [1,3,5,6,7,8,9,10,11,123], [2,4,6,9,11] )
