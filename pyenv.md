# Pyenv Install

``pyenv`` is a really nice way to manage/install specific Python versions on Linux systems.

## Linux

1) Make sure you install the [build dependencies](https://github.com/pyenv/pyenv/wiki/Common-build-problems#prerequisites) 
for your system.

2) Run

        curl https://pyenv.run | bash

3) Restart your shell so the path changes take effect.

        exec $SHELL

4) Install a specific Python version (e.g. 3.8.3) with

        pyenv install 3.8.3
        
## Mac

1) Run 

        brew install pyenv
        
2) Add **pyenv init** to your shell to enable shims and autocompletion. Please make sure ``eval "$(pyenv init -)"`` is placed toward the end of the shell configuration file since it manipulates PATH during the initialization.

3) Restart your shell so the path changes take effect.

        exec $SHELL