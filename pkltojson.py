import pickle
import pandas as pd
import sys

# Get the filename from command-line arguments
script, filename = sys.argv

# Load the pickle file safely
with open(filename, 'rb') as input_file:
    new_dict = pickle.load(input_file)

# Check type
print(f"Loaded data type: {type(new_dict)}")
print(f"First few elements: {new_dict[:5] if isinstance(new_dict, list) else list(new_dict.keys())}")

# Convert to DataFrame based on structure
if isinstance(new_dict, list):
    if isinstance(new_dict[0], dict):  # List of dicts
        df = pd.DataFrame(new_dict)
    else:  # List of lists
        df = pd.DataFrame(new_dict)
elif isinstance(new_dict, dict):  # Dictionary
    df = pd.DataFrame.from_dict(new_dict, orient='index')
else:
    raise ValueError("Unexpected data format!")

# Save as JSON
df.to_json("data.json", orient="values", date_format="iso", date_unit="s")
