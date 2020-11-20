''' Given two strings, check if one is permutation of the other'''
''' The Time Complexity of this is O(nlogn) cuz we are sorting the strings and space complexity is O(1) as we are not using any additional data structure. '''

isPermutation1 = "Dog"
isPermutation2 = "God"

notPermutation1 = "Car"
notPermutation2 = "rax"

def checkPermutaion(string1, string2):
  string1 = string1.lower()
  string2 = string2.lower()

  string1 = ''.join(sorted(string1))
  string2 = ''.join(sorted(string2))

  if(len(string1) != len(string2)):
    return False

  for i in range(len(string1)):
    if(string1[i] != string2[i]):
      return False
  return True

if __name__ == "__main__":
  print(checkPermutaion(isPermutation1, isPermutation2))
  print(checkPermutaion(notPermutation1, notPermutation2))