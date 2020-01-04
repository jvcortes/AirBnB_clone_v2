#!/usr/bin/python3
"""
Fabric file for task 3.
"""
import os
from datetime import datetime
from fabric.api import env, put, run, local, runs_once


env.hosts = ['35.237.10.249', '35.237.191.203']
env.key_filename = "~/.ssh/holberton"
env.user = "ubuntu"


def deploy():
    """
    Generates a new package of web_static and deploys its contents into
    production.
    """

    filepath = do_pack()
    if not filepath:
        return False

    return do_deploy(filepath)


def do_deploy(archive_path):
    """
    Deploys the contents of a web_static TGZ into a production server.
    """

    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    put(archive_path, "/tmp/")

    run("mkdir -p /data/web_static/releases/{}".format(filename.split(".")[0]))
    if run("tar -xzf \"/tmp/{}\" -C /data/web_static/releases/{}".format(
            filename,
            filename.split(".")[0])).failed:
        return False

    if run("rm /tmp/{}".format(filename)).failed:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}".format(filename.split(".")[0],
                                                 filename.split(".")[0])
           ).failed:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".format(
            filename.split(".")[0])).failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False

    if run("ln -s /data/web_static/releases/{} "
           "/data/web_static/current".format(
               filename.split(".")[0])).failed:
        return False

    return True


@runs_once
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
