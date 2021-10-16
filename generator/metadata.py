import json
def write_metadata(traits,n):
    f=open('generator/template.json')
    data=json.load(f)
    for k,v in traits.items():
        trait=k
        if trait=="sky":
            i=0
        elif trait=="planet":
            i=1
        elif trait=="rocket":
            i=2
        elif trait=="astronaut":
            i=3
        elif trait=="fuel":
            i=4
        data["attributes"][i]["trait_type"]=trait
        data["attributes"][i]["value"]=v

    write_data=json.dumps(data)
    
    with open(f"output/json/{n}.json", "w") as outfile:
        outfile.write(write_data)

def create_metadata(arr):
    traits={
        "sky": arr[0],
        "planet":arr[1],
        "rocket":arr[5],
        "astronaut":arr[7],
        "fuel":arr[2]
    }
    return traits