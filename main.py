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
for key in list(r.keys()):
  if r[key] == max(r.values()):
    print(key, r[key])

