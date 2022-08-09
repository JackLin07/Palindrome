def StringChallenge(strParam):
  s = strParam.lower() # first we lowercase all characters
  #''.join strings by removing spaces
  # while .isalnum() checks if all characters are alphabets and numbers
  s = ''.join(i for i in s if i.isalnum()) 
  # check the original string with the backwards string
  return s == s[::-1]

# Driver
if __name__ == "__main__"":
  print(StringChallenge(input()))
