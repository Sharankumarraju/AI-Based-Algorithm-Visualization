def selection_sort_steps(arr):

    steps = []

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            steps.append({
                "array": arr.copy(),
                "compare": [min_index, j],
                "sorted": list(range(i))
            })

            if arr[j] < arr[min_index]:

                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

        steps.append({
            "array": arr.copy(),
            "compare": [i, min_index],
            "sorted": list(range(i + 1))
        })

    return steps

if __name__ == "__main__":

    numbers = [5, 3, 8, 1]

    result = selection_sort_steps(numbers)

    for step in result:
        print(step)