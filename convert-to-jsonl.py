import ast
import json

# Run this script second
def convert_to_jsonl(data):
    # Extract labels where value == 1, excluding 'text'
    labels = [key for key, value in data.items() if key != 'text' and value == 1]

    # Join them with " / "
    label_str = " / ".join(labels)

    # Format into the desired structure
    result = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": data['text']}],
            },
            {
                "role": "model",
                "parts": [{"text": label_str}],
            }
        ]
    }
    return result


with open("../json file/output_voicemail4.jsonl", "r") as file:
    lines = file.readlines()

all_data = []
for i in range(len(lines)):
    all_data.append(ast.literal_eval(lines[i]))

converted_data = []
for data in all_data:
    converted = convert_to_jsonl(data)
    converted_data.append(converted)

with open('../json file/output_voicemail5.jsonl', 'w') as outfile:
    for entry in converted_data:
        json.dump(entry, outfile)
        outfile.write('\n')
