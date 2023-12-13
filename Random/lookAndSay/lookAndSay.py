def lookAndSay(n):
     
     string = "1"
     
     for _ in range(0, n):
          c = 1
          str_tmp = ""

          for j in range(0, len(string)):

               d = ord(string[j]) - ord('0')

               if j == (len(string) - 1):
                    str_tmp = str_tmp + str(c) + str(d)
                    print(str_tmp)
                    string = str_tmp
                    break
               elif not (ord(string[j + 1]) - ord('0')) == d:
                    str_tmp = str_tmp + str(c) + str(d)
                    c = 1
               elif (ord(string[j + 1]) - ord('0')) == d:
                    c += 1

               
lookAndSay(5)
# 11
# 21
# 1211
# 111221
# 312211