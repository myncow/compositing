import itertools, os
def permute():
    layer_list=get_layer_list()
    layer_lol=[]
    for layer in layer_list:
        layer_lol.append(os.listdir(f'layers/{layer}'))
    permutations=list(itertools.product(*layer_lol))
    return permutations