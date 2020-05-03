from django.shortcuts import render, HttpResponse
import random


def arrayValues():
    ary = []
    for i in range(0, 150):
        n = random.randint(100, 600)
        ary.append(n)
    return ary


def index(request):
    global arr
    arr = arrayValues()
    return render(request, "index.html", {'arr': arr})


def mergesort(request):
    animations = getMergeSortAnimation(arr)
    return HttpResponse([animations])


def getMergeSortAnimation(arr):
    animations = []
    if len(arr) <= 1: return arr
    auxiliaryArray = arr.copy()
    mergeSortHelper(arr, 0, len(arr) - 1, auxiliaryArray, animations)
    return animations


def mergeSortHelper(mainArray, start, end, auxiliaryArray, animations):
    if start == end: return
    middle = (start + end) // 2
    mergeSortHelper(auxiliaryArray, start, middle, mainArray, animations)
    mergeSortHelper(auxiliaryArray, middle + 1, end, mainArray, animations)
    merge(mainArray, start, middle, end, auxiliaryArray, animations)


def merge(mainArray, start, middle, end, auxiliaryArray, animations):
    k = start
    i = start
    j = middle + 1
    while i <= middle and j <= end:
        animations.append([i, j])
        animations.append([i, j])
        if auxiliaryArray[i] <= auxiliaryArray[j]:
            animations.append([k, auxiliaryArray[i]])
            mainArray[k] = auxiliaryArray[i]
            k += 1
            i += 1
        else:
            animations.append([k, auxiliaryArray[j]])
            mainArray[k] = auxiliaryArray[j]
            k += 1
            j += 1

    while i <= middle:
        animations.append([i, i])
        animations.append([i, i])
        animations.append([k, auxiliaryArray[i]])
        mainArray[k] = auxiliaryArray[i]
        k += 1
        i += 1

    while j <= end:
        animations.append([j, j])
        animations.append([j, j])
        animations.append([k, auxiliaryArray[j]])
        mainArray[k] = auxiliaryArray[j]
        k += 1
        j += 1


def quicksort(request):
    animations = getQuickSortAnimations(arr)
    return HttpResponse([animations])


def getQuickSortAnimations(arr):
    animations = []
    auxiliaryArray = arr.copy()
    quickSortHelper(auxiliaryArray, 0, len(auxiliaryArray) - 1, animations)
    return animations


def quickSortHelper(auxiliaryArray, start, end, animations):
    if start < end:
        pivotIndex = partition(auxiliaryArray, start, end, animations)
        quickSortHelper(auxiliaryArray, start, pivotIndex - 1, animations)
        quickSortHelper(auxiliaryArray, pivotIndex + 1, end, animations)


def partition(auxiliaryArray, start, end, animations):
    pivot = auxiliaryArray[end]
    pivotIndex = start
    for i in range(start, end):
        animations.append([i, end])
        animations.append([i, end])
        if auxiliaryArray[i] <= pivot:
            animations.append([i, auxiliaryArray[pivotIndex]])
            animations.append([pivotIndex, auxiliaryArray[i]])
            auxiliaryArray[i], auxiliaryArray[pivotIndex] = auxiliaryArray[pivotIndex], auxiliaryArray[i]
            pivotIndex += 1
        else:
            animations.append([-1, -1])
            animations.append([-1, -1])
        animations.append([-1, -1])
        animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([pivotIndex, auxiliaryArray[end]])
    animations.append([end, auxiliaryArray[pivotIndex]])
    auxiliaryArray[pivotIndex], auxiliaryArray[end] = auxiliaryArray[end], auxiliaryArray[pivotIndex]
    return pivotIndex


def bubblesort(request):
    animations = getBubbleSortAnimations(arr)
    return HttpResponse([animations])


def getBubbleSortAnimations(arr):
    animations = []
    auxiliaryArray = arr.copy()
    bubbleSortHelper(auxiliaryArray, animations)
    return animations


def bubbleSortHelper(auxiliaryArray, animations):
    for i in range(0, len(auxiliaryArray) - 1):
        for j in range(0, len(auxiliaryArray) - 1):
            animations.append([j, j+1])
            animations.append([j, j+1])
            if auxiliaryArray[j] > auxiliaryArray[j+1]:
                animations.append([j, auxiliaryArray[j+1]])
                animations.append([j+1, auxiliaryArray[j]])
                auxiliaryArray[j], auxiliaryArray[j+1] = auxiliaryArray[j+1], auxiliaryArray[j]
            else:
                animations.append([-1, -1])
                animations.append([-1, -1])



def selectionsort(request):
    animations = getSelectionSortAnimations(arr)
    return HttpResponse([animations])


def getSelectionSortAnimations(arr):
    animations = []
    auxiliaryArray = arr.copy()
    selectionSortHelper(auxiliaryArray, animations)
    return animations


def selectionSortHelper(auxiliaryArray, animations):

    # 999 -> Comparison 1
    # 9999 -> Comparison 2
    # 99999 -> Swap

    for i in range(0, len(auxiliaryArray)):
        minIndex = i
        for j in range(i+1, len(auxiliaryArray)):
            animations.append([999, j, minIndex])
            animations.append([9999, j, minIndex])
            if auxiliaryArray[j] < auxiliaryArray[minIndex]:
                minIndex = j
        animations.append([99999, minIndex, auxiliaryArray[i]])
        animations.append([99999, i, auxiliaryArray[minIndex]])

        auxiliaryArray[minIndex], auxiliaryArray[i] = auxiliaryArray[i], auxiliaryArray[minIndex]


def insertionsort(request):
    animations = getInsertionSortAnimations(arr)
    return HttpResponse([animations])


def getInsertionSortAnimations(arr):
    animations = []
    auxiliaryArray = arr.copy()
    selectionSortHelper(auxiliaryArray, animations)
    return animations


def insertionSortHelper(auxiliaryArray, animations):

    # 999 -> comparision1
    # 9999 -> comparision2
    # 99999 -> overwrite
    for i in range(1, len(auxiliaryArray)):
        key = auxiliaryArray[i]
        j = i - 1
        animations.append([999, j, i])
        animations.append([9999, j, i])
        while j >= 0 and auxiliaryArray[j]>key:
            animations.append([99999, j + 1, auxiliaryArray[j]])
            auxiliaryArray[j + 1] = auxiliaryArray[j]
            j -= 1
            if j >= 0:
                animations.append([999, j, i])
                animations.append([9999, j, i])
        animations.append([99999, j + 1, key])
        auxiliaryArray[j + 1] = key



