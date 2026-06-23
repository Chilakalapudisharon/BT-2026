f = open("/workspaces/BT-2026/DAY 5/test_t.txt","w")
f.write("I Like working with codes")
print("filename is:", f.name)
print(f.tell())
f.close()
print(f.closed)
with open("/workspaces/BT-2026/DAY 5/test_t.txt",'r') as f:
    print(f.read())
    print(f.closed)