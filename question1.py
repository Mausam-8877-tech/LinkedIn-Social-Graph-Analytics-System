# 1. Make a graph (adjacency list) based on which student is adjacent with
# which of these people.

# 2. Find the degree of each student

# 3. Given any pair of students, find a random walk connecting them.
# a. Prune this random walk to find a path connecting the given pair or
# students.
# b. Compute some statistical estimates of the length of these random
# walks and the pruned paths.

# 4. Create a report about the linkedin network for your class.
# Use your creativity to figure out the format,
# and your intelligence to figure out the contents.
import os
import pandas as pd
import re
import json
from collections import defaultdict

# 📂 Folder containing cleaned student files
input_folder = r"cleaned_outputs"

# 🧠 Helper functions
def extract_name(filename):
    return filename.replace('.csv', '').strip().lower()

def normalize_name(name):
    name = str(name).strip().lower()
    name = re.sub(r'\s+', ' ', name)
    return name

# 📁 Lists to track
files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
have_file = set(extract_name(f) for f in files)
adjacency_list = defaultdict(set)
not_have_file = set()
name_to_file = {}

# 🔁 Process each file to build graph
for file in files:
    file_path = os.path.join(input_folder, file)
    try:
        df = pd.read_csv(file_path)

        owner = extract_name(file)
        name_to_file[owner] = file

        if 'full_name' in df.columns:
            adjacent_people = df['full_name'].dropna().map(normalize_name)
        elif 'first name' in df.columns and 'last name' in df.columns:
            adjacent_people = (df['first name'] + ' ' + df['last name']).map(normalize_name)
        else:
            continue

        for person in adjacent_people:
            if person == owner:
                continue
            adjacency_list[owner].add(person)
            if person not in have_file:
                not_have_file.add(person)

    except Exception as e:
        print(f"❌ Error reading {file}: {e}")

# 🔁 Build reverse connections for those without file
for unknown in not_have_file:
    for known in list(adjacency_list.keys()):
        if unknown in adjacency_list[known]:
            adjacency_list[unknown].add(known)

# 🧾 Save adjacency list to JSON
json_path = os.path.join(input_folder, 'adjacency_list.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump({k: list(v) for k, v in adjacency_list.items()}, f, indent=4)
print(f"✅ Adjacency list saved to JSON → {json_path}")

# 📊 Final stats
print(f"\n👥 Total students with file: {len(have_file)}")
print(f"👀 Students without file (extracted from others): {len(not_have_file)}")

