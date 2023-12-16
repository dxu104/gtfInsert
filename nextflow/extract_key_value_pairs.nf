// main.nf
process EXTRACT_KEY_VALUE {

    tag "${meta.id}"
    label 'process_single'

    input:
    tuple val(meta), path(input_file)

    output:
    tuple val(meta), path("*.json"), emit: key_value_json

    when:
    task.ext.when == null || task.ext.when

    script:
    """
    #!/usr/bin/env python3
    import os
    import json

    def extract_key_value(input_file):
        key_value_pairs = {}
        with open(input_file, 'r') as file:
            for line in file:
                parts = line.split('|')
                if len(parts) >= 2:
                    value = parts[0].split()[-1]
                    key = parts[1].split()[0]
                    key_value_pairs[key] = value
        
        return key_value_pairs

    # Generate output JSON file name based on input file
    output_json_name = os.path.basename('${input_file}').replace('.tracking', '_keyvalue.json')

    extracted_data = extract_key_value('${input_file}')
    
    with open(output_json_name, 'w') as json_file:
        json.dump(extracted_data, json_file, indent=4)
    """
}

workflow {
    // Define the input file path
    ch_input_file = Channel.fromPath('/Users/dxu/Documents/compareJoelGTFwithMyGTF/updateGeneID/outputFromGffcompare/null.tracking')

    // Process the file
    key_value_json = EXTRACT_KEY_VALUE(ch_input_file.map { [ [:], it ] })
}
