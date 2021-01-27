class BubbleSort:
  def __init__(self, array):
    self.array = array

  def sort(self):    
    swaps = []
    for i in range(len(self.array)):
        for k in range(len(self.array) - 1, i, -1):
            if (self.array[k] < self.array[k - 1]):
                swaps.append([k, k - 1])
                tmp = self.array[k]
                self.array[k] = self.array[k - 1]
                self.array[k - 1] = tmp
    return swaps
