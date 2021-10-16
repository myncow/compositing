import itertools
def process_rules_arr(filenames,exceptions):
    rules_arr=exceptions
    print(rules_arr)
    res_arr=[]

    for file in filenames:
        for rule in rules_arr:
            i

    for rule in rules_arr:
        for file in filenames:
            #logic
            if find_combination(file,rule):
                continue
            else:
                res_arr.append(file)
    res_arr.sort()
    res=list(res_arr for res_arr,_ in itertools.groupby(res_arr))

    return res

def process_rules_traits(filenames,exceptions):
    rules_arr=exceptions
    res_arr=[]

    for i in rules_arr:
        i=i[:-4]
    
    for rule in rules_arr:
        for file in filenames:
            #logic
            if find_combination(file,rule):
                continue
            else:
                res_arr.append(file)
   
    return res_arr

def find_combination(filename,rule):
    img1,img2=rule
    flag1 = False
    flag2 = False
    for i in range(len(filename)):
        if rule[0] in filename[i]:
            flag1 = True

    for i in range(len(filename)):
        if rule[0] in filename[i]:
            flag2=True
    
    return (flag1 and flag2)