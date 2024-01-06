## llm-mcts

This is a project to explore Monte-Carlo Tree Search (MCTS) for Code-Gen tasks. We first test our method on the Human-Eval dataset.

### Initial Setup

This project uses `conda` to manage its python environment and packages. To install all relevant libraries, run the following:

```sh
conda env create -f environment.yml
conda activate llm-mcts
```

#### Locally downloading Human-Eval dataset

We use a modified human-eval dataset/enviroment from https://github.com/arunpatro/human-eval. This fork contains updated code for python-3.10 and also extends the error feedback to include the traceback.

```sh
git clone https://github.com/arunpatro/human-eval
pip install -e human-eval
```

Checkout the `nbs/humaneval.ipynb` for a demo.

### Running MCTS code generation

```sh
PYTHONPATH="./human-eval" python src/mcts.py
```