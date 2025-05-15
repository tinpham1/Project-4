import sqlite3
import pandas as pd

# Load your fixed CSV file
df = pd.read_csv("resources/space_missions.csv", encoding="ISO-8859-1")
df = df.fillna("")
df = df.drop(columns=["Price"])

# Connect to SQLite and rebuild the database
conn = sqlite3.connect("space_data.db")
cursor = conn.cursor()

# Drop table if it already exists
cursor.execute("DROP TABLE IF EXISTS missions")

# Create the missions table
cursor.execute("""
CREATE TABLE missions (
    "index" INTEGER,
    "company" TEXT,
    "location" TEXT,
    "date" TEXT,
    "time" TEXT,
    "rocket" TEXT,
    "mission" TEXT,
    "rocketstatus" TEXT,
    "missionstatus" TEXT
)
""")

# Insert CSV data into missions table
df.to_sql("missions", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("✅ space_data.db successfully rebuilt with missions table.")
