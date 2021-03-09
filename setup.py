from pathlib import Path
from setuptools import setup, find_packages


root = Path(__file__).parent.resolve()
with (root / "README.md").open() as file:
    long_description = file.read()
with (root / "requirements.txt").open() as file:
    install_requires = [l.strip() for l in file.readlines()]

setup(
    name="gw2apy",
    version="0.0.1",
    description="Guild Wars 2 API Python Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Guillaume Rochette",
    author_email="rochette.guillaume@gmail.com",
    url="https://github.com/GuillaumeRochette/gw2apy/",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },
    project_urls={
        "Bug Reports": "https://github.com/GuillaumeRochette/gw2apy/issues",
        "Source": "https://github.com/GuillaumeRochette/gw2apy/",
    },
    options={"bdist_wheel": {"universal": True}},
)
