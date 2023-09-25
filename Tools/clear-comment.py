import os, sys, re

processDir = os.path.join(os.path.abspath(os.path.dirname(sys.path[0])), "Config")

file_mappings = {
    "clash.yaml": "clash-nocomment.yaml",
    "surge.conf": "surge-nocomment.conf",
}

for src_file, dest_file in file_mappings.items():
    with open(os.path.join(processDir, src_file), "r", encoding="utf-8") as src:
        lines = src.readlines()

    cleaned_lines = []

    for line in lines:
        match = re.match(r"^[^#]*", line)
        if match:
            result = match.group(0)
            result = result.rstrip()
            if result:
                cleaned_lines.append(result + "\n")

    with open(os.path.join(processDir, dest_file), "w", encoding="utf-8") as dest:
        dest.writelines(cleaned_lines)
