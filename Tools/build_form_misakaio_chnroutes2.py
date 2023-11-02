import requests, os


def build(misakaio_chnroutes2, out_dir):
    content = requests.get(misakaio_chnroutes2).text
    exclude = ["223.118.0.0/15", "223.120.0.0/15"]
    lines = []
    for line in content.split("\n"):
        if not line.startswith("#") and not line in exclude:
            lines.append(f"IP-CIDR,{line}\n")
    with open(os.path.join(out_dir, "ChinaIP.conf"), "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    import config

    build(config.misakaio_chnroutes2, config.out_ruleset_dir)
