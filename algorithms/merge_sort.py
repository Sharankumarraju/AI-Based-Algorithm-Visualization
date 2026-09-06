def merge_sort_steps(arr):

    steps = []

    def merge_sort(left, right):

        if left >= right:
            return

        mid = (left + right) // 2

        merge_sort(left, mid)
        merge_sort(mid + 1, right)

        merge(left, mid, right)

    def merge(left, mid, right):

        temp = []

        i = left
        j = mid + 1

        while i <= mid and j <= right:

            steps.append({
                "array": arr.copy(),
                "compare": [i, j],
                "sorted": []
            })

            if arr[i] <= arr[j]:

                temp.append(arr[i])
                i += 1

            else:

                temp.append(arr[j])
                j += 1

        while i <= mid:

            temp.append(arr[i])
            i += 1

        while j <= right:

            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):

            arr[left + k] = temp[k]

            steps.append({
                "array": arr.copy(),
                "compare": [left + k],
                "sorted": []
            })

    merge_sort(0, len(arr) - 1)

    steps.append({
        "array": arr.copy(),
        "compare": [],
        "sorted": list(range(len(arr)))
    })

    return steps


if __name__ == "__main__":

    arr = [5, 3, 8, 1]

    result = merge_sort_steps(arr)

    for step in result:
        print(step)