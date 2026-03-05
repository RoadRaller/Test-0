def printlst(lst):
  for item in lst:
    print(item)

def airport(info):
  bport = input('Enter British Airport')
  if bport != 'LPL' and bport != 'BOH':
    print('wrong airport')
    return
  
  iport = input('Enter International Airport')
  for port in info:
    if iport in port:
      print(port)
      return
  print('not found')
  return

  


#get file
info = []
file = open("airplane.txt","r")
info = file.readlines()
for i in range(len(info)):
  info[i] = info[i].split(',')
  info[i][-1] = info[i][-1][0:-1]
del info[-1]
printlst(info)




menu = ['airport','flight','price','clear','quit']
inp = None
while inp != 'quit':
  printlst(menu)
  
  inp = input()

  if inp == 'airport':
    airport(info)
  
file.close()
print('end')