# Definitions
def ascii(character):
  return ord(character)-64

def stringreturn(number):
  return chr(number+64)

def getupper(character):
  return character.upper()
  
# Input
a = input("Input Code:  ")

# Get Uppercase
uppera = ''
for i in range (0,len(a)):
  uppera += getupper(a[i])

# First Function
firststr = ''
for i in range (0, len(uppera)):
  if (ascii(uppera[i])>0 and ascii(uppera[i])<27):
    f = 2*(ascii(uppera[i]))
    if (f > 26):
      f -= 27
    firststr += stringreturn(f)
  elif (uppera[i]==' '):
    firststr += ' '
  else:
    firststr += stringreturn(2*(ascii(uppera[i]))+1)
# Second Function
secondstr = ''
for i in range(0,len(uppera)):
  if (ascii(firststr[i])>0 and ascii(firststr[i])<27):
    f = (ascii(firststr[i])+7)
    if (f > 26):
      f -= 26
    secondstr += stringreturn(f)
  elif (firststr[i]==' '):
    secondstr += ' '
  else:
    secondstr += stringreturn((ascii(firststr[i])+7))

# Third Function
thirdstr = ''
f = int(len(a)/2)
for i in range(0,f):
  thirdstr += secondstr[2*i+1]
  thirdstr += secondstr[2*i]
if (len(a) % 2 == 1):
  thirdstr += secondstr[2*f]

# Output
print("Upper case:  " + uppera)
print("First step:  " + firststr)
print("Second step: " + secondstr)
print("Final code:  " + thirdstr)
    
    



