# Definitions
def ascii(character):
  return ord(character)-64

def stringreturn(number):
  return chr(number+64)

def getupper(character):
  return character.upper()
# Input
a = input("Input Code:          ")

# Get All Uppercase
upperA=''
for i in range (0,len(a)):
  upperA += getupper(a[i])

# Reverse Third Operation
string1 = ''
halfa = int(len(upperA)/2)
for i in range(0,halfa):
  string1 += upperA[2*i+1]
  string1 += upperA[2*i]
if (len(upperA) % 2 == 1):
  string1 += upperA[2*halfa]

# Reverse Second Operation
string2 = ''
for i in range(0,len(a)):
  if (ascii(string1[i])>0 and ascii(string1[i])<27):
    temp = (ascii(string1[i])-7)
    if (temp <= 0):
      temp += 26
    string2 += stringreturn(temp)
  elif (string1[i]==' '):
    string2 += ' '
  else:
      string2 += stringreturn((ascii(string1[i])-7))
    
# Reverse First Operation
string3 = ''
for i in range (0, len(string2)):
  if (ascii(string2[i])>0 and ascii(string2[i])<27):
    temp = (ascii(string2[i]))
    if (temp % 2 == 1):
      temp +=27
    final=int(temp/2)
    string3 += stringreturn(final)
  elif (string2[i]==' '):
    string3 += ' '
  else:
    string3 += stringreturn(int(ascii(string2[i])/2-1))
  
  

# Outputs
print("Upper case:          " + upperA)
print("Reverse Third step:  " + string1)
print("Reverse Second step: " + string2)
print("Initial code:        " + string3)
