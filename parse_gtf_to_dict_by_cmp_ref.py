import json

def parse_gtf_to_dict_by_cmp_ref(file_path):
    cmp_ref_data = {}
    with open(file_path, 'r') as file:
       
        current_cmp_ref = None
        for line in file:
            if line.startswith("#"):
                continue  # Skip comment lines
            fields = line.strip().split('\t')
            if len(fields) < 9:
                continue

            # Check if the line is a transcript with cmp_ref
            if fields[2] == "transcript" and 'cmp_ref' in fields[8]:
                cmp_ref_field = [f for f in fields[8].split(';') if 'cmp_ref' in f]
                if cmp_ref_field:
                    current_cmp_ref = cmp_ref_field[0].split('"')[1]
                   # current_cmp_ref = cmp_ref_field[0].split('"')[1].split('.')[0]
                    if current_cmp_ref not in cmp_ref_data:
                        cmp_ref_data[current_cmp_ref] = []

            # Append the line if it belongs to the current transcript
            # this is the key point to keep keep_lines still True,so we can continue to append those exon under one transcript
            #if cop_ref is AMEX60DDU001003602.2 or AMEX60DDU001003602.3 in this case, then we can continue to append those exon under one transcript
            
            cmp_ref_data[current_cmp_ref].append(line.strip())
            
           

    return cmp_ref_data


# Path to the GTF file
gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/readyInsert.gtf'

# Parse the GTF file to a dictionary based on cmp_ref
cmp_ref_dict = parse_gtf_to_dict_by_cmp_ref(gtf_path)

# Saving the parsed dictionary to a JSON file
output_json_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/cmp_ref_data.json'
with open(output_json_path, 'w') as json_file:
    json.dump(cmp_ref_dict, json_file, indent=4)

print(f"Cmp_ref dictionary saved to {output_json_path}")



