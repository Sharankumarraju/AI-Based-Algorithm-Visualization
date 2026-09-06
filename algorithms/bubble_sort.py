def bubble_sort_steps(arr):

    steps = []

    n = len(arr)

    for i in range(n):

        for j in range(n - i - 1):

            steps.append({
                "array": arr.copy(),
                "compare": [j, j + 1],
                "sorted": list(range(n - i, n))
            })

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                steps.append({
                    "array": arr.copy(),
                    "compare": [j, j + 1],
                    "sorted": list(range(n - i, n))
                })

    steps.append({
        "array": arr.copy(),
        "compare": [],
        "sorted": list(range(n))
    })

    return steps


if __name__ == "__main__":

    numbers = [5, 3, 8, 1]

    result = bubble_sort_steps(numbers)

    for step in result:
        print(step)