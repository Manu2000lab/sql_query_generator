from google import genai

# --- Configuration ---
client = genai.Client(api_key="Enter your API Key")


def generate_sql_generic(scenario_description):
    prompt = f"""You are a SQL expert. Write a single, correct SQL query for the 
following scenario. The user may or may not specify exact table/column names — 
if they don't, use clear, sensible placeholder names (e.g., table_name, 
column_name) that the user can easily replace with their real names.

Rules:
- Return ONLY the SQL query, no explanation, no markdown formatting, no ```sql tags
- Use standard ANSI SQL syntax that works across MySQL, PostgreSQL, and SQL Server
  unless the user specifies a particular database
- If the scenario is ambiguous, make a reasonable assumption and write a working query

Scenario: {scenario_description}

SQL query:"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    sql_query = response.text.strip()
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
    
    return sql_query

if __name__ == "__main__":
    test_scenario = "Write a query to find the highest salary in this table"
    sql = generate_sql_generic(test_scenario)
    print("Generated SQL:\n", sql)