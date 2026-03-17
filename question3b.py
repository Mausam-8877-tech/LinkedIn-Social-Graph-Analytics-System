import json
import random

# 📂 Load adjacency list
with open('adjacency_list.json', 'r', encoding='utf-8') as f:
    raw_adjacency_list = json.load(f)

# 🔄 Normalize keys to lowercase with underscores
adjacency_list = {
    key.lower().replace(" ", "_"): [v.lower().replace(" ", "_") for v in values]
    for key, values in raw_adjacency_list.items()
}

# 🎲 Generate a random walk (can contain repeated nodes)
def random_walk(start, end, max_steps=1000, max_retries=50):
    start = start.strip().lower().replace(" ", "_")
    end = end.strip().lower().replace(" ", "_")

    for attempt in range(max_retries):
        path = [start]
        current = start

        for step in range(max_steps):
            neighbors = adjacency_list.get(current, [])
            if not neighbors:
                break

            next_node = random.choice(neighbors)
            path.append(next_node)
            current = next_node

            if current == end:
                return path

        # print(f"❌ Retry {attempt + 1}: Walk didn't reach destination")

    return None

# ✂️ Prune a path to remove loops and repeated edges
def prune_path(path):
    seen = {}
    pruned = []

    for i, node in enumerate(path):
        if node in seen:
            idx = seen[node]
            pruned = pruned[:idx + 1]
            seen = {n: j for j, n in enumerate(pruned)}
        else:
            pruned.append(node)
            seen[node] = len(pruned) - 1

    return pruned

# 🔍 Example: Set start and end students
start_student = "mausam kumari"
end_student = "tamnna parveen"

walk = random_walk(start_student, end_student, max_steps=1000, max_retries=50)

if walk:
    print("\n🔀 Random Walk:")
    print(" → ".join(walk))

    pruned = prune_path(walk)
    print("\n✅ Pruned Path (Loop-free):")
    print(" → ".join(pruned))
# else:
    # print("❌ No path found after retries.")
