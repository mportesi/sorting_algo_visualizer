class OddEvenSort:
  def __init__(self, array):
    self.array = array

  def sort(self): 
    swaps = []
    n=len(self.array)
    isSorted = 0

    while isSorted == 0: 
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2): 
            if self.array[i] > self.array[i+1]: 
                self.array[i], self.array[i+1] = self.array[i+1], self.array[i] 
                swaps.append([i,i+1])
                isSorted = 0
                  
        for i in range(0, n-1, 2): 
            if self.array[i] > self.array[i+1]: 
                self.array[i], self.array[i+1] = self.array[i+1], self.array[i] 
                swaps.append([i,i+1])
                isSorted = 0
      
    return swaps