import config
import datetime
import os
import shutil
import until

start_time = datetime.datetime.now()


out_dir = config.out_dir
init_dir_name = config.init_dir_name
copy_path = config.copy_path
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
    for path in copy_path:
        if os.path.isdir(path):
            shutil.copytree(
                os.path.join(process_dir, path),
                os.path.join(out_dir, path),
                dirs_exist_ok=True,
            )
        else:
            shutil.copyfile(
                os.path.join(process_dir, path),
                os.path.join(out_dir, path),
            )


def clear_config_comment():
    print("Start clearing config comment…")

    clear_functions = [
        lambda src=src, dest=dest: until.clear_comment(src, dest)
        for src, dest in config.config_file_clear.items()
    ]
    until.run_in_threads(clear_functions)

    print("End clearing config comment")


def build_form_dnsmasq_china_list():
    import build_form_dnsmasq_china_list

    build_form_dnsmasq_china_list.build(config.dnsmasq_china_list, out_ruleset_dir)


def build_smartdns_guard_rule():
    print("Start building smartdns guard rule…")
    with open(os.path.join(ruleset_dir, "Guard.conf"), "r", encoding="utf-8") as f:
        content = f.readlines()

    filtered = []

    filtered = [
        line.replace(".", "", 1) if line.startswith(".") else line
        for line in content
        if not line.startswith("#") and line.strip()
    ]

    with open(
        os.path.join(out_ruleset_dir, "smartdns", "Guard.txt"), "w", encoding="utf-8"
    ) as f:
        f.write("".join(filtered))

    print("End building smartdns guard rule")


def build_form_misakaio_chnroutes2():
    import build_form_misakaio_chnroutes2

    build_form_misakaio_chnroutes2.build(config.misakaio_chnroutes2, out_ruleset_dir)


init()
copy_files()
# clear_config_comment()
# build_form_dnsmasq_china_list()
# build_smartdns_guard_rule()
# build_form_misakaio_chnroutes2()

until.run_in_threads(
    [
        clear_config_comment,
        build_form_dnsmasq_china_list,
        build_smartdns_guard_rule,
        build_form_misakaio_chnroutes2,
    ]
)

end_time = datetime.datetime.now()

print(f"Total time: {end_time - start_time}")
