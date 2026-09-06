def linear_search_steps(arr, target):

    steps = []

    for i in range(len(arr)):

        steps.append({

            "array": arr.copy(),

            "compare": [i],

            "sorted": [],

            "found": False,

            "target": target,

            "result": None
        })


        if arr[i] == target:

            steps.append({

                "array": arr.copy(),

                "compare": [],

                "sorted": [i],

                "found": True,

                "target": target,

                "result": i
            })

            return steps


    steps.append({

        "array": arr.copy(),

        "compare": [],

        "sorted": [],

        "found": False,

        "target": target,

        "result": -1
    })


    return steps



if __name__ == "__main__":

    arr = [5,3,8,1]

    result = linear_search_steps(arr,8)

    for step in result:

        print(step)