import subprocess
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # Execute the post-install script
        subprocess.call([sys.executable, 'scripts/post_install.py'])

setup(
    name="mash",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
        "openai>=1.0.0",
        "anthropic>=0.3.0",
        "python-dotenv>=0.19.0",
    ],
    entry_points={
        "console_scripts": [
            "mash=mash.cli:cli",
        ],
    },
    cmdclass={
        'install': PostInstallCommand,
    },
    author="Michael Lee",
    author_email="leemichael289@gmail.com",
    description="MASH - Master Shell for interacting with various LLM providers and other tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MikeHLee/mash",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
