# ollama-browser-use
Scripts for running an ollama model locally with browser-use

## Installation 

### Poetry
1) [Set up SSH](https://github.com/TrevorBurgoyne/ollama-browser-use/blob/main/ssh_setup.md)
2) Install [pyenv](https://github.com/TrevorBurgoyne/ollama-browser-use/blob/main/pyenv.md) and [poetry](https://python-poetry.org/docs/#installation)
3) Install package

        >> git clone git@github.com:TrevorBurgoyne/ollama-browser-use.git
        >> cd ollama-browser-use
        >> pyenv install $(cat .python-version)
        >> poetry install
                
4) Set up ``pre-commit`` to ensure all commits to adhere to **black** and **PEP8** style conventions.

        >> poetry run pre-commit install
        
### Conda
It is recommended you install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) over Anaconda for a quicker install time and to save space on unneeded packages. Make sure you install Miniconda for Python 3.X.

1) [Set up SSH](https://github.com/TrevorBurgoyne/ollama-browser-use/blob/main/ssh_setup.md)
2) Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
3) Install package

        >> git clone git@github.com:TrevorBurgoyne/ollama-browser-use.git
        >> cd ollama-browser-use
        >> conda env create -f environment.yaml
        >> conda activate ollama-browser-use-venv
        >> pip install -e .
        
4) Within the conda shell, set up ``pre-commit`` to ensure all commits to adhere to **black** and **PEP8** style conventions.

        >> pre-commit install