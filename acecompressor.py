import click
import pathlib
from acedecomp import Decrypter
from acecomp import Encrypter


@click.group()
def main():
    pass


@main.command(help='Decompress ACE Studio project file')
@click.argument('input', metavar='INPUT')
@click.argument('output', metavar='OUTPUT')
def decomp(input: str, output: str):
    input = pathlib.Path(input).resolve()
    output = pathlib.Path(output).resolve()
    assert input.exists(), 'The input file does not exist.'
    decrypter = Decrypter()
    decrypter.decomp_project(input, output)


@main.command(help='Compress ACE Studio project file')
@click.argument('input', metavar='INPUT')
@click.argument('output', metavar='OUTPUT')
def comp(input: str, output: str):
    input = pathlib.Path(input).resolve()
    output = pathlib.Path(output).resolve()
    assert input.exists(), 'The input file does not exist.'
    encrypter = Encrypter()
    encrypter.comp_project(input, output)

if __name__ == '__main__':
    main()