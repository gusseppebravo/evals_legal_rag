# Legal RAG Evaluation

Creates ground truth Q&A datasets for evaluating legal RAG pipelines on data usage, privacy, and AI/ML restrictions.

## Features

- **Q&A Generation**: Creates multiple-choice questions from legal document chunks (2000+ tokens)
- **LLM Critic**: Evaluates factuality of generated Q&A pairs to ensure ground truth quality
- **RAG Evaluation**: Tests RAG system performance against ground truth using existing backend
- **Multiple Outputs**: Generates both datasets and evaluation results with detailed metrics

## Installation

```bash
uv sync
```

## Usage

### 1. Generate Ground Truth Dataset

Open `ground_truth_generation.ipynb` to:

1. **Generate Q&A pairs** from legal documents using LangChain and Azure OpenAI
2. **Evaluate factuality** using an LLM critic to filter out hallucinated content
3. **Export datasets**:
   - `qa_list.json`: All generated Q&A pairs with IDs
   - `qa_list_evaluated.json`: Q&A pairs with factuality scores
   - `qa_list_factual_only.json`: Only factually correct pairs (ground truth)

### 2. Evaluate RAG System

Open `rag_evaluation.ipynb` to:

1. **Load ground truth dataset** (`qa_list_factual_only.json`)
2. **Test RAG system** using existing `legal_rag.py` backend
3. **Calculate metrics**: accuracy, coverage, response time by client and document type
4. **Export results**:
   - `rag_evaluation_results.json`: Detailed evaluation results with metrics
   - `rag_evaluation_summary.csv`: Summary table for analysis
