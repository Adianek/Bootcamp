import json

lista = [1, 2, 3, 'a', 'b', 'c']
print(type(lista))

json_list = json.dumps(lista)

print(type(json_list))  # serializacja

napis = '{"1":"a","2":"b"}'

ds_napis = json.loads(napis)  # deserializacja
print(ds_napis)
print(type(ds_napis))

# print(help(json.dump))
print(help(json.load))

with open("napis.json", 'w') as fp:
    json.dump(ds_napis, fp)

with open("napis.json") as fp:
    ob = json.load(fp)
    print(ob)
    print(type(ob))
