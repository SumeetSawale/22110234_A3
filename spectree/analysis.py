import json

with open('out.json') as f:
    data = json.load(f)

fan_in = {}
fan_out = {}

for module, details in data.items():
    deps = details.get('imports', [])
    fan_out[module] = len(deps)
    for dep in deps:
        fan_in[dep] = fan_in.get(dep, 0) + 1

all_modules = set(fan_in.keys()) | set(fan_out.keys())

print(f"{'Module':<35} | {'Fan In':>7} | {'Fan Out':>8}")
print("-" * 60)
for module in sorted(all_modules):
    fi = fan_in.get(module, 0)
    fo = fan_out.get(module, 0)
    print(f"{module:<35} | {fi:>7} | {fo:>8}")

with open("fan_analysis.json", "w") as f:
    json.dump({"fan-in": fan_in, "fan-out": fan_out}, f, indent=4)