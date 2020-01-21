def append_0s_left(left):
    if(len(left) < 2):
        return '0'+left
    else:
        return left

def append_0s_right(right):
    if(len(right) < 2):
        return '00'+right
    elif(len(right) < 3):
        return '0'+right
    else:
        return right


def zad_1(start_code,end_code):
    big1 = int(start_code[0:2])
    big2 = int(end_code[0:2])
    small1 = int(start_code[3:6])
    small2 = int(end_code[3:6])
    
    if(big1 > big2 or (big1==big2 and small1 > small2)):
        temp = big1
        big1 = big2
        big2 = temp

        temp = small1
        small1 = small2
        small2 = temp
    

    for i in range(big1,big2+1):
        if i != big2 and i!= big1:
            for j in range(0,1000):
                left = append_0s_left(str(i));
                right = append_0s_right(str(j));
                
                print(left+'-'+right)
        elif i!=big2 and i==big1:
            for j in range(small1+1,1000):
                left = append_0s_left(str(i));
                right = append_0s_right(str(j));

                print(left+'-'+right)
        elif big1==big2:
            for j in range(small1+1,small2):
                left = append_0s_left(str(i));
                right = append_0s_right(str(j));

                print(left+'-'+right)
        else:
            for j in range(0,small2):
                left = append_0s_left(str(i));
                right = append_0s_right(str(j));

                print(left+'-'+right)


def zad_2(arr,upper_bound):
    missing_pieces=[]
    for i in range(1,upper_bound+1):
        if(arr.count(i)==0):
            missing_pieces.append(i)
    
    return missing_pieces


def zad_3(start,end):
    numbers = []
    step=0.5
    while(start<=end):
        numbers.append(start)
        start+=step
    return numbers




#zad_1('80-400','81-200')
#print(zad_2([2,3,7,4,9],10))
#print(zad_3(2,5.5))
