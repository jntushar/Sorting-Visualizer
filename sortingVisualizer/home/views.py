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
    return render(request, "home.html", {'arr': arr})


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



