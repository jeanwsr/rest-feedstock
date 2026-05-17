import os
import pathlib
import shutil
import subprocess


recipe_dir = os.environ.get("RECIPE_DIR")
if not recipe_dir:
    raise RuntimeError("RECIPE_DIR is not set")

script = pathlib.Path(recipe_dir) / "build.sh"
if not script.is_file():
    raise FileNotFoundError(f"Build script not found: {script}")

print(f"Running build script: {script}")

bash_cmd = "bash"
if os.name == "nt":
    program_files = pathlib.Path(os.environ.get("ProgramFiles", r"C:\Program Files"))
    candidates = [
        program_files / "Git" / "bin" / "bash.exe",
        pathlib.Path(os.environ.get("BUILD_PREFIX", "")) / "Library" / "usr" / "bin" / "bash.exe",
    ]
    for candidate in candidates:
        if candidate.is_file():
            bash_cmd = str(candidate)
            break
    else:
        bash_cmd = shutil.which("bash") or "bash"

try:
    script_arg = script.as_posix() if os.name == "nt" else str(script)
    subprocess.run([bash_cmd, script_arg], check=True)
except FileNotFoundError as exc:
    raise RuntimeError(f"Failed to execute build script: bash not found ({bash_cmd}). Ensure bash is installed and available in PATH.") from exc
except subprocess.CalledProcessError as exc:
    raise RuntimeError(f"Failed to execute build script: build.sh exited with code {exc.returncode}") from exc
