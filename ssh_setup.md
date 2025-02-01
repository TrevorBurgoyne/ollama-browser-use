# SSH Setup

Most libraries depend on private github repositories, and our setup tools use ssh to access them. 
You need to link ssh keys on your computer with your GitHub account in order to install libraries with 
private dependencies. 

## Linux

1) Follow [these](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) instructions.

2) Test your SSH setup with:
    
        ssh -T git@github.com
    
## Windows

1) Install [Git Bash](https://gitforwindows.org/).  (Just click Next until the end)

2) Open Git Bash and run the following. (Hit enter at all prompts).

        ssh-keygen -t ecdsa -b 521
        eval $(ssh-agent -s)
        ssh-add ~/.ssh/id_ecdsa
        
3) Open a Windows Powershell with Administrator privileges. 

    * (Search ``powershell`` in the search bar.  Right click on the Windows Powershell result and select ``Run as administrator``).

4) Within the Powershell run

        Set-Service ssh-agent -StartupType Automatic
        
5) [Add the ssh key to your GitHub account](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account). 
    
    * **Note: Copy the contents of the file ~/.ssh/id_ecdsa.pub instead of ~/.ssh/id_rsa.pub**

6) Test your SSH setup with: (You may have to restart)

        ssh -T git@github.com