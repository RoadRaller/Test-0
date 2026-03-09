def printlst(lst):
  for item in lst:
    print(item)
  print
  return
def airport(info):
  bport = input('Enter British Airport: ')
  if bport != 'LPL' and bport != 'BOH':
    print('wrong airport')
    return
  
  iport = input('Enter International Airport: ')
  for port in info:
    if iport in port:
      print(port)
      return
  print('not found')
  return

def flight(info):
  type = input('Enter plane Type: ')
  for item in info:
    if type == item[0]:
      printlst(item)
      fc = int(input('Number of First Class:'))
      if fc < int(item[4]):
        print('Lower then minimal')
        return
      elif fc*2 > int(item[3]):
        print('to high')
        return
      

      print(f'Capacity:{int(item[3])-fc*2}')


      return
    print('not found')
    return


#get file

def get_file(name):
  file = open(name,"r")
  lst = file.readlines()
  for i in range(len(lst)):
    lst[i] = lst[i].split(',')
    lst[i][-1] = lst[i][-1][0:-1]
  del lst[-1]
  printlst(lst)
  file.close()
  return lst

ap = get_file('airplane.txt')
fl = get_file('flights.txt')

menu = ['airport','flight','price','clear','quit']
inp = None
while inp != 'quit':
  printlst(menu)
  
  inp = input()

  if inp == 'airport':
    airport(ap)
  elif inp == 'flight':
    flight(fl)

print('end')