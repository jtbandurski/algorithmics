d = dict()
d["a"]=1
# print("a" in d)
# print(True+3)
# print(d["b"]+4)
# print(d.get("b",0))
# print(d.get("a",0))

e=dict()
e["a"] = [1,2]
e["c"]=[0,0]
e["a"][0] = 2
print(e["a"])
print(e.get("b",[0])[0])
print(e.values())
print(2 in [x[0] for x in e.values()])