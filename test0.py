def printlst(lst):
  for item in lst:
    print(item)

menu = ['airport','flight','price','clear','quit']

info = []
txt = open("airport.txt","r")
info = readlines(txt)
for i in range(len(info)):
  info[0] = info[0].split(',')
print(info)
inp = None
while inp != 'quit':
  printlst(menu)

  inp = input()

  
  
print('end')