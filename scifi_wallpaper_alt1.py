#! /bin/python3
'''`scifi_wallpaper` module contains methods for setting background image, \
along with the mode. Help: $ python3 listdir_test.py'''
from os import listdir
from datetime import date
from subprocess import run
import click


SET_DESK_BG = ['gsettings', 'set', 'org.gnome.desktop.background']  # args 1

@click.group(chain=True)  # group the methods
def scifi_wallpaper():
    '''scifi_wallpaper group method.'''

@scifi_wallpaper.command()  # scifi-wallpaper group
def setimg():
    '''Set desktop wallpaper image of the day.'''
    list_imgs = listdir('/home/foo/scripts/scifi_wallpaper/img/')  # img dir
    list_imgs.sort()  # sort filenames d01 thru d31
    img_uri_args = ['picture-uri',
                    'file:///home/foo/scripts/scifi_wallpaper/img/' +
                    list_imgs[date.today().day - 1]]  # args 2
    run(SET_DESK_BG + img_uri_args, check=True)  # run cli args
    print(f'wallpaper img: \x1b[1;34m{list_imgs[date.today().day - 1]}\x1b[0m')

@scifi_wallpaper.command()  # scifi-wallpaper group
def center():
    '''Centered mode for desktop wallpaper image.'''
    args_center = ['picture-options', 'centered']  # args 2
    run(SET_DESK_BG + args_center, check=True)  # run cli args

@scifi_wallpaper.command()  # scifi-wallpaper group
def tile():
    '''Tile mode for desktop wallpaper image.'''
    args_tile = ['picture-options', 'wallpaper']  # args 2
    run(SET_DESK_BG + args_tile, check=True)  # run cli args


if __name__ == '__main__':
    scifi_wallpaper()  # if standalone
