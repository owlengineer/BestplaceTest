import numpy as np


def find_missing(arr: list):
    i = 1
    arr_sum = 0
    full_sum = 0
    # O(N) complexity, no memory overload
    for num in arr:
        arr_sum += num
        full_sum += i
        i += 1
    full_sum += i
    return full_sum - arr_sum


def create_array(n: int):
    res = np.random.permutation(np.arange(1, n))
    res = np.delete(res, n-2)
    return res


if __name__ == '__main__':
    arr = create_array(7)
    print(f"Splitted: {arr}")
    print(find_missing(arr))