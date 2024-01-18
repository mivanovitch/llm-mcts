import outlines
from concurrent.futures import ThreadPoolExecutor
# from human_eval.execution import check_correctness
from verilog_eval.data import read_problems
from verilog_eval.data import VERILOG_EVAL_HUMAN, HUMAN_DESCRIPTIONS

problems = read_problems(VERILOG_EVAL_HUMAN)
descriptions = read_problems(HUMAN_DESCRIPTIONS)
for task_id, item in descriptions.items():
    problems[task_id]['description'] = item['detail_description']

problems = list(problems.values())

STOP_SEQUENCES = ["```"]


# def stats_execute(task_id, completion, timeout=10):
#     problem = task_id_problem_map[task_id]
#     split_tests = task_id_split_tests_map[task_id]
#     thread_problems = [{**problem, "test": test} for test in split_tests]
#     results = []
#     with ThreadPoolExecutor() as executor:
#         for result in executor.map(
#             lambda tp: check_correctness(tp, completion, timeout), thread_problems
#         ):
#             results.append(result["passed"])

#     return {
#         "task_id": task_id,
#         "pass_rate": sum(results) / len(results),
#     }


@outlines.prompt
def few_shot_prompt(instructions, examples, description, question):
    """{{ instructions }}

    {% for example in examples %}
    Description:
    ```
    {{ example.description }}
    ```
    Question:
    ```
    {{ example.prompt }}
    ```
    Answer:
    ```
    {{ example.canonical_solution }}
    ```
    {% endfor %}

    Description:
    ```
    {{ description }}
    ```
    Question:
    ```
    {{ question }}
    ```
    Answer:
    ```
    """


instructions = "Please answer the following question following the examples. Generate valid verilog code always."
examples = problems[:2]


def get_prompts_with_ids():
    prompts_with_ids = [
        (few_shot_prompt(instructions, examples, problem["description"], problem["prompt"]), problem["task_id"])
        for problem in problems[2:]
    ]
    return prompts_with_ids
