answer=list()
answer_2=list()
temp=0

def find_parent(begin,finish,array,temp):
    array_3 = list()

    if temp==0:
        answer_2.append(begin)
    else:
        pass

    for i in range(len(array)):
        if begin in array[i]:
            if begin == array[i][1]:
                array_3.append(array[i][0])# to find the parent
                answer_2.append(array[i][0])
                temp=temp+1
    if array_3[0]==finish:
        return(answer_2)
    else:
        find_parent(array_3[0],finish,array,temp)

    return(answer_2[::-1])

def find_child_parent(source,final,array):
    array_1 = list()
    array_2 = list()
    for i in range(len(array)):
        if source in array[i]:
            if source == array[i][0]:
                array_2.append(array[i][1])# To find the child elements

            else:
                array_1.append(array[i][0]) # To find the parent element


    if final in array_1:
        answer.append(source)
        answer.append(final)
        return(answer)

    elif final in array_2:
        for k in range(len(array_2)):
            if final==array_2[k]:
                answer.append(source)
                answer.append(final)
                return(answer)
    else:
        if len(array_1)==0:
            answer.append(source)
            return(answer)
            exit()
        answer.append(source)
        find_child_parent(array_1[0],final,array)
    return(ans;;wer)
