# handles file reading/writing 
import json

def load_portfolio():
    try:
        with open('data/portfolio.json','r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error: The file 'portfolio.json' was not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return {}

