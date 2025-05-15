# Purpose: Parse user input to determine intent (for SQL-based handlers)

import re

def classify_intent(question):
    q = question.lower()

    if "reusable" in q and "active" in q:
        return "get_reusable_active"

    elif "retired" in q and "expendable" in q:
        return "get_retired_expendable"

    elif "most missions" in q or ("top" in q and "missions" in q):
        year = extract_year(q)
        return "top_company_by_missions" if year else "top_rockets"

    elif "longest operational" in q or ("longest" in q and "active" in q):
        return "longest_operational"

    elif "rockets launched by" in q or "used by" in q or "from" in q:
        return "rockets_by_company"

    return None

def extract_year(text):
    match = re.search(r"(20\d{2})", text)
    return match.group(1) if match else None

def extract_company(text):
    # Can be expanded as needed
    companies = ["spacex", "nasa", "boeing", "lockheed", "ula", "blue origin"]
    for company in companies:
        if company in text.lower():
            return company
    return None
