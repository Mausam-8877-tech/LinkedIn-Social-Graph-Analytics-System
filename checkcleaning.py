import pandas as pd
import chardet
import glob
import os
import re

# Define cleaning function
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = str(text)
    text = re.sub(r'[,\t;|\.]', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text.title()

# Detect encoding
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read(100000))
        return result['encoding']

# Folder setup
input_folder = r"new_renamed_files"
output_folder = os.path.join(input_folder, "cleaned_outputs")

os.makedirs(output_folder, exist_ok=True)

# Get all CSV files
csv_files = glob.glob(os.path.join(input_folder, "*.csv"))

# Initialize tracking
skipped_read = 0
skipped_empty = 0
saved = 0
overwritten_files = set()
total = len(csv_files)

# Clean each CSV
for file in csv_files:
    encoding = detect_encoding(file)
    print(f" Detected Encoding: {file} => {encoding}")

    df = None
    read_successful = False
    fallback_encodings = [encoding, 'ISO-8859-1', 'cp1252', 'latin1']

    for enc in fallback_encodings:
        try:
            df = pd.read_csv(file, encoding=enc, sep=None, engine='python')
            print(f" Read success: {file} using {enc}")
            read_successful = True
            break
        except Exception as e:
            print(f" Read failed: {file} using {enc} → {e}")

    if not read_successful:
        skipped_read += 1
        continue

    try:
        df.columns = [col.strip().lower() for col in df.columns]

        for col in df.columns:
            df[col] = df[col].astype(str).apply(clean_text)

        df.dropna(how='all', inplace=True)
        df.drop_duplicates(inplace=True)

        if df.empty:
            skipped_empty += 1
            print(f" Skipping empty file after cleaning: {file}")
            continue

        # Keep original filename
        output_path = os.path.join(output_folder, os.path.basename(file))

        if os.path.exists(output_path):
            print(f" Overwriting file: {output_path}")
            overwritten_files.add(output_path)

        df.to_csv(output_path, index=False)
        print(f" Cleaned CSV saved: {output_path}")
        saved += 1

    except Exception as e:
        print(f" Error processing {file}: {e}")

# Summary
print("\n Processing Summary")
print(f" Total CSV files found: {total}")
print(f" Cleaned & saved: {saved}")
print(f" Skipped (read error): {skipped_read}")
print(f" Skipped (empty after cleaning): {skipped_empty}")
print(f" Overwritten files due to duplicate names: {len(overwritten_files)}")