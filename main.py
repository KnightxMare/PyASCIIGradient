from colorama import Back, Fore, Style
from pystyle import *

banner = r'''

██╗  ██╗    ██╗  ██╗    ███╗   ███╗
██║ ██╔╝    ╚██╗██╔╝    ████╗ ████║
█████╔╝      ╚███╔╝     ██╔████╔██║
██╔═██╗      ██╔██╗     ██║╚██╔╝██║
██║  ██╗    ██╔╝ ██╗    ██║ ╚═╝ ██║
╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝     ╚═╝
                                   

'''
System.Size(120, 30)
System.Clear()
Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, interval=0.025, enter=True) 