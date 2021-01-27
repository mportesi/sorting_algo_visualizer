class ShellSort:
  def __init__(self, array):
    self.array = array

    
  def sort(self): 
    swaps =[]
    n = len(self.array) 
    gap = n//2
    while gap > 0: 
        for i in range(gap,n): 
            temp = self.array[i] 
            j = i 
            while  j >= gap and self.array[j-gap] >temp: 
                self.array[j] = self.array[j-gap] 
                swaps.append([j, j-gap])
                j -= gap 
            self.array[j] = temp 
        gap //= 2
    return swaps