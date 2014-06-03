import csv
import glob

csv_list = glob.glob("csv/*.csv")

all_records = []

for c in csv_list:
    cluster = c.split("_")[1][2:].replace(".csv", "") 
    group_ti = c.split("_")[0][6:]
    with open(c, 'rb') as csvfile:
        csv_file = csv.reader(csvfile, delimiter='\t')
        for row in csv_file:
            row_list = []
            row_gi = row[1].split("_ti_")[0].replace("gi_", "")
            row_ti = row[1].split("_ti_")[1]
            row_distance = row[2].split(":")[2].replace(" ", "")
            row_cutoff = row[2].split(":")[1].replace(".0 with Distance", "")[1:]
            row_list.append(cluster)
            row_list.append(group_ti)
            row_list.append(row_gi)
            row_list.append(row_ti)
            row_list.append(row_distance)
            row_list.append(row_cutoff)
            all_records.append(row_list)


label_list = ["Cluster ID", "Cluster TI", "Record GI", "Record TI", "Record Distance", "Group Cutoff"]
all_records.insert(0, label_list) 
with open('outliers.csv', 'wb') as f:
    writer = csv.writer(f, delimiter='\t')
    for r in all_records:
        writer.writerow(r)
