# Purpose: Execute SQL queries for structured intent responses

import sqlite3
import re

def get_db_connection():
    conn = sqlite3.connect("space_data.db")
    conn.row_factory = sqlite3.Row
    return conn

def handle_get_reusable_active():
    with get_db_connection() as conn:
        cur = conn.execute("""
            SELECT rocket FROM us_operation_time
            WHERE rocketstatus = 'Active' AND reusability = 'Reusable'
        """)
        return [row["rocket"] for row in cur.fetchall()]

def handle_get_retired_expendable():
    with get_db_connection() as conn:
        cur = conn.execute("""
            SELECT rocket FROM us_operation_time
            WHERE rocketstatus = 'Retired' AND reusability = 'Expendable'
        """)
        return [row["rocket"] for row in cur.fetchall()]

def handle_top_company_by_missions(year):
    with get_db_connection() as conn:
        cur = conn.execute("""
            SELECT company, COUNT(*) AS mission_count
            FROM missions
            WHERE strftime('%Y', date) = ?
            GROUP BY company
            ORDER BY mission_count DESC
            LIMIT 1
        """, (year,))
        result = cur.fetchone()
        return f"{result['company']} with {result['mission_count']} missions" if result else "No data for that year."

def handle_longest_operational():
    with get_db_connection() as conn:
        cur = conn.execute("""
            SELECT rocket, operation_days FROM us_operation_time
            ORDER BY operation_days DESC
            LIMIT 1
        """)
        result = cur.fetchone()
        return f"{result['rocket']} ({result['operation_days']} days)" if result else "No data found."

def handle_top_rockets():
    with get_db_connection() as conn:
        cur = conn.execute("""
            SELECT rocket, total_missions FROM us_operation_time
            ORDER BY total_missions DESC
            LIMIT 5
        """)
        return [f"{row['rocket']} ({row['total_missions']} missions)" for row in cur.fetchall()]

def handle_rockets_by_company(company):
    with get_db_connection() as conn:
        cur = conn.execute("""
            SELECT DISTINCT rocket FROM us_operation_time
            WHERE LOWER(company) = LOWER(?)
        """, (company,))
        return [row['rocket'] for row in cur.fetchall()]

def handle_intent(intent, question):
    if intent == "get_reusable_active":
        rockets = handle_get_reusable_active()
        return ", ".join(rockets) if rockets else "No reusable and active rockets found."
    
    elif intent == "get_retired_expendable":
        rockets = handle_get_retired_expendable()
        return ", ".join(rockets) if rockets else "No retired expendable rockets found."

    elif intent == "top_company_by_missions":
        year_match = re.search(r"(20\d{2})", question)
        year = year_match.group(1) if year_match else None
        return handle_top_company_by_missions(year) if year else "Please provide a year in your question."

    elif intent == "longest_operational":
        return handle_longest_operational()

    elif intent == "top_rockets":
        rockets = handle_top_rockets()
        return ", ".join(rockets) if rockets else "No rocket data found."

    elif intent == "rockets_by_company":
        company = question.split()[-1]  # basic heuristic
        rockets = handle_rockets_by_company(company)
        return ", ".join(rockets) if rockets else f"No rockets found for {company}."

    else:
        return "Sorry, I couldn't match that question to a known intent."
