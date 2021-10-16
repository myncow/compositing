import itertools
def process_rules_arr(filenames,exceptions):
    rules_arr=exceptions
    res_arr=[]

    nogo=[]
    c=0
    
    for file in filenames:
        for rule in rules_arr:
            if find_combination(file,rule):
                c+=1
                nogo.append(file)

    for file in filenames:
        if file in nogo:
            continue
        else:
            res_arr.append(file)

    return res_arr

def process_rules_traits(filenames,exceptions):
    rules_arr=exceptions
    res_arr=[]

    for i in rules_arr:
        i=i[:-4]

    nogo=[]
    c=0
    
    for file in filenames:
        for rule in rules_arr:
            if find_combination(file,rule):
                c+=1
                nogo.append(file)

    for file in filenames:
        if file in nogo:
            continue
        else:
            res_arr.append(file)

    return res_arr

def find_combination(filename,rule):
    img1,img2=rule
    flag1 = False
    flag2 = False
    for i in range(len(filename)):
        if img1 in filename[i]:
            flag1 = True

    for i in range(len(filename)):
        if img2 in filename[i]:
            flag2=True
    
    return (flag1 and flag2)