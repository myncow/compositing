import os, random, sys, json
from .composite import composite
from .metadata import create_metadata, write_metadata
from .rules import process_rules_arr, process_rules_traits, find_combination

# PROGRESS BAR
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

# LOGIC HELPERS
def get_layer_list():
    layer_list=os.listdir('../layers')
    index = layer_list.index(".DS_Store")
    del layer_list[index]
    layer_list.sort()
    layer_list
    return layer_list

def extract_parray(d):
    return [(k,v) for k,v in d.items()]

def generate_fpath(n,layer_name):
    return f"../layers/layer_{n}/{layer_name}"

#LAYER PROCESSOR
def process_layer(layer,arr, traits, n,total):
    if arr == None:
        arr=[[] for _ in range(total)]
        traits=[[] for _ in range(total)]
        ind=[j for j in range(total)]
        random.shuffle(ind)
        for tuple in layer:
            layer_name=tuple[0]
            amount=tuple[1]
            for _ in range(amount):
                rand_i=ind.pop()
                traits[rand_i].append(layer_name)
                arr[rand_i].append(f"layers/layer_{n}/{layer_name}.png")
    else:
        ind=[j for j in range(total)]
        random.shuffle(ind)
        for tuple in layer:
            layer_name=tuple[0]
            amount=tuple[1]
            for _ in range(amount):
                rand_i=ind.pop()
                traits[rand_i].append(layer_name)
                arr[rand_i].append(f"layers/layer_{n}/{layer_name}.png")
    return arr,traits


# MAIN
def composite_probabilistically():
    with open("generator/config.json") as f:
        data = json.load(f)

    total=data["total"]
    n_layers=data["n_layers"]
    exceptions=data["exceptions"]    
    data=data["Layers"]

    layer_names=list(data.keys())

    data=[extract_parray(data[i]) for i in layer_names]
    
    arr=None
    traits=None
    
    #create filename lists
    for i in range(n_layers):
        arr,traits=process_layer(data[i],arr,traits,i+1,total)

    #apply rules 
    x_rules=[]
    for k,v in exceptions.items():
        x_rules.append(v)
  
    arr=process_rules_arr(arr,x_rules)
    traits=process_rules_traits(traits,x_rules)

        

    #create metadata
    for t, trait in enumerate(traits):
        meta=create_metadata(trait)
        write_metadata(meta,t)

    #generate images
    tots=len(arr)
    for j,img in enumerate(arr):
        progress(j,tots,status=f'compositing {tots} images')
        composite(img,j)