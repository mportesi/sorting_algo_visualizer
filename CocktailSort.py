class CocktailSort:
  def __init__(self, array):
    self.array = array

  def swap(self,x, y):
        tmp = self.array[x]
        self.array[x] = self.array[y]
        self.array[y] = tmp 

  def sort(self):
    swapped = True
    swaps =[]
    while swapped:
        swapped = False
        for i in range(len(self.array)-1):
            if self.array[i] > self.array[i + 1]:
                swaps.append([i,i+1])
                self.swap(i, i+1)
                swapped = True
        if swapped == False:
            break
        for j in range(len(self.array)-2, -1,-1):
            if self.array[j] > self.array[j + 1]:
                swaps.append([j,j+1])
                self.swap(j, j+1)
                swapped = True
    return swaps