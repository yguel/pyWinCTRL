# Make all the chrome windows disappear from the task bar of all the desktops by undemanding attention for all of them.

This project was tested only on a linux OS.

When restoring a chrome session with many windows (after a reboot for instance) all the windows appear in a state demanding attention.
\
If you have a multiple workspace setup, with many chrome windows on each workspace, then any window demanding attention appears in the task bar of all workspaces.
\
For instance with a 14 workspaces setup, with 5 chrome windows in each you get 70 minified windows demanding attention in the task bar of all your workspaces.

Then the task bar is unusable since you cannot identify the windows because with so many windows minified only a few pixels are dedicated for each window.
\
It is even hard to click on a specific window.

The only solutions so far were: 
1. to not restore session (and if you have a power failure you are screwed),
2. to not have so many chrome windows in your session (bye bye multi-tasking),
3. click on each window to make it stop demanding attention. And if you have a 14 workspaces setup, with 5 chrome windows in each, you have to click 70 times ... well more than that since the situation is a bit fuzzy. Normally demanding attention windows are supposed to appear in the task bar with the window title in bold. But in this case, with so many windows in the task bar, the title do not appear at all and the windows demanding attention are mixed with windows not demanding attention. Then you have to click at random, expecting to hit a demanding attention window. Worst, some time you click on a window and you are transported to the workspace where the window is, where other non demanding attention windows are and in a totally different order in the task bar from the previous workspace you were in.

As you can read, the best solution so far was a nightmare. 


So I wrote this script to make all the chrome windows stop demanding attention.



## Install

1. Install [poetry](https://python-poetry.org/docs/#installation) using the recommended installation method for your OS. For instance on linux:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
2. Go to the directory where you want to install the script and run the following command:
```bash
poetry install
```
3. Create a bash alias for the script by adding the following line to your `.bashrc` or `.bash_aliases` file:
```bash
alias chrome_offbar="cd where_I_put_this_poetry_project/pyWinCTRL && bash -c '~/.local/bin/poetry run chrome_offbar' && cd - > /dev/null"
```
replacing `where_I_put_this_poetry_project` with the path to the directory where you dowloaded this poetry project.

4. Run the following command to apply the changes:
```bash
source ~/.bashrc
```

## Usage

Run the following command to make all the chrome windows disappear from the task bar of all the desktops by undemanding attention for all of them:
```bash
chrome_offbar
```
### Windows (re)demanding attention AGAIN!
Sometimes running `chrome_offbar` just after restoring the session, windows for which demanding attention was removed, pop up again demanding attention. 
\
Are chrome windows toddlers ?

__Solution__: 
In that case, `visit all the workspaces once` and run the command again.

I suspect that for many windows, chrome does not have time to restore properly the entire session before you run the undemanding attention command, or something special happens with the window manager when a demanding attention window is on a workspace you have not visited yet.

## Note on potential taskbar improvements alternative
A nice way to solve this problem, would be for the taskbar to register the fact that it became unusable and:
1. transform into a menu with all the windows listed in it,
2. add a menu option to make all or certain windows stop demanding attention. It could propose filters, like chrome windows for instance to make it easier to use.
3. propose to make demanding attention windows only appear in the task bar of the workspace where they are.

## Troubleshooting

### Solve sudden error:  ImportError: cannot import name 'appengine' from 'requests.packages.urllib3.contrib' 

It may work great for a while and then suddenly stop working with the following error:
```bash
ImportError: cannot import name 'appengine' from 'requests.packages.urllib3.contrib'
```

A solution is to reinstall the `requests-toolbelt` package:
```bash
pip install --upgrade twine requests-toolbelt
```

The cause is that the latest version of ``requests`` does not support ``urllib3 2.0.0``.
\
That may be triggered by changes in versions of ``requests-toolbelt`` and/or ``urllib3``.
\
The question is why ``poetry`` requires to use ``requests`` to run the script, since it is not listed in the ``pyproject.toml`` file.

Credits for the solution:
 - [Robin De Schepper on stackoverflow](https://stackoverflow.com/a/76438881/938287)

Credits for the explanation:
 - [Paul on stackoverflow](https://stackoverflow.com/a/76177575/938287)

### Solve sudden error: ImportError: cannot import name 'Application' from 'cleo' 

Cleo is actually a dependency of poetry.

It means that something is wrong with your poetry installation and that poetry is not installed properly for pyWinCTRL to run.

A solution is to reinstall poetry with the recommended installation method for your OS, then by ensuring that pyWinCTRL uses ```~/.local/bin/poetry``` to run poetry, which is the default path for the recommended installation of poetry, pyWinTRL will be run with the expected poetry binary.

You can ensure that no problematic poetry installation is used by removing the faulty poetry (beware it may brake programs that were using this poetry installation but that would use obsolete installations of poetry).

To uninstall poetry, you can use the following steps:
First looks for the poetry installation path:
```bash
which poetry
```
If you have something different from `~/.local/bin/poetry` for instance:
```bash
/home/myuser/.pyenv/shims/poetry
```
Then proceed as follows:
1. List all pyenv Python versions:
```bash
pyenv versions
```
2. Check which version is currently active:
```bash
pyenv version
```
3. Activate the version you want to uninstall poetry from (e.g. 3.8.2):
```bash
pyenv shell 3.8.2
```
4. Show where poetry is installed on this version to confirm it is the same version you got from the `which poetry` command:
```bash
pip show poetry
```
5. Once you have confirmation that it is the version of poetry you need to uninstall, uninstall poetry:
```bash
pip uninstall poetry
```

Then (re)install poetry using the recommended installation method for your OS.
For instance on linux:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
