import itertools
def process_rules_arr(filenames,exceptions):
    rules_arr=[]

    for k,v in exceptions.items():
        rules_arr.append((k,v))
    
    res_arr=[]

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
    rules_arr=[]

    for k,v in exceptions.items():
        rules_arr.append((k,v))
    
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
    #return true if img1,img_2 in filename
    c=0
    for layer in filename:
        if layer.find(img1) == -1:
            continue
        else:
            c+=1

        if layer.find(img2) == -1:
            continue
        else:
            c+=1
    
    return c==2