"""
Maintenance tasks for vocametrix-python.

Usage:
    python tasks.py regenerate          # regenerate low-level client from OpenAPI spec
    python tasks.py regenerate --url URL  # override spec URL
"""

import subprocess
import sys
import shutil
import argparse
from pathlib import Path

GENERATED_DIR = Path("src/vocametrix/_generated")
OPENAPI_GENERATOR = "openapi-python-client"
OPENAPI_GENERATOR_VERSION = "0.28.3"
DEFAULT_SPEC_URL = "https://www.vocametrix.com/openapi.json"
LOCAL_SPEC_FALLBACK = Path("../vocametrix-landing-page/public/openapi.json")


def ensure_generator():
    result = subprocess.run([sys.executable, "-m", "pip", "show", OPENAPI_GENERATOR],
                            capture_output=True)
    if result.returncode != 0:
        print(f"Installing {OPENAPI_GENERATOR}=={OPENAPI_GENERATOR_VERSION}...")
        subprocess.run([sys.executable, "-m", "pip", "install",
                        f"{OPENAPI_GENERATOR}=={OPENAPI_GENERATOR_VERSION}"], check=True)


def regenerate(spec_url: str):
    ensure_generator()

    tmp_out = Path("_generated_tmp")
    if tmp_out.exists():
        shutil.rmtree(tmp_out)

    print(f"Generating client from: {spec_url}")
    cmd = [
        sys.executable, "-m", "openapi_python_client", "generate",
        "--url", spec_url,
        "--output-path", str(tmp_out),
        "--overwrite",
        "--meta", "none",
    ]

    # Fall back to local file if URL fails
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        if LOCAL_SPEC_FALLBACK.exists():
            print(f"URL failed, falling back to local spec: {LOCAL_SPEC_FALLBACK}")
            cmd = [
                sys.executable, "-m", "openapi_python_client", "generate",
                "--path", str(LOCAL_SPEC_FALLBACK),
                "--output-path", str(tmp_out),
                "--overwrite",
                "--meta", "none",
            ]
            subprocess.run(cmd, check=True)
        else:
            print(result.stderr)
            sys.exit(1)

    # Move generated files into _generated/
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    GENERATED_DIR.mkdir(parents=True)

    # With --meta none, openapi-python-client writes the package CONTENTS
    # directly into the output path (api/, models/, client.py, types.py,
    # errors.py, __init__.py, py.typed) — there is no single wrapper package
    # dir. Copy everything across; descending into the first subdir (e.g. api/)
    # would drop models/ and the root modules and break all imports.
    for item in tmp_out.iterdir():
        dest = GENERATED_DIR / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)

    shutil.rmtree(tmp_out)

    # Ensure the marker comment stays
    init = GENERATED_DIR / "__init__.py"
    marker = "# Auto-generated — do not edit. Run `python tasks.py regenerate` to update.\n"
    if init.exists():
        content = init.read_text()
        if not content.startswith("# Auto-generated"):
            init.write_text(marker + content)
    else:
        init.write_text(marker)

    print(f"Done. Generated client written to {GENERATED_DIR}/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    regen = subparsers.add_parser("regenerate")
    regen.add_argument("--url", default=DEFAULT_SPEC_URL)
    args = parser.parse_args()

    if args.command == "regenerate":
        regenerate(args.url)
    else:
        parser.print_help()
