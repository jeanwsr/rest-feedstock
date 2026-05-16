import glob
import os
import pathlib
import shutil


prefix = pathlib.Path(os.environ["PREFIX"])
target = os.environ.get("TARGET_PLATFORM", os.environ.get("target_platform", ""))
destination = prefix / ("Scripts" if target.startswith("win-") else "bin")
destination.mkdir(parents=True, exist_ok=True)

for source_path in glob.glob("utilities/*.py"):
    source = pathlib.Path(source_path)
    shutil.copy2(source, destination / source.name)
