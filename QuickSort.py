class QuickSort:
  def __init__(self, array):
    self.array = array

  def partition(self, begin, end):
      pivot = begin
      swaps = []
      for i in range(begin + 1, end + 1):
          if self.array[i] <= self.array[begin]:
              pivot += 1
              self.array[i], self.array[pivot] = self.array[pivot], self.array[i]
              swaps.append([i, pivot])
      self.array[pivot], self.array[begin] = self.array[begin], self.array[pivot]
      swaps.append([pivot, begin])
      return pivot, swaps

  def sort(self,begin=0, end=None):    
      global swaps
      swaps = []
      if end is None:
          end = len(self.array) - 1

      def _quicksort(begin, end):
          global swaps
          if begin >= end:
              return
          pivot, newSwaps = self.partition(begin, end)
          swaps += newSwaps
          _quicksort(begin, pivot - 1)
          _quicksort(pivot + 1, end)
      _quicksort(begin, end)
      return swaps





