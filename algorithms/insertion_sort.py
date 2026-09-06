def insertion_sort_steps(arr):

    steps = []

    n = len(arr)

    for i in range(1, n):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            steps.append({
                "array": arr.copy(),
                "compare": [j, j + 1],
                "sorted": list(range(i))
            })

            arr[j + 1] = arr[j]

            steps.append({
                "array": arr.copy(),
                "compare": [j, j + 1],
                "sorted": list(range(i))
            })

            j -= 1

        arr[j + 1] = key

        steps.append({
            "array": arr.copy(),
            "compare": [j + 1],
            "sorted": list(range(i + 1))
        })

    return steps

if __name__ == "__main__":

    numbers = [5, 3, 8, 1]

    result = insertion_sort_steps(numbers)

    for step in result:
        print(step)