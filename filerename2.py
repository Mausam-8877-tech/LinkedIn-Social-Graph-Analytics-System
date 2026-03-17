import os

# Put your folder path here
folder_path = r"new_original_files"

# Map of messy file names to cleaned-up ones
rename_map = {
    "Ajay Jatav Connections-1 - Ajay Jatav.csv": "Ajay_Jatav.csv",
    "Aman_ Adarsh.csv": "Aman_Adarsh.csv",
    "Arjun Kadam - Arjun Kadam.csv": "Arjun_Kadam.csv",
    "Challa_Trivedh_Kumar - CHALLA TRIVEDH KUMAR.csv": "Trivedh_Kumar.csv",
    "Connection - VISHAL KUMAR.csv": "Vishal_Kumar.csv",
    "connection1-1 - Aman Adarsh.csv": "Aman_Adarsh.csv",
    "Connections - Aman Verma.csv": "Aman_Verma.csv",
    "Connections - Anand Singh.csv": "Anand_Singh.csv",
    "Connections - Harshit Chaturvedi.csv": "Harshit_Chaturvedi.csv",
    "connections - N. Arun Kumar.csv": "Arun_Kumar.csv",
    "Connections - Ompal Yadav.csv": "Ompal_Yadav.csv",
    "Connections - RAVI RAJPUT.csv": "Ravi_Rajput.csv",
    "debangsu_misra.csv - Debangsu Misra.csv": "Debangsu_Misra.csv",
    "Divyanshi_Sahu.csv - Divyanshi Sahu.csv": "Divyanshi_Sahu.csv",
    "Ekta Kumari - Ekta Kumari.csv": "Ekta_Kumari.csv",
    "gaurav_khainwar.csv - Gaurav Khainwar.csv": "Gaurav_Khainwar.csv",
    "HimanshuKanwarChundawat - Himanshu Chundawat.csv": "Himanshu_Chundawat.csv",
    "KARANPAL_SINGH_RANAWAT - KARANPAL SINGH RANAWAT.csv": "Karanpal_Singh_Ranawat.csv",
    "linkedin list - Nidhi Kumari.csv": "Nidhi_Kumari.csv",
    "Linked_in_connection - Samina Sultana.csv": "Samina_Sultana.csv",
    "Manoj K. Connections - MANOJ KHARKAR.xlsx": "Manoj_Kharkar.xlsx",
    "Nirmal LinkdIn Connections - NIRMAL MEWADA.csv": "Nirmal_Mewada.csv",
    "Prem kumar.csv": "Prem_Kumar.csv",
    "Pushpraj_Singh.csv - Pushpraj Singh.csv": "Pushpraj_Singh.csv",
    "Rahul_Kumar_Verma - Rahul Verma.csv": "Rahul_Kumar_Verma.csv",
    "Ranjeet_Kumar_Yadav - Ranjeet Yadav.csv": "Ranjeet_Kumar_Yadav.csv",
    "Samina_Sultana.csv": "Samina_Sultana.csv",
    "Shivam_Shukla.csv": "Shivam_Shukla.csv",
    "Shubham Kumar - Shubham Kumar.csv": "Shubham_Kumar.csv",
    "Sneha_Shaw.csv": "Sneha_Shaw.csv",
    "Uppara Sai_Maithreyi - UPPARA MAITHREYI.csv": "Uppara_Maithreyi.csv",
}

# Function to auto-append numbers if filename exists
def get_unique_name(path):
    base, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = f"{base}_{counter}{ext}"
        counter += 1
    return path

# Process the renaming
for old_name, new_name in rename_map.items():
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)

    if os.path.exists(old_path):
        final_new_path = get_unique_name(new_path)
        os.rename(old_path, final_new_path)
        print(f"✅ Renamed: {old_name} --> {os.path.basename(final_new_path)}")
    else:
        print(f"❌ File not found: {old_name}")