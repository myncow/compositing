import json
def write_metadata(traits,n):
    f=open('generator/template.json')
    data=json.load(f)
    for k,v in traits.items():
        trait=k
        if trait=="trait_1":
            i=0
        elif trait=="trait_2":
            i=1
        elif trait=="trait_3":
            i=2
        elif trait=="trait_4":
            i=3
        elif trait=="trait_5":
            i=4
        data["attributes"][i]["trait_type"]=trait
        data["attributes"][i]["value"]=v

    write_data=json.dumps(data)
    
    with open(f"output/json/{n}.json", "w") as outfile:
        outfile.write(write_data)

def create_metadata(arr):
    traits={
        "trait_1": arr[0],
        "trait_2":arr[1],
        "trait_3":arr[4],
        "trait_4":arr[7],
        "trait_5":arr[5]
    }
    return traits