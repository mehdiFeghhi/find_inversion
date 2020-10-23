def partition(arr, size):

    lower = []
    higher = []
    result_list = []
    for j in range(1, size):

            if arr[0][1] < arr[j][1]:
                higher.append(arr[j])
            else:
                lower.append(arr[j])

                for x in higher:
                    result_list.append((x[0],arr[j][0]))

                result_list.append((arr[0][0] , arr[j][0]))


    return [result_list, lower, higher]


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def arr_is_ascending(arr,size):

    for j in range(size):

        if arr[j][1] > arr[j+1][1]:
            return False
    return True

def inversion(arr):
        print(arr)
        size = len(arr)

        if size == 1 or size == 0:
            return []

        if not arr_is_ascending(arr,size):


            if size == 2 :
                pi = partition(arr, size)
                return pi[0]


            pi = partition(arr,size)
            # Separately sort elements before
            # partition and after partition
            result_left  = inversion(pi[1])
            result_right = inversion(pi[2])
            print("x")
            print(pi)
            print(result_left)
            print(result_right)
            return result_left + pi[0] + result_right

def main():

    list_input = list(map(int, input().split()))

    work_list = []
    k = 0
    for j in list_input:
        work_list.append([k, j])
        k += 1
    find_inv = inversion(work_list)

    print(find_inv)

if __name__ == '__main__':
    main()


