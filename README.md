# ollama-browser-use
Scripts for running an ollama model locally with browser-use

## Installation

### Google Chrome
1) Download [here](https://www.google.com/chrome/)

### Ollama
1) Download [Ollama](https://ollama.com/)
2) Run the installer
3) Open the command prompt and pull the desired model:

        >> ollama pull qwen2.5

### Poetry
1) [Set up SSH](https://github.com/TrevorBurgoyne/ollama-browser-use/blob/main/ssh_setup.md)
2) Install [pyenv](https://github.com/TrevorBurgoyne/ollama-browser-use/blob/main/pyenv.md) and [poetry](https://python-poetry.org/docs/#installation)
3) Install package

        >> git clone git@github.com:TrevorBurgoyne/ollama-browser-use.git
        >> cd ollama-browser-use
        >> pyenv install $(cat .python-version)
        >> poetry install
        >> playwright install
                
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
        >> playwright install
        
4) Within the conda shell, set up ``pre-commit`` to ensure all commits to adhere to **black** and **PEP8** style conventions.

        >> pre-commit install


## Usage

1) Activate virtual environment

        >> conda activate ollama-browser-use-venv

2) Run the `main.py`

        >> python ollama_browser_use/main.py