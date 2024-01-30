from winctrl import WinCtrl
import click

@click.command()
def main():
    x = WinCtrl()
    x.remove_demands_attention_by_name_filter(ends_with="Google Chrome")

if __name__ == "__main__":
    main()