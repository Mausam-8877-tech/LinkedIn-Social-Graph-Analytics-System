import random
import statistics
from question3b import random_walk, prune_path  # ✅ use your module

# 📊 Helper for mode with fallback
def safe_mode(data):
    try:
        return statistics.mode(data)
    except statistics.StatisticsError:
        return "No unique mode"

# 📊 Helper for full statistics
def compute_stats(data, label):
    print(f"{label} → Average: {sum(data)/len(data):.2f}, "
          f"Median: {statistics.median(data)}, "
          f"Mode: {safe_mode(data)}, "
          f"Std Dev: {statistics.stdev(data):.2f}")

# 📂 Load students from adjacency list (assumed already cleaned)
import json
with open('adjacency_list.json', 'r', encoding='utf-8') as f:
    raw_adj = json.load(f)
all_students = [s.lower().replace(" ", "_") for s in raw_adj.keys()]

# 📊 Containers for lengths
random_walk_lengths = []
pruned_path_lengths = []

# 🔁 Collect 100 successful samples
success = 0
attempt = 0
while success < 100 and attempt < 2000:
    s1, s2 = random.sample(all_students, 2)
    if s1 == s2:
        continue

    walk = random_walk(s1, s2)
    attempt += 1

    if walk:
        pruned = prune_path(walk)
        random_walk_lengths.append(len(walk))
        pruned_path_lengths.append(len(pruned))
        print(f"✅ {success+1}: {s1} → {s2} | Walk: {len(walk)} | Pruned: {len(pruned)}")
        success += 1
    # else:
        # print(f"❌ Attempt {attempt}: No path found {s1} → {s2}")

# 📈 Show final statistics
if success:
    print("\n📊 Statistics for 100 successful samples:")
    compute_stats(random_walk_lengths, "Random Walks")
    compute_stats(pruned_path_lengths, "Pruned Paths")
else:
    print("🚫 No successful paths to analyze.")
