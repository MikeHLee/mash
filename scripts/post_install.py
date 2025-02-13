import os
import sys
from pathlib import Path

def add_to_path():
    """Add the Python user bin directory to PATH in shell config files."""
    home = str(Path.home())
    py_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    bin_path = f"$HOME/Library/Python/{py_version}/bin"
    path_export = f'\nexport PATH="{bin_path}:$PATH"'
    
    # Common shell config files
    shell_configs = [
        '.zshrc',   # ZSH (default on modern macOS)
        '.bashrc',  # Bash
        '.bash_profile',  # Bash on macOS
    ]
    
    for config in shell_configs:
        config_path = os.path.join(home, config)
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                content = f.read()
                
            # Only add if not already present
            if bin_path not in content:
                with open(config_path, 'a') as f:
                    f.write(path_export)
                print(f"Added PATH export to {config}")

if __name__ == '__main__':
    add_to_path()
