import json

# 📖 Load adjacency list
with open('adjacency_list.json', 'r', encoding='utf-8') as f:
    adjacency_list = json.load(f)

# 📊 Compute and sort degrees
degrees = {student: len(neighbors) for student, neighbors in adjacency_list.items()}
sorted_degrees = dict(sorted(degrees.items(), key=lambda x: x[1], reverse=True))  # Descending order

# 💾 Save sorted degrees to JSON
with open('student_degrees.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_degrees, f, indent=4)

print("✅ Sorted degrees saved to student_degrees.json (highest degree first)")
