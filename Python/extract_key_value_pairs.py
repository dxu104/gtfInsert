import json

def extract_key_value(input_file, output_file):
    # Dictionary to store the key-value pairs
    key_value_pairs = {}

    # Read the input file
    with open(input_file, 'r') as file:
        for line in file:
            # Split the line at the '|' symbol
            parts = line.split('|')
            if len(parts) >= 2:
                # The value is the part before the '|', and the key is the part after '|', up to the first whitespace
                value = parts[0].split()[-1]
                key = parts[1].split()[0]
                key_value_pairs[key] = value

    # Write the dictionary to the output file in JSON format
    with open(output_file, 'w') as file:
        json.dump(key_value_pairs, file, indent=4)

    return key_value_pairs

# Specify the input and output file paths
input_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/null.tracking'
output_file_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/keyvalue.json'

# Call the function and get the result
extracted_data = extract_key_value(input_file_path, output_file_path)
extracted_data
