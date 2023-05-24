import yaml
import sys

if len(sys.argv) != 4:
    print("You must provide the following arguments: input filename, annotation key, annotation value")
    print(sys.argv)
    exit(1)

filename = sys.argv[1]
key = sys.argv[2]
value = sys.argv[3]
print('Setting annotation "', key, ": ", value)

with open(filename, 'r') as file:
    document = yaml.safe_load(file)
    if not ("annotations" in document["metadata"]):
        document["metadata"]["annotations"] = {}
    document["metadata"]["annotations"][key] = value

    print(yaml.dump(document))