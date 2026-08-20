# AI SQL Query Generator

A general-purpose SQL query writer — describe any scenario in plain English, and Google's Gemini model generates a working SQL query. Unlike a database-connected assistant, this tool has no live connection to any specific database: it writes syntactically correct SQL for any table/column structure you describe (or sensible placeholders if you don't specify one), making it a flexible helper for writing queries quickly, regardless of project or database.

This is a companion project to [AI-Powered SQL Chatbot for CRM Sales Data](../ai-sql-chatbot) — that project answers questions about one specific, connected database; this one is a general-purpose SQL-writing assistant with no database connection at all.

## What It Does

1. User describes a SQL scenario in plain English (e.g., *"Write a query to find the highest salary in the employees table"*)
2. The description is sent to Google's Gemini model, along with instructions to write standard, portable SQL
3. If the user doesn't specify exact table/column names, the model uses clear placeholder names (e.g., `table_name`, `column_name`) that are easy to swap out
4. The generated SQL is displayed — nothing is executed, since there's no database connected

## Tech Stack

- **Python** — application logic
- **Google Gemini API** (`google-genai`) — natural language → SQL generation
- **Streamlit** — web interface

## Why Build This Separately from the CRM Chatbot

The two projects demonstrate different things intentionally:

| | This project | [CRM SQL Chatbot](../ai-sql-chatbot) |
|---|---|---|
| Database connection | None | Live PostgreSQL |
| Scope | Any scenario, any schema | One specific, known schema |
| Output | SQL text only | SQL text + real executed results |
| Use case | Quick SQL drafting/learning aid | Answering questions about real data |

Building both shows the difference between a context-aware AI tool (grounded in real data, with execution and safety guardrails) and a general-purpose AI writing assistant (flexible, but unverified and non-executing).

## Limitations

- The model has no way to verify a generated query is syntactically perfect for every SQL dialect — always review generated SQL before running it against a real database
- Since nothing is executed, there's no feedback loop confirming the query actually works — this is a drafting/learning tool, not a validated query-execution system
- Placeholder table/column names are guesses based on context (e.g., "salary" implies an `employees` table) — always replace them with your real schema names

## How to Run It

1. Clone this repo and install dependencies:
   ```
   pip install streamlit,Python,pandas,google-genai
   ```
2. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com)
3. In `sql_generator.py`, add your Gemini API key
4. Run the app:
   ```
   python -m streamlit run app.py
   ```
5. Open the browser tab it launches (usually `localhost:8501`) and describe a scenario

## Example Scenarios to Try

- "Write a query to find the highest salary in this table"
- "Find all customers in the Sales department, table name is staff, department column is dept"
- "Get the top 5 best-selling products by total revenue"
- "Find duplicate email addresses in a users table"


## Repo Structure

```
ai-sql-generator/
├── sql_generator.py     # Core logic: prompt construction, SQL generation
├── app.py                # Streamlit web interface
├── app_screenshot.png
└── README.md
```

---

*A self-directed project built to practice prompt engineering for a general-purpose (non-database-connected) AI tool, and to understand the practical difference between context-grounded and general-purpose AI assistants.*
