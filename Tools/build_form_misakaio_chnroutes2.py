import requests, os, datetime


def build(misakaio_chnroutes2, out_dir):
    print("Start build form misakaio chnroutes2…")

    update_info = f'# Updated: {datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}\n'
    content = requests.get(misakaio_chnroutes2).text
    exclude = ["223.118.0.0/15", "223.120.0.0/15", ""]
    lines = []
    for line in content.split("\n"):
        if not line.startswith("#") and not line in exclude:
            lines.append(f"IP-CIDR,{line}\n")
    with open(os.path.join(out_dir, "ChinaIP.conf"), "w") as f:
        f.write(update_info)
        f.writelines(lines)

    print("End building form misakaio chnroutes2")


if __name__ == "__main__":
    import config

    build(config.misakaio_chnroutes2, config.out_ruleset_dir)
