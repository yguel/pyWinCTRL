# Make all the chrome windows disappear from the task bar of all the desktops by undemanding attention for all of them.

## Install

1. Go to the directory where you want to install the script and run the following command:
```bash
poetry install
```
2. Create a bash alias for the script by adding the following line to your `.bashrc` or `.bash_aliases` file:
```bash
alias chrome_offbar="cd where_I_put_this_poetry_project/pyWinCTRL && bash -c 'poetry run chrome_offbar' && cd -"
```
replacing `where_I_put_this_poetry_project` with the path to the directory where you dowloaded this poetry project.

3. Run the following command to apply the changes:
```bash
source ~/.bashrc
```

## Usage

Run the following command to make all the chrome windows disappear from the task bar of all the desktops by undemanding attention for all of them:
```bash
chrome_offbar
```

## Troubleshooting

### Solve sudden error:  ImportError: cannot import name 'appengine' from 'requests.packages.urllib3.contrib' 

It may works great for a while and then suddenly stop working with the following error:
```bash
ImportError: cannot import name 'appengine' from 'requests.packages.urllib3.contrib'
```

A solution is to reinstall the `requests-toolbelt` package:
```bash
pip install --upgrade twine requests-toolbelt
```

The cause is that the latest version of ``requests`` does not support ``urllib3 2.0.0``.
That may be triggered by changed of versions of ``requests-toolbelt`` and/or ``urllib3``
The question is why ``poetry`` requires to use ``requests`` to run the script, since it is not listed in the ``pyproject.toml`` file.

Credits for the solution:
 - [Robin De Schepper on stackoverflow](https://stackoverflow.com/a/76438881/938287)

Credits for the explanation:
 - [Paul on stackoverflow](https://stackoverflow.com/a/76177575/938287)