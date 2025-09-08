# AI-Agent-workshop

Questo repository raccoglie esempi pratici su agenti e modelli di linguaggio.

## Indice dei contenuti

 - [AI Agents Basics with AutoGen](notebooks/autogen-ai-agents-basics.ipynb) – Introduzione ad AutoGen: definizione di agenti, conversazioni e utilizzo di strumenti.
 - [Local Model Agent Example](notebooks/ai-agent-local-model-example.ipynb) – Esegue un agente su un modello LLM locale usando Unsloth e Transformers.
 - [Agentic Solution for Business Pain Points](notebooks/ai-agent-business-solution.ipynb) – Progetta un flusso di tre chiamate per risolvere un pain point aziendale con API compatibile OpenAI.
 - [CrewAI Agents for Blogger Support](notebooks/crewai-blogger-support.ipynb) – Crea agenti e task con CrewAI per generare articoli e aggregare informazioni dal web.
 - [Entity Recognition with Hugging Face](notebooks/huggingface-entity-recognition.ipynb) – Mostra una pipeline di Named Entity Recognition e analisi dei risultati.
 - [Fine-tuning for Text Classification](notebooks/text-classification-finetuning.ipynb) – Addestra un modello Sentence Transformers e lo pubblica su Hugging Face.
 - [Getting Started with LangChain](notebooks/langchain-getting-started.ipynb) – Introduzione a LangChain, template di prompt e LangChain Expression Language.

## Prerequisiti e Avvio rapido

### Requisiti

- Python 3.10 o superiore
- Librerie principali: pyautogen, crewai, langchain, transformers, sentence-transformers, datasets, unsloth, accelerate, bitsandbytes, python-dotenv, jupyter

### Installazione

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Avvio

```bash
jupyter notebook
# oppure
jupyter lab
```

Apri quindi il notebook di interesse dalla lista sopra.
