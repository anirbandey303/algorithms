''' check weather given string has a possible permutation which is a palindrome '''

isPalindrome = "taco caT"
notPalindrome = "no posssible permutation of this string is a palindrome"

'''approach:
count of every letter in a palindrome string is 'even' with atmost 1 letter with 'odd' count"

will use a hashtable to count occurances of each letter and then check to satisfy our condition
'''

def normalize(string):
  string = string.replace(" ","")
  string = string.lower()
  return string

def addLettersToDictionary(string):
  letterCount = dict()
  for letter in string:
    if(letter in letterCount):
      letterCount[letter] += 1
    else:
      letterCount[letter] = 1
  return letterCount

def chekPermutationForPalindrome(string):
  string = normalize(string)
  letterCount = addLettersToDictionary(string)

  oddNumbers = 0
  for counts in letterCount.values():
    if(counts%2 != 0):
      oddNumbers += 1

  if(oddNumbers > 1):
    return False
  else:
    return True

if __name__ == "__main__":
  print(chekPermutationForPalindrome(isPalindrome))
  print(chekPermutationForPalindrome(notPalindrome))