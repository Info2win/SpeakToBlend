import os
import subprocess
import sys

def get_python_path():
    python_dir = os.path.join(sys.prefix, 'bin')
    python_files = [i for i in os.listdir(python_dir) if i.startswith("python")]
    
    python = os.path.join(sys.prefix, 'bin', python_files[0])

    return python

def pip_install(packages_names):
    python = get_python_path()
    subprocess.run([python, "-m", "ensurepip"])
    subprocess.run([python, "-m", "pip", "install", "--upgrade", "pip"])

    for package_name in packages_names:        
        subprocess.run([python, "-m", "pip", "install", package_name, '--upgrade'])