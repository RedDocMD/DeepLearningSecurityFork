from pathlib import Path
import csv
import shutil

cwd = Path.cwd()
src_root = cwd / "nbaiot_raw"
dest_root = cwd / "nbaiot"

dest_root.mkdir(exist_ok=True)

dev_list_path = src_root / "device_info.csv"
devices = []
with dev_list_path.open() as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
        devices.append((row[0], row[1]))

children = list(src_root.iterdir())

for dev_id, dev_name in devices:
    print("Copying {}".format(dev_name))
    dev_dir = dest_root / dev_name 
    mirai_dir = dev_dir / "mirai"
    gafgyt_dir = dev_dir / "gafgyt"

    mirai_dir.mkdir(parents=True, exist_ok=True)
    gafgyt_dir.mkdir(parents=True, exist_ok=True)

    for child in children:
        name = child.name
        if not name.startswith(dev_id):
            continue
        print("Copying {}".format(name))
        if 'benign' in name:
            shutil.copy(child, dev_dir)
        if 'mirai' in name:
            shutil.copy(child, mirai_dir)
        if 'gafgyt' in name:
            shutil.copy(child, gafgyt_dir)
