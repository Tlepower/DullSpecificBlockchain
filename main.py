file = open("sample.txt","r")
r = {}
count = 0
for line in file:
  line = line.strip()
  line = line.replace(".", " ").split()
  for word in line:
    if word in r:
      r[word] += 1
    else:
      r[word] = 1
file.close()
print(max(r.values()))


