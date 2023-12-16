import json

def json_to_gtf(json_path, output_gtf_path):
    # Read the JSON file
    with open(json_path, 'r') as json_file:
        gene_data = json.load(json_file)

    # Create a GTF file from the JSON data
    with open(output_gtf_path, 'w') as gtf_file:
        for gene_id in gene_data:
            for line in gene_data[gene_id]:
                gtf_file.write(line + '\n')

# Paths
# json_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/gene_id_data.json'  # JSON file path
# output_gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/output.gtf'  # Output GTF file path


json_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/updated_gene_id_data.json'  # JSON file path
output_gtf_path = '/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/final_annotation.gtf'  # Output GTF file path
# Convert JSON to GTF
json_to_gtf(json_path, output_gtf_path)

print(f"GTF file created at {output_gtf_path}")
