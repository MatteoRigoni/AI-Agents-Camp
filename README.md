<p align="center">
  <img src="assets/openais-banner.svg" alt="AI Agents Camp banner" />
</p>

# openais-camp

[![GitHub](https://img.shields.io/badge/GitHub-AI--agents--camp-blue?style=for-the-badge&logo=github)](https://github.com/MatteoRigoni/openais-camp)

> **Nota**: repository precedentemente noto come `AI-Camp_LLM-Agents-Transformers`.



Questo repository raccoglie esempi pratici su agenti e modelli di linguaggio.

## Indice dei contenuti

 - [AI Agents Basics with AutoGen](notebooks/autogen-openais-basics.ipynb) – Introduzione ad AutoGen: definizione di agenti, conversazioni e utilizzo di strumenti.
 - [Local Model Agent Example](notebooks/openai-local-model-example.ipynb) – Esegue un agente su un modello LLM locale usando Unsloth e Transformers.
 - [Agentic Solution for Business Pain Points](notebooks/openai-business-solution.ipynb) – Progetta un flusso di tre chiamate per risolvere un pain point aziendale con API compatibile OpenAI.
 - [Cold Outreach Agent](notebooks/openai-cold-outreach.ipynb) – Sistema agentico in Python che genera e invia email a freddo con SendGrid, usando tool, handoff tra agenti e tracing.
 - [Cold Outreach Agent](notebooks/openai-deep-web-researcher.ipynb) – Agente che pianifica ricerche web, sintetizza i risultati in un report strutturato, usando OpenAI Agents, tool hosted e tracing end-to-end..
 - [CrewAI Agents for Blogger Support](notebooks/crewai-blogger-support.ipynb) – Crea agenti e task con CrewAI per generare articoli e aggregare informazioni dal web.
 - [Entity Recognition with Hugging Face](notebooks/huggingface-entity-recognition.ipynb) – Mostra una pipeline di Named Entity Recognition e analisi dei risultati.
 - [Fine-tuning for Text Classification](notebooks/huggingface-text-classification-finetuning.ipynb) – Addestra un modello Sentence Transformers e lo pubblica su Hugging Face.
 - [Getting Started with LangChain](notebooks/langchain-getting-started.ipynb) – Introduzione a LangChain, template di prompt e LangChain Expression Language.
 - [AI Agent Profile Chatbot](notebooks/openai-profile-chatbot.ipynb) – Crea un chatbot per il profilo personale utilizzando modelli di linguaggio avanzati.

## Prerequisiti e Avvio rapido

### Requisiti

- Python 3.10 o superiore
- Librerie principali: pyautogen, crewai, langchain, transformers, sentence-transformers, datasets, unsloth, accelerate, bitsandbytes, python-dotenv, jupyter

### Installazione

```bash
python -m venv .venv
source \.venv\Scripts\activate
pip install -r requirements.txt
```

### Avvio

```bash
jupyter notebook
# oppure
jupyter lab
```

Apri quindi il notebook di interesse dalla lista sopra.