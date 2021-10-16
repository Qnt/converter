import json
import csv

if __name__ == '__main__':
    with open("C:/Users/Aynur/Documents/Python Pit/converter/input.json") as f:
        json_input = json.loads(f.read())
    fieldnames = [*json_input[0]]
    with open("C:/Users/Aynur/Documents/Python Pit/converter/output.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(json_input)