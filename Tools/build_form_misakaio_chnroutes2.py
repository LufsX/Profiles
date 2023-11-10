import requests, os, datetime


def build(misakaio_chnroutes2, out_dir):
    print("Start building from misakaio chnroutes2…")

    update_info = f'# Updated: {datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}\n'
    exclude = {"223.118.0.0/15", "223.120.0.0/15", ""}
    content = requests.get(misakaio_chnroutes2).text

    lines = [
        f"IP-CIDR,{line}\n"
        for line in content.split("\n")
        if line and not line.startswith("#") and line not in exclude
    ]

    with open(os.path.join(out_dir, "ChinaIP.conf"), "w") as f:
        f.write(update_info)
        f.writelines(lines)

    print("End building from misakaio chnroutes2")


if __name__ == "__main__":
    import config

    build(config.misakaio_chnroutes2, config.out_ruleset_dir)
