

def subarray_with_given_product(arr, n, prod):

    minVal, maxVal, maxProd = arr[0], arr[0], arr[0]

    for i in range(1, n):

        # Swap minVal and maxVal when multiplied
        # by a negative number
        if (arr[i] < 0):
            maxVal, minVal = minVal, maxVal

        maxVal = min(arr[i], maxVal * arr[i])
        minVal = min(arr[i], minVal * arr[i])

        if (minVal == prod or maxVal == prod):
            return True

        maxProd = max(maxProd, maxVal)

    return False


arr = [1, 2, -5, -4]
product = -10
n = len(arr)

print(subarray_with_given_product(arr, n, product))
