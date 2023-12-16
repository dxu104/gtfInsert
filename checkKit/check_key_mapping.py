import json

def check_key_mapping(source_file_path, target_file_path):
    # Load the source file data
    with open(source_file_path, 'r') as file:
        source_data = json.load(file)

    # Load the target file data
    with open(target_file_path, 'r') as file:
        target_data = json.load(file)

    # Check if each key in the target file has a mapping in the source file
    unmapped_keys = []
    for key in target_data.keys():
        if key not in source_data:
            unmapped_keys.append(key)

    return unmapped_keys

# File paths (update these with actual paths)
source_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/keyvalue.json'
target_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/cmp_ref_data.json'

# Check and get the unmapped keys
unmapped_keys = check_key_mapping(source_file_path, target_file_path)

# Print the result
print("Unmapped Keys:", unmapped_keys)

