class HeapSort:
  def __init__(self, array):
    self.array = array

  def swap(self,x, y):
        tmp = self.array[x]
        self.array[x] = self.array[y]
        self.array[y] = tmp 
  def moveDown(self, first, last ):
    global swaps
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if ( largest < last ) and (self.array[largest] < self.array[largest + 1] ):
            largest += 1

        # right child is larger than parent
        if self.array[largest] > self.array[first]:
            swaps.append([largest, first])
            self.swap(largest, first)
            # move down to largest child
            first = largest
            largest = 2 * first + 1
        else:
            return # force exit
            
  def sort(self):
    global swaps
    swaps = []
    # convert aList to heap
    length = len(self.array ) - 1
    leastParent = length // 2
    for i in range ( leastParent, -1, -1 ):
        self.moveDown(i, length )

    # flatten heap into sorted array
    for i in range ( length, 0, -1 ):
        if self.array[0] > self.array[i]:
            swaps.append([0, i])
            self.swap(0, i )
            self.moveDown(0, i - 1 )
    return swaps