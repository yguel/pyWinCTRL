from winctrl import WinCtrl
import click

@click.command()
@click.argument('ew',"--title_ends_with", type=str, required=True)
def main(ew : str):
    x = WinCtrl()
    x.remove_demands_attention_by_name_filter(ends_with=ew)

if __name__ == "__main__":
    main()