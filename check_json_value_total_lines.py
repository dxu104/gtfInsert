import json

# Replace with the path to your JSON file
#json_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/cmp_ref_data.json' #用trackingFile keyvalue.json替换cmp_ref_data.json的key之前，cmp_ref_data.json 有104860个value
json_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/sortInsert/gffInsert/nextflow/work/b7/4a98f483ab85ed3f633f8635b1d1f1/null_final_annotation.json'# 替换之后就只有79199个
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Count the total number of lines in all values
total_lines = sum(len(value) for value in data.values())

print(f"Total number of lines: {total_lines}")
