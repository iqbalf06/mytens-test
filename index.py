import os
import argparse
import json

def log_grabber():
    parser = argparse.ArgumentParser(description="Grab log files and convert to plaintext or json")
    parser.add_argument("log_file", type=str, help="Path to the log file")
    parser.add_argument("-t", "--type", type=str, choices=["json", "text"], default="text", help="Conversion type")
    parser.add_argument("-o", "--output", type=str, help="Output file path")
    args = parser.parse_args()

    log_file = args.log_file
    conv_type = args.type
    output_file = args.output

    if not os.path.isfile(log_file):
        print("Error: Log file does not exist.")
        return

    with open(log_file, "r") as f:
        log_content = f.read()

    if conv_type == "json":
        log_dict = {"content": log_content}
        log_json = json.dumps(log_dict, indent=4)
        output_content = log_json
    elif conv_type == "text":
        output_content = log_content

    if output_file:
        with open(output_file, "w") as f:
            f.write(output_content)
    else:
        print(output_content)

if __name__ == "__main__":
    log_grabber()
