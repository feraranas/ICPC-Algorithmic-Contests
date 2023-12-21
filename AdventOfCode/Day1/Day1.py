# combination of alphanumeric numbers
def getFirstLastAlphaNumeric(max_sum, line):
     numbers = {'1': "one",
                '2': "two",
                '3': "three",
                '4': "four",
                '5': "five",
                '6': "six",
                '7': "seven",
                '8': "eight",
                '9': "nine", 
                '10': "ten"}
     
     fn = ''
     ln = ''
     i = 0
     j = len(line) - 1

     while (i < len(line)):
          if line[i].isnumeric():
               fn += line[i]
               break
          
          t =  next(((k,v) for k,v in numbers.items() if line[i:].startswith(v)), None)
          
          if t != None:
               fn += t[0]
               i += len(t[1])
               break
          i += 1
     
     while (j >= i):
          if line[j].isnumeric():
               ln += line[j]
               n = fn + ln
               max_sum += int(n)
               break

          t =  next(((k,v) for k,v in numbers.items() if line[j - len(v) + 1:].startswith(v)), None)
          
          if t != None:
               ln += t[0]
               n = fn + ln
               max_sum += int(n)
               break

          j -= 1

     return fn, ln, max_sum

# only numerical integer numbers
def getFirstLastNumeric(max_sum, line):
     fn = ''
     ln = ''
     i = 0
     j = len(line) - 1

     while (i < len(line)):
          if line[i].isnumeric():
               fn += line[i]
               break
          i += 1
               
     while (j >= i):
          if line[j].isnumeric():
               ln += line[j]
               n = fn + ln
               max_sum += int(n)
               break
          j -= 1

     return fn, ln, max_sum


if __name__ == '__main__':
     max_sum = 0

     with open('document.txt', 'r') as file:
          for index, line in enumerate(file):
               # fn, ln, max_sum = getFirstLastNumeric(max_sum, line)
               fn, ln, max_sum = getFirstLastAlphaNumeric(max_sum, line)
               print("index: ", index, end=" ")
               print("fn: ", fn, ", ", end=" ")
               print("ln: ", ln, end="\n")
               
     print(max_sum)