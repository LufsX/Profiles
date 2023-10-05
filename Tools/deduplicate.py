import sys, os

RulesetDir = os.path.join(os.path.abspath(os.path.dirname(sys.path[0])), "List") + "/"


def remove_duplicate_lines(file_path):
    lines_seen = set()
    output_lines = []

    with open(file_path, "r", encoding="utf-8") as file:
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

    with open(file_path, "w",encoding="utf-8") as file:
        file.writelines(output_lines)


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".conf"):
                file_path = os.path.join(root, file)
                remove_duplicate_lines(file_path)


# 处理指定目录下的文件
process_directory(RulesetDir)
