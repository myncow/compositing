from wand.image import Image
import os
import itertools

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
    for count, perm in enumerate(perms):
        with Image(filename=f'layers/layer_1/{perm[0]}') as l1:
            with Image(filename=f'layers/layer_2/{perm[1]}') as l2:
                with Image(filename=f'layers/layer_3/{perm[2]}') as l3:
                    with Image(filename=f'layers/layer_4/{perm[3]}') as l4:
                            with Image(filename=f'layers/layer_5/{perm[4]}') as l5:
                                with Image(filename=f'layers/layer_6/{perm[5]}') as l6:
                                    l1.composite(l2)
                                    l1.composite(l3)
                                    l1.composite(l4)
                                    l1.composite(l5)
                                    l1.composite(l6)
                                    l1.save(filename=f'output/permutations/permutation{count}.png')

def composite_probabilistically():
    pass
