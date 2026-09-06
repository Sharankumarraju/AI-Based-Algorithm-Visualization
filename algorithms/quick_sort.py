def quick_sort_steps(arr):

    steps = []

    def partition(low, high):

        pivot = arr[high]

        i = low - 1

        for j in range(low, high):

            steps.append({
                "array": arr.copy(),
                "compare": [j, high],
                "sorted": []
            })

            if arr[j] < pivot:

                i += 1

                arr[i], arr[j] = arr[j], arr[i]

                steps.append({
                    "array": arr.copy(),
                    "compare": [i, j],
                    "sorted": []
                })

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        steps.append({
            "array": arr.copy(),
            "compare": [i + 1, high],
            "sorted": []
        })

        return i + 1

    def quick_sort(low, high):

        if low < high:

            pivot_index = partition(low, high)

            quick_sort(low, pivot_index - 1)

            quick_sort(pivot_index + 1, high)

    quick_sort(0, len(arr) - 1)

    steps.append({
        "array": arr.copy(),
        "compare": [],
        "sorted": list(range(len(arr)))
    })

    return steps


if __name__ == "__main__":

    arr = [5, 3, 8, 1]

    result = quick_sort_steps(arr)

    for step in result:
        print(step)