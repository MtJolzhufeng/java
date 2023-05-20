import yaml



# with open("youconfig.yaml", 'r') as stream:
#   data = yaml.safe_load(stream)
# keys = []
# def find_keys(data):
#   if isinstance(data, dict):
#     for key, value in data.items():
#       keys.append(key)
#       find_keys(value)
#   elif isinstance(data, (list, tuple)):
#     for item in data:
#       find_keys(item)
# find_keys(data)
# print(keys)

with open("youconfig.yaml", 'r') as stream:
    data = yaml.safe_load(stream)
    key, value = list(data['artifacts'].items())[0]
print(key)