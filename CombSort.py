class CombSort:
  def __init__(self, array):
    self.array = array

  def sort(self):
    length = len(self.array)
    shrink = 1.3
    _gap = length
    sorted = False
    swaps = []

    while not sorted:
        _gap /= shrink
        gap = int(_gap)
        if gap <= 1:
            sorted = True
            gap = 1
        
        for i in range(length - gap):
            sm = gap + i
            if self.array[i] > self.array[sm]:
                self.array[i], self.array[sm] = self.array[sm], self.array[i]
                swaps.append([i,sm])
                sorted = False

    return swaps