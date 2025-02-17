from setuptools import setup, find_packages

setup(
    name='metaphlan_taxa_summary',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'metaphlan_summary=metaphlan_taxa_summary.summarize:main',
        ],
    },
    author="Your Name",
    description="A simple tool to summarize MetaPhlAn taxa tables",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/metaphlan_taxa_summary",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
