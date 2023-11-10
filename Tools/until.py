import re
import threading


def clear_comment(src_file, dest_file):
    with open(src_file, "r", encoding="utf-8") as src:
        lines = src.readlines()

    cleaned_lines = []

    for line in lines:
        match = re.match(r"^[^#]*", line)
        if match:
            result = match.group(0)
            result = result.rstrip()
            if result:
                cleaned_lines.append(result + "\n")

    with open(dest_file, "w", encoding="utf-8") as dest:
        dest.writelines(cleaned_lines)


def deduplicate(src_file, dest_file):
    lines_seen = set()
    output_lines = []

    with open(src_file, "r", encoding="utf-8") as file:
        for line in file:
            stripped_line = line.strip()
            if (
                stripped_line == ""
                or stripped_line.startswith("#")
                or stripped_line not in lines_seen
            ):
                output_lines.append(line)
                if stripped_line != "":
                    lines_seen.add(stripped_line)

    with open(dest_file, "w", encoding="utf-8") as file:
        file.writelines(output_lines)

def run_in_threads(functions):
    threads = [threading.Thread(target=lambda f=f: f()) for f in functions]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

if __name__ == "__main__":
    import os
    import sys

    ruleset_dir = os.path.join(os.path.abspath(os.path.dirname(sys.path[0])), "List")

    for root, _, files in os.walk(ruleset_dir):
        for file in files:
            if file.endswith(".conf"):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}")
                deduplicate(file_path, file_path)
