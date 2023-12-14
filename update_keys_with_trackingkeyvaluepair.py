import json

def update_keys(source_file, target_file, new_file):
    try:
        print("Loading source data...")
        with open(source_file, 'r') as file:
            source_data = json.load(file)

        print("Loading target data...")
        with open(target_file, 'r') as file:
            target_data = json.load(file)

        updated_data = {}
        print("Updating keys...")
        for key, value in target_data.items():
            new_key = source_data.get(key, key)
            updated_data[new_key] = value

        print("Saving updated data...")
        with open(new_file, 'w') as file:
            json.dump(updated_data, file, indent=4)

        return "Update successful and saved to new file"
    except Exception as e:
        return f"Error: {e}"

# File paths (update these with actual paths)
source_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/keyvalue.json'
target_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/cmp_ref_data.json'
new_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/cmp_ref_data_after_replace_key_trackingFile.json'



# Run the function
result = update_keys(source_file_path, target_file_path, new_file_path)
print(result)



