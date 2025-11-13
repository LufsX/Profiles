import os
import requests
import datetime


def generate_file_tree_html(public_dir, base_url="."):
    def get_file_size(filepath):
        size = os.path.getsize(filepath)
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} TB"

    def scan_directory(dir_path, relative_path=""):
        items = []
        try:
            entries = sorted(os.listdir(dir_path))
            for entry in entries:
                if entry.startswith(".") or entry == "index.html":
                    continue

                full_path = os.path.join(dir_path, entry)
                rel_path = (
                    os.path.join(relative_path, entry) if relative_path else entry
                )

                if os.path.isdir(full_path):
                    items.append(
                        {
                            "type": "dir",
                            "name": entry,
                            "path": rel_path,
                            "items": scan_directory(full_path, rel_path),
                        }
                    )
                else:
                    items.append(
                        {
                            "type": "file",
                            "name": entry,
                            "path": rel_path,
                            "size": get_file_size(full_path),
                        }
                    )
        except Exception as e:
            print(f"Error scanning {dir_path}: {e}")
        return items

    def get_default_expand_state(path_parts, level):
        """
        Config: expanded
        List: level 0 expanded, level 1 collapsed
        Mock: collapsed
        Module: level 0 expanded, level 1 collapsed
        Script: collapsed
        """
        if not path_parts:
            return True

        top_dir = path_parts[0]

        if top_dir == "Config":
            return True  # Config expanded
        elif top_dir == "List":
            return level == 0  # List only expanded at level 0
        elif top_dir == "Mock":
            return False  # Mock collapsed
        elif top_dir == "Module":
            return level == 0  # Module only expanded at level 0
        elif top_dir == "Script":
            return False  # Script collapsed
        else:
            return True

    def generate_html_tree(items, level=0, path_parts=[]):
        html_lines = []
        html_lines.append('<ul class="file-tree">')

        for item in items:
            if item["type"] == "dir":
                current_path_parts = path_parts + [item["name"]]
                dir_id = f"dir-{item['path'].replace(os.sep, '-').replace('.', '-')}"

                is_expanded = get_default_expand_state(current_path_parts, level)

                expand_class = "expanded" if is_expanded else ""
                display_style = "" if is_expanded else "display: none;"

                html_lines.append(f'<li class="folder {expand_class}">')
                html_lines.append(
                    f'<span class="folder-name" onclick="toggleFolder(\'{dir_id}\')">'
                )
                html_lines.append(
                    f'<span class="folder-icon">📁</span> <strong>{item["name"]}/</strong>'
                )
                html_lines.append("</span>")
                html_lines.append(
                    f'<div id="{dir_id}" class="folder-content" style="{display_style}">'
                )
                html_lines.extend(
                    generate_html_tree(item["items"], level + 1, current_path_parts)
                )
                html_lines.append("</div>")
                html_lines.append("</li>")
            else:
                file_url = f"{base_url}/{item['path'].replace(os.sep, '/')}"
                html_lines.append('<li class="file">')
                html_lines.append(f'<span class="file-icon">📄</span> ')
                html_lines.append(
                    f'<a href="{file_url}" target="_blank">{item["name"]}</a> '
                )
                html_lines.append(f'<code class="file-size">{item["size"]}</code>')
                html_lines.append("</li>")

        html_lines.append("</ul>")
        return html_lines

    file_tree = scan_directory(public_dir)

    html_content = "\n".join(generate_html_tree(file_tree))

    return html_content


def build_file_list_page(public_dir, output_path, base_url=".", github_token=None):
    print("[Web] Start building file list page...")

    template_path = os.path.join(os.path.dirname(__file__), "web_index_template.md")
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    update_time = (
        datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)
    ).strftime("%Y-%m-%dT%H:%M:%S") + "+08:00"

    md_content = template_content.replace("{{UPDATE_TIME}}", update_time)

    github_api_url = "https://api.github.com/markdown"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"

    payload = {"text": md_content}

    response = requests.post(github_api_url, headers=headers, json=payload)

    if response.status_code == 200:
        html_content = response.text
    else:
        print(f"[Web] GitHub API request failed, status code: {response.status_code}")
        print(f"[Web] Error message: {response.text}")
        return

    file_tree_html = generate_file_tree_html(public_dir, base_url)

    html_content = html_content.replace("{{FILE_TREE}}", file_tree_html)

    html_template_path = os.path.join(
        os.path.dirname(__file__), "web_index_template.html"
    )
    with open(html_template_path, "r", encoding="utf-8") as f:
        html_template = f.read()

    full_html = html_template.replace("{{CONTENT}}", html_content)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as html_file:
        html_file.write(full_html)

    print(f"[Web] File list page generated: {output_path}")
    print("[Web] End building file list page")


if __name__ == "__main__":
    import config

    public_dir = config.out_dir
    output_path = os.path.join(public_dir, "index.html")

    build_file_list_page(public_dir, output_path)
