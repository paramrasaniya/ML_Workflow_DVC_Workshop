# ML Workflow with DVC

This project is a simple machine learning workflow built with **DVC (Data Version Control)** and **PyTorch**. The goal of this workshop is to understand how DVC helps organize a machine learning pipeline by tracking data, code, parameters, models, and metrics in a reproducible way.

In this project, the pipeline is based on the **MNIST** dataset and includes these main steps:

- preparing the dataset
- training a CNN model
- saving evaluation metrics
- generating predictions

## Project Structure

```text
ML_Workflow_DVC/
├── data/
│   └── processed/
├── src/
│   ├── prepare.py
│   ├── train.py
│   └── predict.py
├── params.yaml
├── dvc.yaml
├── metrics.json
├── predictions.json
├── model.pt
├── ML_Workflow_DVC_updated.ipynb
└── README.md
```

## What Each File Does

- `src/prepare.py` downloads and prepares the MNIST dataset.
- `src/train.py` trains the CNN model using the values from `params.yaml`.
- `src/predict.py` loads the trained model and creates predictions on the test set.
- `params.yaml` stores experiment settings like epochs, learning rate, and batch size.
- `dvc.yaml` defines the DVC pipeline stages and their dependencies.
- `metrics.json` stores the model evaluation result.
- `predictions.json` stores sample predictions from the trained model.
- `model.pt` is the saved trained PyTorch model.
- `ML_Workflow_DVC_updated.ipynb` explains the workflow step by step with code and talking points.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/paramrasaniya/ML_Workflow_DVC_Workshop.git
cd ML_Workflow_DVC
```

### 2. Create and activate a virtual environment

#### Windows PowerShell

```powershell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Mac/Linux

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install required libraries

```bash
pip install dvc torch torchvision scikit-learn pandas pyyaml jupyter notebook
```

## How to Run the Project

### Option 1: Run the DVC pipeline

This is the main way to run the project.

```bash
dvc repro
```

After running the pipeline, you can view the metric with:

```bash
dvc metrics show
```

### Option 2: Run each script manually

If you want to test each step one by one, run:

```bash
python src/prepare.py
python src/train.py
python src/predict.py
```

## Parameters

The training settings are stored in `params.yaml`.

Example:

```yaml
epochs: 2
lr: 0.001
batch_size: 64
```

You can change these values and then rerun:

```bash
dvc repro
dvc metrics show
```

## DVC Pipeline Stages

The pipeline is defined in `dvc.yaml` and follows this workflow:

```text
prepare -> train -> predict
```

- **prepare**: creates processed dataset files
- **train**: trains the CNN model and saves `model.pt` and `metrics.json`
- **predict**: uses the trained model to create `predictions.json`

## Output Files

After a successful run, these main output files are created:

- `data/processed/train.pt`
- `data/processed/test.pt`
- `model.pt`
- `metrics.json`
- `predictions.json`

## Notes

- If `dvc pull` does not work in the professor repo, run `dvc repro` instead.
- Do not run `git init` or `dvc init` again if the cloned repo already contains `.git` and `.dvc`.
- Run commands from the **project root folder**.

## Learning Summary

From this project, we learned that:

- Git is good for code, but DVC is better for tracking ML artifacts like data and models.
- `params.yaml` helps keep experiments organized.
- `dvc.yaml` makes the workflow reproducible and easier to rerun.
- DVC only reruns the stages that actually changed.
- A pipeline can be extended step by step, such as adding a prediction stage after training.

## Team Members

- 1) Param Rasaniya,         Student ID: 9086095
- 2) Viraj Mistry,           Student ID: 9088985
- 3) Sumanth Reddy,          Student ID: 9040660
