from setuptools import setup, find_packages

setup(
    name="openCleanlib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openclean",
        "pandas"
    ],
    author="Andrei Portugal,... ",
    author_email="andrei.torres@aluno.uece.br,...",
    description="Uma biblioteca para limpeza, transformação e wrangling de dados usando OpenClean",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/...",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
