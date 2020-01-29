#Without copy
aa=["aaa","bbb"]
bb=aa
bb.append("ccc")
print(aa)
print(bb)
#With Copy
aa=["aaa","bbb"]
bb=aa.copy()
bb.append("ccc")
print(aa)
print(bb)