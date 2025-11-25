from setuptools import setup, find_packages

import pathlib

this_dir = pathlib.Path(__file__).parent
readme = (this_dir / "README.md").read_text()

setup(
    name="NagParser",
    version="0.0.51",
    description="Parse realtime Nagios Data from status.dat and objects.cache",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="GPLv3",
    author="Andreas Thienemann",
    author_email="andreas@bawue.net",
    url="https://github.com/ixs/NagParser",
    packages=find_packages(include=["nagparser", "nagparser.*"]),
    python_requires=">=3.6",
    platforms=["any"],
    extras_require={
        "dev": [
            "pytest>=7.0.0,<9.0.0",
            "sphinx>=5.3.0",
        ]
    },
)
