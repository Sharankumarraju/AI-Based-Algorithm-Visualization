def binary_search_steps(arr, target):

    steps = []

    left = 0
    right = len(arr) - 1


    while left <= right:


        mid = (left + right) // 2


        steps.append({

            "array": arr.copy(),

            "compare": [mid],

            "sorted": [],

            "found": False,

            "left": left,

            "right": right,

            "mid": mid,

            "target": target,

            "result": None

        })


        if arr[mid] == target:


            steps.append({

                "array": arr.copy(),

                "compare": [],

                "sorted": [mid],

                "found": True,

                "left": left,

                "right": right,

                "mid": mid,

                "target": target,

                "result": mid

            })


            return steps



        elif arr[mid] < target:


            left = mid + 1


        else:


            right = mid - 1



    steps.append({

        "array": arr.copy(),

        "compare": [],

        "sorted": [],

        "found": False,

        "left": left,

        "right": right,

        "mid": None,

        "target": target,

        "result": -1

    })


    return steps



if __name__ == "__main__":


    arr = [1,3,5,8,9]


    result = binary_search_steps(arr,8)


    for step in result:

        print(step)