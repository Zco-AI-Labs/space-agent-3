import os
import sys
import subprocess
import shutil

import re

PROJECT_ID = os.getenv("GCP_PROJECT_ID", "hubscape-geap")
LOCATION = os.getenv("GCP_LOCATION", "us-central1")

# Dynamically parse display_name from agents-cli-manifest.yaml
display_name = "custom-agent"
manifest_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agents-cli-manifest.yaml")
if os.path.exists(manifest_path):
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r'^name:\s*["\']?([^"\'\s]+)["\']?', content, re.MULTILINE)
            if match:
                display_name = match.group(1)
    except Exception as e:
        print(f"Warning: Failed to parse manifest name, using default. Error: {e}")

print(f"Deploying {display_name} via native agents-cli...")

agents_cli_path = shutil.which("agents-cli")
if not agents_cli_path:
    venv_bin = os.path.dirname(sys.executable)
    fallback_path = os.path.join(venv_bin, "agents-cli")
    if os.path.exists(fallback_path):
        agents_cli_path = fallback_path
if not agents_cli_path:
    agents_cli_path = "agents-cli"

cmd = [
    agents_cli_path, "deploy",
    "--project", PROJECT_ID,
    "--region", LOCATION,
    "--service-name", display_name,
    "--agent-identity",
    "--no-confirm-project"
]

env = os.environ.copy()
venv_bin = os.path.dirname(sys.executable)
env["PATH"] = f"{venv_bin}{os.path.pathsep}{env.get('PATH', '')}"

print(f"Executing: {' '.join(cmd)}")
subprocess.run(cmd, env=env, check=True)
print("🎉 Deployment completed successfully!")