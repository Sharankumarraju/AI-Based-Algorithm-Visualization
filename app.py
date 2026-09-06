from flask import Flask, render_template, request

from algorithms.bubble_sort import bubble_sort_steps
from algorithms.selection_sort import selection_sort_steps
from algorithms.insertion_sort import insertion_sort_steps
from algorithms.merge_sort import merge_sort_steps
from algorithms.quick_sort import quick_sort_steps
from algorithms.linear_search import linear_search_steps
from algorithms.binary_search import binary_search_steps
from google import genai
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/compare")
def compare():

    return render_template("compare.html")

@app.route("/compare_visualize", methods=["POST"])
def compare_visualize():

    algo1 = request.form["algo1"]
    algo2 = request.form["algo2"]

    numbers = request.form["numbers"]
    arr = list(map(int, numbers.split()))

    target = request.form.get("target")

    if target is not None and target != "":
        target = int(target)

    def get_algorithm_steps(algo, array):

        if algo == "bubble":
            return "Bubble Sort", bubble_sort_steps(array)

        elif algo == "selection":
            return "Selection Sort", selection_sort_steps(array)

        elif algo == "insertion":
            return "Insertion Sort", insertion_sort_steps(array)

        elif algo == "merge":
            return "Merge Sort", merge_sort_steps(array)

        elif algo == "quick":
            return "Quick Sort", quick_sort_steps(array)

        elif algo == "linear":
            return "Linear Search", linear_search_steps(array, target)

        elif algo == "binary":

            array.sort()

            return "Binary Search", binary_search_steps(array, target)

    algorithm1, steps1 = get_algorithm_steps(algo1, arr.copy())
    algorithm2, steps2 = get_algorithm_steps(algo2, arr.copy())

    return render_template(
        "compare_result.html",
        algorithm1=algorithm1,
        algorithm2=algorithm2,
        steps1=steps1,
        steps2=steps2
    )


@app.route("/visualize", methods=["POST"])
def visualize():

    algorithm = request.form["algorithm"]

    numbers = request.form["numbers"]

    arr = list(map(int, numbers.split()))

    if algorithm == "bubble":

        steps = bubble_sort_steps(arr)

        return render_template(
            "result.html",
            steps=steps,
            algorithm_name="Bubble Sort",
            algorithm_type="sort",
            best_case="O(n)",
            average_case="O(n²)",
            worst_case="O(n²)",
            space_complexity="O(1)"
        )

    elif algorithm == "selection":

        steps = selection_sort_steps(arr)

        return render_template(
            "result.html",
            steps=steps,
            algorithm_name="Selection Sort",
            algorithm_type="sort",
            best_case="O(n²)",
            average_case="O(n²)",
            worst_case="O(n²)",
            space_complexity="O(1)"
        )
    
    elif algorithm == "insertion":

        steps = insertion_sort_steps(arr)

        return render_template(
            "result.html",
            steps=steps,
            algorithm_name="Insertion Sort",
            algorithm_type="sort",
            best_case="O(n)",
            average_case="O(n²)",
            worst_case="O(n²)",
            space_complexity="O(1)"
        )
    
    elif algorithm == "merge":

        steps = merge_sort_steps(arr)

        return render_template(
            "result.html",
            steps=steps,
            algorithm_name="Merge Sort",
            algorithm_type="sort",
            best_case="O(n log n)",
            average_case="O(n log n)",
            worst_case="O(n log n)",
            space_complexity="O(n)"
        )
    
    elif algorithm == "quick":

        steps = quick_sort_steps(arr)

        return render_template(
            "result.html",
            steps=steps,
            algorithm_name="Quick Sort",
            algorithm_type="sort",
            best_case="O(n log n)",
            average_case="O(n log n)",
            worst_case="O(n²)",
            space_complexity="O(log n)"
        )
    
    elif algorithm == "linear":

        target = int(request.form["target"])

        steps = linear_search_steps(arr, target)

        return render_template(
            "result.html",
            steps=steps,
            algorithm_name="Linear Search",
            algorithm_type="search",
            best_case="O(1)",
            average_case="O(n)",
            worst_case="O(n)",
            space_complexity="O(1)"
        )
    
    elif algorithm == "binary":

        target = int(request.form["target"])

        # Binary Search requires sorted array
        arr.sort()

        steps = binary_search_steps(
            arr,
            target
        )

        return render_template(
            "result.html",
            steps=steps,
            algorithm_name="Binary Search",
            algorithm_type="search",
            best_case="O(1)",
            average_case="O(log n)",
            worst_case="O(log n)",
            space_complexity="O(1)"
        )

@app.route("/ask", methods=["POST"])
def ask():

    data = request.json

    question = data["question"]

    algorithm = data["algorithm"]

    algorithm_type = data["algorithm_type"]

    current_step = data["current_step"]

    total_steps = data["total_steps"]

    array = data["array"]

    compare = data["compare"]

    sorted_indices = data["sorted"]

    comparisons = data["comparisons"]

    swaps = data["swaps"]

    progress = data["progress"]

    left = data.get("left")

    right = data.get("right")

    mid = data.get("mid")

    target = data.get("target")

    found = data.get("found")


    prompt = f"""
You are an AI assistant helping students understand algorithms.

Current Algorithm:
{algorithm}

Algorithm Type:
{algorithm_type}

Current Step:
{current_step}/{total_steps}

Current Array:
{array}

Compared Indices:
{compare}

Sorted Indices:
{sorted_indices}

Comparisons:
{comparisons}

Swaps:
{swaps}

Progress:
{progress}%

Binary Search State (ignore if not a search algorithm):

Left Index:
{left}

Right Index:
{right}

Middle Index:
{mid}

Target:
{target}

Found:
{found}

Instructions:

- Answer using the CURRENT visualization.
- If this is Bubble Sort, explain the current comparison and progress.
- If this is Binary Search, explain using the Left, Right and Middle indices.
- Never give generic textbook answers if visualization information is available.
- Keep answers concise (5–8 lines).

Student Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {"answer": response.text}

    except Exception as e:
        return {"answer": "AI Assistant is temporarily unavailable."}, 500

if __name__ == "__main__":
    app.run(debug=True)