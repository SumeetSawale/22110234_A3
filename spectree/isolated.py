import json
import os

with open('out.json') as f:
    data = json.load(f)

project_root = '/home/sumeet/Sumeet/Study/STT/spectree/spectree'
python_files = []
for root, dirs, files in os.walk(project_root):
    for file in files:
        if file.endswith('.py'):
            python_files.append(os.path.join(root, file))

paths = []
info = data.values()
for i in info:
    paths.append(i['path'])

num_isolated = 0
for file in python_files:
    if file not in paths:
        print(file)
        num_isolated += 1

print("Number of isolated files: ", num_isolated)
