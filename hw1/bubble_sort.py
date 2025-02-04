# pylint: skip-file
def bubbleSort(A):
    print("bubble sorted: ", end=" ")
    if len(A) == 1:
        print(A[0], end=" -> ")
        print("end")
        return A
    for i in range(len(A)):
          for j in range(0, len(A)-i-1):
               if(A[j] > A[j+1]):
                    A[j+1], A[j] = A[j], A[j+1]
    
    for num in A:
        print(num, end=" -> ")
    print("end")
    return A

print("--------Bubble Sort--------------")
bubbleSort([-100, 13, 20])  #  -100 -> 13 -> 20 -> end
bubbleSort([20])  #  20 -> end
bubbleSort([])  #  end
bubbleSort([1, 2, 3, 4, 5])  # 1 -> 2 -> 3 -> 4 -> 5 -> end
bubbleSort([1, 2, 5, 8, 10, 3, 4, 6, 7])  # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 10 -> end
bubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> end
print("----------------------------------")


          
          


