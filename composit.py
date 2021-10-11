from wand.image import Image
from wand.display import display
import os
import itertools
import random
import sys
import time
import json

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush() 


def get_layer_list():
    layer_list=os.listdir('layers')
    index = layer_list.index(".DS_Store")
    del layer_list[index]
    layer_list.sort()
    layer_list
    return layer_list

def permute():
    layer_list=get_layer_list()
    layer_lol=[]
    for layer in layer_list:
        layer_lol.append(os.listdir(f'layers/{layer}'))
    permutations=list(itertools.product(*layer_lol))
    return permutations

def composite_all_permutations():
    perms=permute()
    n=len(perms)
    for count, perm in enumerate(perms):
        progress(count,n,status='compositing all permutations')
        filenames=[f'layers/layer_{i+1}/{perm[i]}' for i in range(len(perm))]
        with Image(filename=filenames[0]) as l1:
            with Image(filename=filenames[1]) as l2:
                with Image(filename=filenames[2]) as l3:
                    with Image(filename=filenames[3]) as l4:
                            with Image(filename=filenames[4]) as l5:
                                with Image(filename=filenames[5]) as l6:
                                    with Image(filename=filenames[6]) as l7:
                                        l1.composite(l2)
                                        l1.composite(l3)
                                        l1.composite(l4)
                                        l1.composite(l5)
                                        l1.composite(l6)
                                        l1.composite(l7)
                                        l1.save(filename=f'output/permutations/permutation_{count}.png')

def display_random():
    perms=permute()
    rand_perm=random.choice(perms)
    with Image(filename=f'layers/layer_1/{rand_perm[0]}') as l1:
            with Image(filename=f'layers/layer_2/{rand_perm[1]}') as l2:
                with Image(filename=f'layers/layer_3/{rand_perm[2]}') as l3:
                    with Image(filename=f'layers/layer_4/{rand_perm[3]}') as l4:
                            with Image(filename=f'layers/layer_5/{rand_perm[4]}') as l5:
                                with Image(filename=f'layers/layer_6/{rand_perm[5]}') as l6:
                                    l1.composite(l2)
                                    l1.composite(l3)
                                    l1.composite(l4)
                                    l1.composite(l5)
                                    l1.composite(l6)
                                    display(l1)
def extract_parray(d):
    return [(k,v) for k,v in d.items()]

def generate_fpath(n,layer_name):
    return f"layers/layer_{n}/{layer_name}"


def process_layer(layer,arr,n,total):
    if arr == None:
        arr=[[] for _ in range(total)]
        ind=[j for j in range(total)]
        random.shuffle(ind)
        for tuple in layer:
            layer_name=tuple[0]
            amount=tuple[1]
            for _ in range(amount):
                rand_i=ind.pop()
                arr[rand_i].append(f"layers/layer_{n}/{layer_name}.png")
    else:
        ind=[j for j in range(total)]
        random.shuffle(ind)
        for tuple in layer:
            layer_name=tuple[0]
            amount=tuple[1]
            for _ in range(amount):
                rand_i=ind.pop()
                arr[rand_i].append(f"layers/layer_{n}/{layer_name}.png")
        
    
    return arr

def composite(filenames,count):
    with Image(filename=filenames[0]) as l1:
        with Image(filename=filenames[1]) as l2:
            with Image(filename=filenames[2]) as l3:
                with Image(filename=filenames[3]) as l4:
                        with Image(filename=filenames[4]) as l5:
                            with Image(filename=filenames[5]) as l6:
                                with Image(filename=filenames[6]) as l7:
                                    l1.composite(l2)
                                    l1.composite(l3)
                                    l1.composite(l4)
                                    l1.composite(l5)
                                    l1.composite(l6)
                                    l1.composite(l7)
                                    l1.save(filename=f'output/prob/{count}.png')

def composite_probabilistically(total=100):
    n_layers=7
    with open("config.json") as f:
        data = json.load(f)
    data=data["Layers"]
    layer_names=list(data.keys())
    data=[extract_parray(data[i]) for i in layer_names]

    filenames=[]
    arr=None
    for i in range(n_layers):
        arr=process_layer(data[i],arr,i+1,total)

    for j,img in enumerate(arr):
        progress(j,total,status=f'compositing {total} images')
        arr=composite(img,j)
    

    