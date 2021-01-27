class SelectionSort:
  def __init__(self, array):
    self.array = array

  def swap(self,x, y):
        tmp = self.array[x]
        self.array[x] = self.array[y]
        self.array[y] = tmp 

  def sort(self):
    swaps = []
    for i in range(len(self.array)):
        jMin = i
        for j in range(i+1,len(self.array)):
            if self.array[j]<self.array[jMin]:
                jMin = j
        if jMin != i:
            swaps.append([i, jMin])
            self.swap(i, jMin)
    return swaps