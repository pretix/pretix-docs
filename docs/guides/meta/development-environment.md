# Development environment 

This article explains how to set up the development environment for working on the pretix documentation and how to run that development environment on a daily basis.
Since this documentation uses the docs-as-code approach, the setup is similar to that of other software development projects. 

!!! Note 
    These instructions were tested using Arch Linux, Bash, and Nano. 
    If you are using a different operating system and software, adapt the commands given here to your own use case. 

## Prerequisites 

In order to contribute to this documentation, you need an SSH key and a GitHub account. 
You need to have the following packages installed: 

 - Git 
 - OpenSSH
 - Python
 - virtualenvwrapper

For instance, if you want to install these packages on Arch Linux or a distro based on Arch Linux, run the following command: 

```
$ pacman -S python python-virtualenvwrapper git openssh 
``` 

## Setting up the development environment 

Setting up the development environment for the pretix documentation involves three steps: setting an environment variable, cloning the Git repository, and preparing a Python environment. 

### Environment variable 

Set your `WORKON_HOME` environment variable to `~/.virtualenvs`. 
There are several ways to do this. 
For instance, if you want to do this using Linux, Bash and nano, run the following command: 

```
$ nano /.bashrc
``` 

Append the following to the file: 

```
export WORKON_HOME=~/.virtualenvs
source /usr/bin/virtualenvwrapper.sh
``` 

Then save the file. 

### Cloning the Git repository

Clone the Git repository: 

```
$ git clone git@github.com:pretix/pretix-docs.git
``` 

### Prepare a Python environment for MkDocs 

Set up a Python environment for MkDocs using the following commands. 
Navigate to the directory to which you cloned the Git repository. 
By default, it should be located at `~/pretix-docs`. 

```
$ cd pretix-docs
``` 

Make a virtual environment for pretix-docs: 

``` 
$ mkvirtualenv pretix-docs
```

Install the Python requirements: 

```
$ pip install -Ur requirements.txt
``` 

## Using the development environment

In order to use development environment for contributing to the pretix documentation, take the following steps. 
Navigate to the directory to which you cloned the Git repository: 

```
$ cd pretix-docs
``` 

Activate the Python environment: 

``` 
$ workon pretix-docs
```

Launch the MkDocs server:

``` 
$ mkdocs serve
```

Open the URL [https://127.0.0.1:8000/](https://127.0.0.1:8000/) in your browser. 
Use your preferred IDE or text editor to work on the docs. 
Saving, creating or moving a file makes the MkDocs server do an update within a few seconds. 