import json

def count_keys_in_json_file(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        return len(data.keys())
    except Exception as e:
        return f"An error occurred: {e}"

# Use the function with your JSON file
json_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/cmp_ref_data.json'  # Replace this with the path to your JSON file
total_keys = count_keys_in_json_file(json_file_path)
print(f"Total number of keys: {total_keys}")
