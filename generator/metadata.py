import json
def write_metadata(traits,n):
    f=open('generator/template.json')
    data=json.load(f)
    for k,v in traits.items():
        trait=k
        if trait=="planet":
            i=0
        elif trait=="rocket":
            i=1
        elif trait=="astronaut":
            i=2
        elif trait=="fuel":
            i=3
        data["attributes"][i]["trait_type"]=trait
        data["attributes"][i]["value"]=v

    write_data=json.dumps(data)
    
    with open(f"output/json/{n}.json", "w") as outfile:
        outfile.write(write_data)

def create_metadata(arr):
    traits={
        "planet":arr[0],
        "rocket":arr[4],
        "astronaut":arr[6],
        "fuel":arr[3]
    }
    return traits