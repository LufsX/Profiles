import os
import shutil


def build(out_ruleset_dir, out_surge_ruleset_dir):
    print("[Surge] Start copying surge rules...")

    # 确保目标目录存在
    if not os.path.exists(out_surge_ruleset_dir):
        os.makedirs(out_surge_ruleset_dir)

    # 获取所有 .conf 文件
    conf_files = [f for f in os.listdir(out_ruleset_dir) if f.endswith(".conf")]
    copied_count = 0

    # 复制文件
    for filename in conf_files:
        source_file = os.path.join(out_ruleset_dir, filename)
        dest_file = os.path.join(out_surge_ruleset_dir, filename)

        shutil.copyfile(source_file, dest_file)
        copied_count += 1
        print(f"[Surge] Copied {filename} to Surge ruleset directory")

    print(f"[Surge] Completed: {copied_count} files copied to Surge ruleset directory")
    print("[Surge] End copying surge rules")


if __name__ == "__main__":
    import config

    build(config.out_ruleset_dir, config.out_surge_ruleset_dir)
