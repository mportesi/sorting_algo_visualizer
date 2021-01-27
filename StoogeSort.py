class StoogeSort:
  def __init__(self, array):
    self.array = array

  def sort(self, begin=0, end=None):
    global swaps
    swaps = []
    if end is None:
        end = len(self.array) - 1

    def _stoogesort(begin, end):
        global swaps
        if begin >= end: 
            return
        
        if self.array[begin]>self.array[end]: 
            t = self.array[begin] 
            self.array[begin] = self.array[end] 
            self.array[end] = t 
            swaps.append([begin, end])
    
        if end-begin+1 > 2: 
            t = (int)((end-begin+1)/3) 
    
            #first 2/3 elements 
            _stoogesort(begin, (end-t)) 
    
            #last 2/3 elements 
            _stoogesort(begin+t, (end)) 
    
            #2/3 elements 
            _stoogesort(begin, (end-t))
    _stoogesort(begin, end)
    return swaps