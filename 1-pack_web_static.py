#!/usr/bin/python3
# Packs the contents of web_static into a .tgz file
import os
from datetime import datetime
from fabric import Connection


def do_pack():
    """
    Packs the contents of web_static in a TGZ archive, and stores it inside
    the folder named 'versions'.
    """

    if not os.path.exists("versions/"):
        os.mkdir("versions")

    with Connection('localhost') as c:
        filename = "web_static_{}{}{}{}{}".format(datetime.now().year,
                                                  datetime.now().month,
                                                  datetime.now().day,
                                                  datetime.now().hour,
                                                  datetime.now().minute)
        if c.run("tar -cvzf versions/{} web_static".format(filename)).failed:
            return None
        return "versions/{}".format(filename)
