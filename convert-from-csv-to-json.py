import pandas as pd

# Run this script first to start from csv
# Load your CSV file
df = pd.read_csv("../voicemail_data6.csv")  # Replace with your actual CSV file name

# Convert to JSON Lines format
with open("../json file/output_voicemail4.jsonl", "w") as f:
    for record in df.to_dict(orient="records"):
        f.write(f"{record}\n")
