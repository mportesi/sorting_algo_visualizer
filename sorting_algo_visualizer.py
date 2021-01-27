import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import argparse

##### todo #####
#implements other algo
#clean up code
#give possibility so specify dpi, framerate, size of output

##### IMPLEMENTED ALGO #####
#BUBBLE
#QUICK
#HEAP
#INSERTION
#SELECTION
#COCKTAIL
#SHELL
#STOOGE
#COMB
#ODDEVEN
#MERGE


def bubblesort(A):    
    swaps = []
    for i in range(len(A)):
        for k in range(len(A) - 1, i, -1):
            if (A[k] < A[k - 1]):
                swaps.append([k, k - 1])
                tmp = A[k]
                A[k] = A[k - 1]
                A[k - 1] = tmp
    return swaps


def partition(array, begin, end):
    pivot = begin
    swaps = []
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
            swaps.append([i, pivot])
    array[pivot], array[begin] = array[begin], array[pivot]
    swaps.append([pivot, begin])
    return pivot, swaps

def quicksort(array, begin=0, end=None):    
    global swaps
    swaps = []
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        global swaps
        if begin >= end:
            return
        pivot, newSwaps = partition(array, begin, end)
        swaps += newSwaps
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)
    _quicksort(array, begin, end)
    return swaps


def heapsort( aList ):
    global swaps
    swaps = []
    # convert aList to heap
    length = len( aList ) - 1
    leastParent = length // 2
    for i in range ( leastParent, -1, -1 ):
        moveDown( aList, i, length )

    # flatten heap into sorted array
    for i in range ( length, 0, -1 ):
        if aList[0] > aList[i]:
            swaps.append([0, i])
            swap( aList, 0, i )
            moveDown( aList, 0, i - 1 )
    return swaps

def moveDown( aList, first, last ):
    global swaps
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
            largest += 1

        # right child is larger than parent
        if aList[largest] > aList[first]:
            swaps.append([largest, first])
            swap( aList, largest, first )
            # move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return # force exit


def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def insertionsort(A):
    swaps = []
    for i in range(1,len(A)):
        j=i
        while j > 0 and A[j-1] > A[j]:
            swap(A, j, j-1)
            swaps.append([j, j - 1])
            j = j-1
    return swaps


def selectionsort(A):
    swaps = []
    for i in range(len(A)):
        jMin = i
        for j in range(i+1,len(A)):
            if A[j]<A[jMin]:
                jMin = j
        if jMin != i:
            swaps.append([i, jMin])
            swap(A, i, jMin)
    return swaps


def cocktailsort(A):
    swapped = True
    swaps =[]
    while swapped:
        swapped = False
        for i in range(len(A)-1):
            if A[i] > A[i + 1]:
                swaps.append([i,i+1])
                swap(A, i, i+1)
                swapped = True
        if swapped == False:
            break
        for j in range(len(A)-2, -1,-1):
            if A[j] > A[j + 1]:
                swaps.append([j,j+1])
                swap(A, j, j+1)
                swapped = True
    return swaps


def shellsort(A): 
    swaps =[]
    n = len(A) 
    gap = n//2
    while gap > 0: 
        for i in range(gap,n): 
            temp = A[i] 
            j = i 
            while  j >= gap and A[j-gap] >temp: 
                A[j] = A[j-gap] 
                swaps.append([j, j-gap])
                j -= gap 
            A[j] = temp 
            
        gap //= 2
    return swaps


def stoogesort(A, begin=0, end=None):
    global swaps
    swaps = []
    if end is None:
        end = len(A) - 1

    def _stoogesort(A, begin, end):
        global swaps
        if begin >= end: 
            return
        
        if A[begin]>A[end]: 
            t = A[begin] 
            A[begin] = A[end] 
            A[end] = t 
            swaps.append([begin, end])
    
        if end-begin+1 > 2: 
            t = (int)((end-begin+1)/3) 
    
            #first 2/3 elements 
            _stoogesort(A, begin, (end-t)) 
    
            #last 2/3 elements 
            _stoogesort(A, begin+t, (end)) 
    
            #2/3 elements 
            _stoogesort(A, begin, (end-t))
    _stoogesort(A, begin, end)
    return swaps

def combsort(data):
    length = len(data)
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
            if data[i] > data[sm]:
                data[i], data[sm] = data[sm], data[i]
                swaps.append([i,sm])
                sorted = False

    return swaps

def oddevensort(arr): 
    swaps = []
    n=len(arr)
    isSorted = 0

    while isSorted == 0: 
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2): 
            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i] 
                swaps.append([i,i+1])
                isSorted = 0
                  
        for i in range(0, n-1, 2): 
            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i] 
                swaps.append([i,i+1])
                isSorted = 0
      
    return swaps


#in-place
def mergesort(A):
    global swaps
    swaps = []

    def _merge(arr, start, mid, end):
        global swaps
        start2 = mid + 1; 

        if (arr[mid] <= arr[start2]): 
            return; 

        while (start <= mid and start2 <= end): 

            if (arr[start] <= arr[start2]): 
                start += 1; 
            else: 
                value = arr[start2]; 
                index = start2; 

                while (index != start): 
                    arr[index] = arr[index - 1]; 
                    swaps.append([index,index-1])
                    index -= 1; 

                #swaps.append([start2, start])
                arr[start] = value; 

                start += 1; 
                mid += 1; 
                start2 += 1; 

    def _mergeSort(arr, l, r): 
        global swaps
        if (l < r): 
    
            # Same as (l + r) / 2, but avoids overflow 
            # for large l and r 
            m = l + (r - l) // 2; 
    
            # Sort first and second halves 
            _mergeSort(arr, l, m); 
            _mergeSort(arr, m + 1, r); 
    
            _merge(arr, l, m, r); 
    _mergeSort(A, 0, len(A)-1)
    return swaps


def videovisualize(sorter, cmap):    
    image = np.zeros((140, 120))
    for i in range(image.shape[1]):
        image[:,i] = i
    for i in range(image.shape[0]):
        np.random.shuffle(image[i,:])

    maxMoves = 0
    moves = []
    sorter_to_use = eval(str(sorter)+'sort')
    for i in range(image.shape[0]):
        newMoves = []
        newMoves = sorter_to_use(list(image[i,:]))
        if len(newMoves) > maxMoves:
            maxMoves = len(newMoves)
        moves.append(newMoves)

    def swap_pixels(row, places):
        tmp = image[row,places[0]].copy()
        image[row,places[0]] = image[row,places[1]]
        image[row,places[1]] = tmp

    currentMove = 0
    imagelist=[]
    fig = plt.figure(dpi=400, constrained_layout = True)
    fig.patch.set_facecolor('black')    
    fig.set_size_inches(4.8, 4.8)  #custom
    plt.axis("off")

    movie_image_step = maxMoves // 140    
    if movie_image_step == 0:
        movie_image_step = 1
    
    #unsorted image at start
    for i in range(20):
        imagelist.append((plt.imshow(image, cmap=cmap),))

    while currentMove < maxMoves:
        for i in range(image.shape[0]):
            if currentMove < len(moves[i]):
                swap_pixels(i, moves[i][currentMove])

        if currentMove % movie_image_step == 0:
            imagelist.append((plt.imshow(image, cmap=cmap),))
        currentMove += 1

    #sorted image at end
    for i in range(20):
        imagelist.append((plt.imshow(image, cmap=cmap),))
    
    im_ani = animation.ArtistAnimation(
        fig, imagelist, interval=60, repeat_delay=3000, blit=True
    )    
    
    os.makedirs('output/video', exist_ok=True)
    im_ani.save(('output/video/sample-'+str(sorter)+'-'+str(movie_image_step)+str(cmap)+ ".gif"))


def imagevisualize(sorter, order, cmap):
    image = get_list_for_image(order)
    newMoves = []
    sorter_to_use = eval(str(sorter)+'sort')
    newMoves = sorter_to_use(list(image))
    newimage=image
    temp = len(newMoves) // 700
    if temp ==0:
        temp=1
    
    imagelist=[]
    fig = plt.figure(dpi=200)
    fig.patch.set_facecolor('black')    
    plt.axis("off")

    def swap_pixels(places):
        tmp = image[places[0]].copy()
        image[places[0]] = image[places[1]]
        image[places[1]] = tmp

    for i in range(len(newMoves)):
        swap_pixels(newMoves[i])
        if i % temp == 0:
            newimage=np.vstack([newimage,image])

    for x in range(10):
        newimage=np.vstack([newimage,image])

    plt.imshow(newimage,cmap=cmap)
    os.makedirs('output/image', exist_ok=True)
    plt.imsave('output/image/sample-'+str(sorter)+'-'+str(order)+'-'+str(temp)+str(cmap)+ ".png",newimage, dpi=1200, cmap=cmap)


def get_list_for_image(order):
    image = np.zeros((300))
    if order =='random':
        for i in range(image.shape[0]):
            image[i] = i
        np.random.shuffle(image[:])
    if order == 'reverse':
        j=image.shape[0]-1
        for i in range(image.shape[0]):
            image[i] = j
            j-=1
    if order =='interleave':
        x = 0
        y = image.shape[0]-1
        for i in range(image.shape[0]):
            if i%2 == 0:
                image[i] = x
                x+=1
            else:
                image[i]=y
                y-=1
    if order =='swappedhalf':
        x=image.shape[0]//2
        for i in range(image.shape[0]//2):
            image[i]=x
            x+=1
        x=0
        for i in range(image.shape[0]//2, image.shape[0]):
            image[i]=x
            x+=1
    if order =='interleavehalf':
        x = 0
        y = image.shape[0]-1
        for i in range(image.shape[0]):
            if i%2 == 0:
                image[x] = i
                x+=1
            else:
                image[y]=i
                y-=1
    return image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sorting Algorithms Visualizer. By default, produce a bubblesort visualization"
    )
    parser.add_argument(
        "-sorter", type=str, default="bubble", help="sorting algorithm to use."
    )
    parser.add_argument(
        "-out", type=str, default="video", help="Type of output to produce, -o video or -o image"
    )
    parser.add_argument(
        "-order", type=str, default="random", help="Starting order of the list. Default to random."
    )
    parser.add_argument(
        "-c", type=str, default="viridis", help="matplotlib colormap."
    )
    args = parser.parse_args()
    if args.out == 'video':
        videovisualize(sorter=args.sorter, cmap=args.c)
    elif args.out =='image':
        imagevisualize(sorter=args.sorter, order=args.order,cmap=args.c)
    else:
        videovisualize(args.sorter)






