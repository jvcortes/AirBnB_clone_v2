#!/usr/bin/python3
"""
Fabric file for task 1.
"""
import os
from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Packs the contents of web_static in a TGZ archive, and stores it inside
    the folder named 'versions'.
    """

    if not os.path.exists("versions/"):
        os.mkdir("versions")

    filename = "web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S")
    )
    if local("tar -cvzf versions/{} web_static".format(filename)).failed:
        return None
    return "versions/{}".format(filename)
