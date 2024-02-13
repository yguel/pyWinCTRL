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