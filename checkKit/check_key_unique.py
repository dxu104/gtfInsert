import json
def check_unique_keys(json_file):
    try:
        # Load the JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)

        # Check if all keys are unique
        keys = list(data.keys())
        if len(keys) == len(set(keys)):
            return True  # All keys are unique
        else:
            return False  # Some keys are duplicated
    except Exception as e:
        return str(e)

# Since I cannot access the file system, I'll provide this function for you to use in your environment.
# You can run this function with the path to your JSON file to check if all keys are unique.


json_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/cmp_ref_data.json'
are_keys_unique = check_unique_keys(json_file_path)
print("Are all keys unique?", are_keys_unique)
