#! /snap/bin/pypy3
'''`scifi_wallpaper.scifi_wallpaper()` gets wallpaper of the day from a
list of image filenames in `img/img.csv`. Then `gsettings` is called to set
tile mode or center the background image.
$ python3 scifi_wallpaper.py --help'''
from csv import reader
from datetime import datetime
from shlex import split
from subprocess import run
import click


@click.group()
@click.option('--background/--no-background', default=False)
def scifi_wallpaper(background):
    '''`scifi_wallpaper()` method gets image of the day from a list of image
filesnames listed in `img/img.csv`:\n
- `$ python3 scifi_wallpaper.py --background center` (centers bg image)\n
- `$ python3 scifi_wallpaper.py --background tile` (sets tile mode)\n
- `$ python3 scifi_wallpaper.py --background artists` (lists artists)'''
    image_database = '/home/foo/scripts/scifi_wallpaper/csv/img.csv'
    with open(image_database) as _file:
        _reader = reader(_file)
        specific_row = [row for i, row in enumerate(_reader, 1)
                        if i == (datetime.now().day)]
        click.echo(f"wallpaper file: \x1b[0;36m{specific_row[0][0]}\x1b[0m")

    cli_args = 'gsettings set org.gnome.desktop.background picture-uri \
file:///home/foo/scripts/scifi_wallpaper/img/' + specific_row[0][0]
    cli_args_list = split(cli_args)
    run(cli_args_list, check=True)

@scifi_wallpaper.command()
def center():
    '''`center()` method centers background image.'''
    centered_args = 'gsettings set org.gnome.desktop.background \
picture-options centered'
    centered_args_list = split(centered_args)
    run(centered_args_list)

@scifi_wallpaper.command()
def tile():
    '''`tile()` method sets background image to tile mode.'''
    tiled_args = 'gsettings set org.gnome.desktop.background picture-options \
wallpaper'
    tiled_args_list = split(tiled_args)
    run(tiled_args_list)

@scifi_wallpaper.command()
def artists():
    '''`artists()` method lists names, titles and locations of artists.'''
    artist_database = '/home/foo/scripts/scifi_wallpaper/csv/artists.csv'
    with open(artist_database) as _file:
        _reader = reader(_file)
        for j in _reader:
            click.echo(f'{j[0]:<20}{j[1]:<20}{j[2]:<20}')


if __name__ == '__main__':
    scifi_wallpaper()
