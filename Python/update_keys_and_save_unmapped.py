import json

def update_keys_and_save_unmapped(source_file, target_file, updated_file, unmapped_file):
    try:
        print("Loading source data...")
        with open(source_file, 'r') as file:
            source_data = json.load(file)

        print("Loading target data...")
        with open(target_file, 'r') as file:
            target_data = json.load(file)

        updated_data = {}
        unmapped_data = {}
        print("Updating keys...")
        for key, value in target_data.items():
            if key in source_data:
                # If the key exists in source_data, update the key
                new_key = source_data[key]
                # Use setdefault to append values for the same new_key
                updated_data.setdefault(new_key, []).extend(value)
            # else: 这里的else是没有必要，因为cmp_ref这里attribute意味着一定可以找到map的，如果找不到，cmp_ref就不会存在
            #     # If the key doesn't exist in source_data, save it in unmapped_data
            #     unmapped_data[key] = value

        print("Saving updated data...")
        with open(updated_file, 'w') as file:
            json.dump(updated_data, file, indent=4)

        print("Saving unmapped data...")
        with open(unmapped_file, 'w') as file:
            json.dump(unmapped_data, file, indent=4)

        return "Update successful. Updated data and unmapped data saved."
    except Exception as e:
        return f"Error: {e}"

# File paths (update these with actual paths)



source_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/keyvalue.json'
target_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/cmp_ref_data.json'
updated_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/cmp_ref_data_after_replace_key_trackingFile.json'
unmapped_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/cmp_ref_data_unmapped_after_replace_key_trackingFile.json'
# Run the function
result = update_keys_and_save_unmapped(source_file_path, target_file_path, updated_file_path, unmapped_file_path)
print(result)
