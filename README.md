# Legal RAG Evaluation

Creates ground truth Q&A datasets for evaluating legal RAG pipelines on data usage, privacy, and AI/ML restrictions.

## Features

- **Q&A Generation**: Creates multiple-choice questions from legal document chunks (2000+ tokens)
- **LLM Critic**: Evaluates factuality of generated Q&A pairs to ensure ground truth quality
- **Multiple Outputs**: Generates both full dataset and filtered factually-correct dataset

## Installation

```bash
uv sync
```

## Usage

Open `evaluation.ipynb` to:

1. **Generate Q&A pairs** from legal documents using LangChain and Azure OpenAI
2. **Evaluate factuality** using an LLM critic to filter out hallucinated content
3. **Export datasets**:
   - `qa_list.json`: All generated Q&A pairs with IDs
   - `qa_list_evaluated.json`: Q&A pairs with factuality scores
   - `qa_list_factual_only.json`: Only factually correct pairs (ground truth)valuation

Creates ground truth Q&A datasets for evaluating legal RAG pipelines on data usage, privacy, and AI/ML restrictions.

## Installation

```bash
uv sync
```

## Usage

Open `evaluation.ipynb` to generate Q&A pairs (qa_list.json) from legal documents using LangChain and Azure OpenAI.