import json

def separate_transcripts_with_same_cmp_ref_geneID(gtf_list):
    processed_dict = {}
    key_counter = 1  # Used for generating unique keys for non-transcript/exon lines

    for line in gtf_list:
        fields = line.split('\t')
        if fields[2] in ['transcript', 'exon']:
            start_position = fields[3] if fields[2] == 'transcript' else start_position
            processed_dict.setdefault(start_position, []).append(line)
        else:
            unique_key = f'unique_key_{key_counter}'
            processed_dict[unique_key] = [line]
            key_counter += 1

    return processed_dict


# Define file paths
cmp_ref_data_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/cmp_ref_data.json'
reference_gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/gene_id_data.json'



# Load JSON files
with open(cmp_ref_data_path, 'r') as file:
    cmp_ref_data = json.load(file)

with open(reference_gtf_path, 'r') as file:
    reference_data = json.load(file)



#  Define a function to find the last key containing a transcript in reference_value
def find_last_transcript_key(reference_value):
    last_transcript_key = None
    for key in reference_value:
        if key.startswith("unique_key_"):
            continue
        # Keep track of the last key with a transcript
        last_transcript_key = key
    return last_transcript_key


with open(cmp_ref_data_path, 'r') as file:
    cmp_ref_data = json.load(file)

with open(reference_gtf_path, 'r') as file:
    reference_data = json.load(file)

# Process each cmp_ref_data, type is key and value
for cmp_ref_full, lines in cmp_ref_data.items():
    cmp_ref = cmp_ref_full.split('.')[0]

    if cmp_ref in reference_data:
        cmp_ref_value = separate_transcripts_with_same_cmp_ref_geneID(lines)
        reference_value = separate_transcripts_with_same_cmp_ref_geneID(reference_data[cmp_ref])

        for cmp_ref_start_position, cmp_ref_lines in cmp_ref_value.items():
            inserted = False
            for reference_start_position, reference_lines in reference_value.items():
                if reference_start_position.isdigit() and int(cmp_ref_start_position) <= int(reference_start_position):
                    # Insert cmp_ref_lines at the found position; each insertion updates the value of reference_value, so the reference_start_position is updated for the next search
                    reference_value[reference_start_position] = cmp_ref_lines + reference_lines
                    inserted = True
                    break
            
            if not inserted:
                # If not inserted at an existing transcript position, append to the end of the last transcript group
                last_transcript_key = find_last_transcript_key(reference_value)
                if last_transcript_key is not None:
                    reference_value[last_transcript_key].extend(cmp_ref_lines)
                else:
                    # Extend the last transcript group with cmp_ref_lines
                    unique_key = f'unique_end_key_{cmp_ref_start_position}'
                    reference_value[unique_key] = cmp_ref_lines

        # Update the original reference_data
        reference_data[cmp_ref] = [line for sublist in reference_value.values() for line in sublist]




updated_reference_gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/updated_gene_id_data.json'
# Save the updated reference data
with open(updated_reference_gtf_path, 'w') as file:
    json.dump(reference_data, file, indent=4)
