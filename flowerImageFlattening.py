import os
import shutil
import csv

# Path to unzipped flowers dataset
input_dir = "C:/Users/ezhan/Downloads/archive/flowers"  # <- CHANGE THIS
output_dir = "flowerImages"
os.makedirs(output_dir, exist_ok=True)

csv_file = "flowerLabels.csv"

# Open CSV for writing
with open(csv_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['filename', 'label'])

    for class_name in os.listdir(input_dir):
        class_dir = os.path.join(input_dir, class_name)
        if not os.path.isdir(class_dir):
            continue

        for filename in os.listdir(class_dir):
            src = os.path.join(class_dir, filename)
            dst_filename = f"{class_name}_{filename}"
            dst = os.path.join(output_dir, dst_filename)

            shutil.copy(src, dst)
            writer.writerow([dst_filename, class_name])
