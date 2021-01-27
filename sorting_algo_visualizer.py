import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import argparse
from BubbleSort import BubbleSort
from QuickSort import QuickSort
from HeapSort import HeapSort
from InsertionSort import InsertionSort
from SelectionSort import SelectionSort
from CocktailSort import CocktailSort
from ShellSort import ShellSort
from StoogeSort import StoogeSort
from CombSort import CombSort
from OddEvenSort import OddEvenSort
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

def videovisualize(sorter, cmap):    
    image = np.zeros((140, 120))
    for i in range(image.shape[1]):
        image[:,i] = i
    for i in range(image.shape[0]):
        np.random.shuffle(image[i,:])

    maxMoves = 0
    moves = []
    sorter_to_use = eval(str(sorter))
    for i in range(image.shape[0]):
        newMoves = []
        newMoves = sorter_to_use(list(image[i,:])).sort()
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
    newMoves = eval(str(sorter))(list(image)).sort()
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
        "-sorter", type=str, default="BubbleSort", help="sorting algorithm to use."
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






