import json

def parse_gtf_to_dict(file_path):
    gene_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("#"):
                continue  # Skip comment lines
            fields = line.strip().split('\t')
            if len(fields) < 9:
                continue

            gene_id_field = [f for f in fields[8].split(';') if 'gene_id' in f]
            if gene_id_field:
                gene_id = gene_id_field[0].split('"')[1]

                if gene_id not in gene_data:
                    gene_data[gene_id] = []

                gene_data[gene_id].append(line.strip())

    return gene_data

# Path to the GTF file
gtf_path = '/Users/dxu/Documents/axolotlOmics/AmexT_v47-AmexG_v6.0-DD.gtf'
#gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/readyInsert.gtf'
# Parse the GTF file to a dictionary
gene_id_dict = parse_gtf_to_dict(gtf_path)

# Saving the parsed dictionary to a JSON file
output_json_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/gene_id_data.json'
with open(output_json_path, 'w') as json_file:
    json.dump(gene_id_dict, json_file, indent=4)

print(f"Gene ID dictionary saved to {output_json_path}")
