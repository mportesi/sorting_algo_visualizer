class InsertionSort:
  def __init__(self, array):
    self.array = array

  def swap(self,x, y):
        tmp = self.array[x]
        self.array[x] = self.array[y]
        self.array[y] = tmp 

  def sort(self):
    swaps = []
    for i in range(1,len(self.array)):
        j=i
        while j > 0 and self.array[j-1] > self.array[j]:
            self.swap(j, j-1)
            swaps.append([j, j - 1])
            j = j-1
    return swaps