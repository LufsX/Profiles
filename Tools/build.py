import config
import os
import shutil
import until


out_dir = config.out_dir
init_dir_name = config.init_dir_name
copy_dir_name = config.copy_dir_name
process_dir = config.process_dir
ruleset_dir = config.ruleset_dir
out_ruleset_dir = config.out_ruleset_dir


def init():
    if os.path.exists(out_dir):
        print("Clear the last generated files…")
        shutil.rmtree(out_dir)
    for dir_name in init_dir_name:
        os.makedirs(os.path.join(out_dir, dir_name))


def copy_files():
    print("Copy files that do not need to be generated…")
    for dir in copy_dir_name:
        shutil.copytree(os.path.join(process_dir, dir), os.path.join(out_dir, dir))
    shutil.copyfile(
        os.path.join(process_dir, "vercel.json"), os.path.join(out_dir, "vercel.json")
    )


def clear_config_comment():
    for src_file, dest_file in config.config_file_clear.items():
        until.clear_comment(src_file, dest_file)


def build_form_dnsmasq_china_list():
    import build_form_dnsmasq_china_list

    build_form_dnsmasq_china_list.build(config.dnsmasq_china_list, out_ruleset_dir)


def build_smartdns_guard_rule():
    with open(os.path.join(ruleset_dir, "Guard.conf"), "r", encoding="utf-8") as f:
        content = f.readlines()

    filtered = []

    for line in content:
        if line.startswith("."):
            filtered.append(line.replace(".", "", 1))
        elif not line.startswith("#") and line != "" and line != "\n":
            filtered.append(line)

    with open(
        os.path.join(out_ruleset_dir, "smartdns", "Guard.txt"), "w", encoding="utf-8"
    ) as f:
        f.write("".join(filtered))


def build_form_misakaio_chnroutes2():
    import build_form_misakaio_chnroutes2

    build_form_misakaio_chnroutes2.build(config.misakaio_chnroutes2, out_ruleset_dir)


init()
copy_files()
clear_config_comment()
build_form_dnsmasq_china_list()
build_smartdns_guard_rule()
build_form_misakaio_chnroutes2()