# Function for finding sum of two numbers as string
def sumTwoStrings(str1, str2):

    if (len(str1) < len(str2)):
        str1, str2 = str2,str1
 
    m = len(str1)
    n = len(str2)
    ans = ""
    
    carry = 0
    
    # FIRST PART. Sums the most upright strings. The smallest string goes down.
    # str1 = 438512 +
    # str2 =    123
    #      = --------
    #           634
    for i in range(n):
 
        # Sum of current digits
        ds = ((ord(str1[m - 1 - i]) - ord('0')) +
                (ord(str2[n - 1 - i]) - ord('0')) +
                carry) % 10
 
        carry = ((ord(str1[m - 1 - i]) - ord('0')) +
                (ord(str2[n - 1 - i]) - ord('0')) +
                carry) // 10
 
        ans = str(ds) + ans
 
    # SECOND PART. Sums the left string that remain. The largest string at the top.
    # str1 = 438512 +
    # str2 =    123
    #      = --------
    #        438 634
    for i in range(n,m):
        ds = (ord(str1[m - 1 - i]) - ord('0') +
                carry) % 10
        carry = (ord(str1[m - 1 - i]) - ord('0') +
                carry) // 10
        ans = str(ds) + ans
 
    if (carry):
        ans = str(carry) + ans
    return ans


# Returns True if two substrings of given lengths of str[beg...] can cause a positive result.
def checkSumStringUtil(Str, beg, len1, len2):
    
    # Finding two substrings of given lengths and their sum
    s1 = Str[beg: beg + len1]
    s2 = Str[beg + len1: beg + len1 + len2]
    s3 = sumTwoStrings(s1, s2)

    s3_len = len(s3)

    # if number of digits s3 is greater than the available string size
    if (s3_len > len(Str) - len1 - len2 - beg):
        return False
    
    # s3 as the next number of the main string
    if (s3 == Str[beg + len1 + len2: beg + len1 + len2 + s3_len]):
        
        # If we have reached the end of the string
        if (beg + len1 + len2 + s3_len == len(Str)):
            return True
        
        # otherwise call recursively for n2, s3
        return checkSumStringUtil(Str, beg + len1, len2, s3_len)
    
    # If we don't get s3 in the main string
    return False


# Returns True if str is sum string, else False.
def isSumString(Str):
    
    n = len(Str)

    # choosing first two numbers and checking whether it is sum-string or not. 
    for i in range(1, n):
        # the sum of (i + j) must not exceed the length of str.
        for j in range(1, n - i):
            if (checkSumStringUtil(Str, 0, i, j)):
                return True
    return False

if __name__ == "__main__":
    print(isSumString("1212243660"))
    print(isSumString("12243660"))
    print(isSumString("123456787"))
            