from setuptools import setup, find_packages

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
    author="Your Name",
    author_email="your.email@example.com",
    description="Master Shell - A unified CLI for interacting with LLMs and other tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mash",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
