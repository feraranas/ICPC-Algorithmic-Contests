def toString(List):
     s = ""
     for x in List:
          if x == '&# 092;&# 048;':
               break
          s += x
     return s


# Function recursively prints the strings having space pattern.
# i and j are indices in 'str[]' and 'buff[]', respectively.
def printPatternUtil(string, buff, i, j, str_len):
     
     if i == str_len:
          buff[j] = '&# 092;&# 048;'
          print(toString(buff))
          return
     
     # Either put the character
     buff[j] = string[i]

     printPatternUtil(string, buff, i + 1, j + 1, str_len)

     # Or put a space followed by next character
     buff[j] = ''
     buff[j + 1] = string[i]

     printPatternUtil(string, buff, i + 1, j + 2, str_len)


# This function creates buff[] to store individual output string
# and uses printPatternUtil() to print all the permutations.
def printPattern(string):
     
     str_len = len(string)

     # Buffer to hold the string containing spaces
     buff = [0] * (2 * str_len)

     # Copy the first character as it is, since it 
     # will alway be at the first position
     buff[0] = string[0]

     printPatternUtil(string, buff, 1, 1, str_len)


if __name__ == '__main__':
     string = "ABCD"
     printPattern(string)