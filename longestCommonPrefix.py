class Soluton(object):
  
  def LCP(self, strs):

    if strs == []:  # if array is empty, return an empty string
      return ""
    
    currPrefix = strs[0] # intialize the current prefix as the first string in the array
    i = 1
    
    for i in range(len(strs)): 
      while not strs[i].startswith(currPrefix):  # while the next string in comparison does not begin with the current prefix
        currPrefix = currPrefix[:-1]  # remove one char from the end of the current prefix until it begins with the string
        
        if not currPrefix:  # if the current prefix becomes empty (no common prefix), return an empty string
          return ""

    return currPrefix

      
