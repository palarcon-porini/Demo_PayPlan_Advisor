# README

## Introduzione

Questa demo utilizza LangChain e LangGraph per gestire un flusso di agenti che estraggono e creano un piano di pagamenti da un file PDF contenente un contratto e un altro file PDF contenente le fatture. L'applicazione è sviluppata con Streamlit, una libreria Python per la creazione di applicazioni web interattive.

## Requisiti

- Python 3.8 o superiore

Puoi installare tutte le dipendenze usando il file `requirements.txt` incluso:

```streamlit
langchain-core
langgraph
langchain-experimental
langchain-openai
langchain-community
langchain-text-splitters
python-dotenv
pypdf
```

## Installazione

1. Clona questo repository:

```bash
git clone <URL_DEL_REPOSITORY>
cd <NOME_DEL_REPOSITORY>
```

2. Crea un ambiente virtuale e attivalo:

```bash
python -m venv venv
source venv/bin/activate  # Su Windows usa `venv\Scripts\activate`
```

3. Installa le dipendenze:

```bash
pip install -r requirements.txt
```

## Esecuzione dell'app

Per eseguire l'applicazione, utilizza il comando:

```bash
streamlit run app.py
```
O pure  

```bash
python app.py
```

## Struttura del Progetto

- `app.py`: Contiene il codice principale per l'app Streamlit.
- `.env`: Contine le credenziali per l'API di Openai.
- `GraphColection`: Cartella con il codice delle struttura 

## Funzionalità Principali

### 1. Caricamento dei File

L'app consente agli utenti di caricare due file PDF: uno contenente il contratto e uno contenente le fatture.

### 2. Estrazione dei Dati

Gli agenti di LangChain estraggono le informazioni rilevanti dai PDF caricati. Utilizziamo tecniche di elaborazione del linguaggio naturale per identificare e strutturare i dati chiave.

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Consulta il file `LICENSE` per maggiori dettagli.

---

Grazie per aver utilizzato questa demo! Speriamo che ti sia utile per i tuoi progetti di gestione dei pagamenti.