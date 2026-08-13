# AI Chatbot Using LangChain

A simple AI chatbot built with LangChain, ChatGroq, and Streamlit.


## Project Overview

This project shows how LangChain can be used to build a chatbot with different chains.

The chatbot can handle:

- Programming questions
- Mathematics questions
- General questions

It also generates 3 follow-up questions for the user that they might ask next.

## Features

- Chat interface using Streamlit
- Chat history
- Programming Assistant
- Mathematics Assistant
- General Assistant
- RunnableBranch for response based on category
- RunnableParallel for multiple outputs
- Pydantic Structured Output
- Follow-up question generation
- ChatGroq LLM

## Install the required packages:

```pip install -r requirements.txt```

## Create a .env file:

```GROQ_API_KEY=your_groq_api_key```

## Run the application:

```streamlit run app.py```

## RunnableParallel Implementation:

`RunnableParallel` is used to generate multiple outputs from the same user question at the same time.

```  
                  User Question
                         |
                        
                 RunnableParallel
                    /          \
                   /            \
                  v              v
             Main Answer    Follow-up Questions
                  |              |
                  \              /
                   \            /
                    v          v
                    Final Response
```


## RunnableBranch Implementation

`RunnableBranch` is used to route the user's question to the appropriate chain.

```text
User Question
      |
      v
RunnableBranch
   /    |    \
  /     |     \
Programming  Math  General