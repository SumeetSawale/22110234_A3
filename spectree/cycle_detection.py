import json

with open('out.json') as f:
    data = json.load(f)

cycle = None

def cycle_detection(path, cur_node):

    global cycle
    
    if cur_node in path:
        cycle = path + [cur_node]
        return True

    if 'imports' not in data[cur_node].keys():
        return False

    for node in data[cur_node]['imports']:
        if cycle_detection(path + [cur_node], node):
            return True

    return False

if cycle_detection([], '__main__'):
    print("Found Cycle")
    print(cycle)
else:
    print("No Cycle found")
