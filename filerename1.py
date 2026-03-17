import os
import re
import shutil
import glob

# 📁 Base folder containing input files
input_folder = r"LinkedIn Data Public"

# 📁 Create output folders
renamed_folder = os.path.join(input_folder, "new_renamed_files")
original_folder = os.path.join(input_folder, "new_original_files")
os.makedirs(renamed_folder, exist_ok=True)
os.makedirs(original_folder, exist_ok=True)

# 📄 Gather all CSV and Excel files
all_files = glob.glob(os.path.join(input_folder, "*.csv")) + glob.glob(os.path.join(input_folder, "*.xlsx"))

# 🔁 Counter for renamed files
renamed_count = 0

# 🔁 Loop through each file
for file_path in all_files:
    base = os.path.basename(file_path)
    name, ext = os.path.splitext(base)

    # 👇 Match pattern like "Mausam_kumari - Mausam kumari"
    match = re.match(r"([A-Za-z]+_[A-Za-z]+)\s*-\s*([A-Za-z\s]+)", name)

    if match:
        # 🎯 Rename using the first part only and title-case it
        new_name = match.group(1).title().replace(" ", "") + ext
        new_path = os.path.join(renamed_folder, new_name)
        shutil.copy(file_path, new_path)
        renamed_count += 1
        print(f"✅ Renamed & copied: {base} → {new_name}")
    else:
        # 🚫 No renaming, just copy to original_files folder
        new_path = os.path.join(original_folder, base)
        shutil.copy(file_path, new_path)
        print(f"📄 Copied without renaming: {base}")

# ✅ Print summary
print(f"\n🔢 Total files renamed: {renamed_count}")
print(f"📁 Renamed files saved in: {renamed_folder}")
print(f"📁 Unchanged files saved in: {original_folder}")
