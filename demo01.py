#字典 键值对 key:value
hdict = {
    "name":"张三",
    "high":"173cm",
    "key":"value",
    "dict1":{
        "name2":"李四"
    }
}

print(hdict["name"])
value1 = hdict.get("name")#get就是通过key取值
print(value1)
value2 = hdict.pop("name")#取走
print(hdict)
del hdict["dict1"]#删除
print(hdict)