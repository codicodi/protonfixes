""" Game fix for FFXIV
"""
#pylint: disable=C0103

from protonfixes import util
import os

def main():
    """ for FFXIV skip intro cutscene to allow game to work.
    """
    util.protontricks('hidewineexports=enable')
    # disable new character intro cutscene to prevent black screen loop
    configpath = os.path.join(util.protonprefix(), 'drive_c/users/steamuser/Documents/My Games/FINAL FANTASY XIV - A Realm Reborn')
    if not os.path.exists(configpath):
        os.makedirs(configpath)
    configgame = os.path.join(configpath, 'FFXIV.cfg')
    if not os.path.isfile(configgame):
        f = open(configgame,"w+")
        f.write("<FINAL FANTASY XIV Config File>\n\n<Cutscene Settings>\nCutsceneMovieOpening 1")
        f.close
    configpath = os.path.join(util.protonprefix(), 'drive_c/users/steamuser/Documents/My Games/FINAL FANTASY XIV - A Realm Reborn')
    if not os.path.exists(configpath):
        os.makedirs(configpath)
    configgame = os.path.join(configpath, 'FFXIV_BOOT.cfg')
    if not os.path.isfile(configgame):
        f = open(configgame,"w+")
        f.write("<FINAL FANTASY XIV Boot Config File>\n\n<Version>\nBrowser 1\nStartupCompleted 1")
        f.close
    # Fixes the startup process.
    if 'NOSTEAM' in os.environ:
        util.replace_command('-issteam', '')
