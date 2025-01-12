import codecs
import os

from setuptools import find_packages, setup

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "optimesh", "__about__.py"), "rb") as f:
    exec(f.read(), about)


def read(fname):
    return codecs.open(os.path.join(base_dir, fname), encoding="utf-8").read()


setup(
    name="optimesh",
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    packages=find_packages(),
    description="Mesh optimization/smoothing",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url=about["__website__"],
    license=about["__license__"],
    platforms="any",
    install_requires=[
        "meshio",
        "meshplex >= 0.11.2, < 0.12.0",
        "numpy",
        "quadpy",
        "termplotlib",
    ],
    python_requires=">=3",
    extras_require={"all": ["matplotlib"], "png": ["matplotlib"]},
    classifiers=[
        about["__status__"],
        about["__license__"],
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "optimesh = optimesh.cli:main",
            "optimesh-info = optimesh.cli:info",
        ]
    },
)
