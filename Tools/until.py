import concurrent.futures
import re


def clear_comment(src_file, dest_file):
    with open(src_file, "r", encoding="utf-8") as src:
        lines = src.readlines()

    cleaned_lines = [
        re.match(r"^[^#]*", line).group(0).rstrip() + "\n" for line in lines
    ]

    cleaned_lines = [line for line in cleaned_lines if line.strip()]

    with open(dest_file, "w", encoding="utf-8", newline="\n") as dest:
        dest.writelines(filter(None, cleaned_lines))

    print(f"[Util] Clearing comments for {src_file}")


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

    with open(dest_file, "w", encoding="utf-8", newline="\n") as file:
        file.writelines(output_lines)

    print(f"[Util] Deduplication for {src_file}")


def run_in_threads(functions):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda f: f(), functions)


if __name__ == "__main__":
    import os
    import sys

    ruleset_dir = os.path.join(os.path.abspath(os.path.dirname(sys.path[0])), "List")

    for root, _, files in os.walk(ruleset_dir):
        for file in files:
            if file.endswith(".conf"):
                file_path = os.path.join(root, file)
                deduplicate(file_path, file_path)
