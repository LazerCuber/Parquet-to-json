import argparse
import pandas as pd
import json

def convert_parquet_to_json(parquet_file, json_file):
    # Load the parquet file
    df = pd.read_parquet(parquet_file, engine='pyarrow')

    # Convert the DataFrame to JSON format
    json_str = df.to_json(orient='records')

    # Save the JSON to a file with pretty formatting, indent=4
    with open(json_file, 'w') as f:
        json.dump(json.loads(json_str), f, indent=4)
    

    print(f"Success! {parquet_file} has been converted to {json_file}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a Parquet file to a JSON file.')
    parser.add_argument('parquet_file', type=str, help='Path to the Parquet file')
    parser.add_argument('json_file', type=str, help='Path where the JSON file will be saved')

    args = parser.parse_args()
    convert_parquet_to_json(args.parquet_file, args.json_file)
