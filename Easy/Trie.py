from collections import defaultdict

class Trie:
    def __init__(self):
        self.d = defaultdict(dict)
        self.last = False
        self.count = 0
 
        
def insert(val,obj):
    cur = obj
    for i in val:
        if i not in cur.d:
            cur.d[i] = Trie()
        cur = cur.d[i]
        cur.count += 1
    cur.last = True

    
      
def search(val,obj):
    cur = obj 
    for i in val:
        if i not in cur.d:
            return 0
        cur = cur.d[i]
        
    return cur.count
    
      
obj = Trie()

last = obj.last
d = obj.d 
            

n = int(input())
for i in range(n):
    k = input()
    insert(k,obj)

tar = input()
print(search(tar,obj))
