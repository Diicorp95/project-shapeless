#!/usr/bin/env python3

"""
Shapeless bot for MsgRoom @ Windows96.net

Shapeless bot © Diicorp95. MIT License
Windows 96 © Mikesoft. All rights reserved, except for some parts

Open-Source Part: Configuration API
"""

import base64  # not implemented
import os.path  # not implemented

global con, config_storage_demo
con = {}
config_storage_demo = [
    None,
    "SHAPELESS:CONFIG",
    "silent:MA==",  # 0: Can send messages; 1: Don't return error code ('Learned', 'Error'..., etc.); 2: Completely silent. 'BOTGUESS', 'say(<<text>>)'' and similar commands will be useless.
    "default_name:PT58PD0=",  # Default name.
    "name_lasts:AA==",  # If true, then bot always sets its nickname as in parameter 'name_default'. Default name can be set if user executes command 'BOTNAME-default'
    "prefix:XSNbIA==",  # Prefix when copying name of a user (by their ID) or nickname
]  # example; do not use in real code


def usend(msg):  # In real code it's used only as a command from terminal
    # < ... >
    # progs.received(msg) # not implemented; will be useless here
    if msg[0:6] == "BOTCON":
        if (
            msg[6:7] == " "
            and msg.find("=") > -1
            and not msg[7:8] == "="
            and not msg[-1:] == "="
        ):
            cfg.edit(msg[7 : msg.find("=")], msg[msg.find("=") + 1 :])
    if msg == "BOTSAVECON":
        cfg.save(False)
    if msg == "BOTRESTORECON":
        cfg.restore(False)
    # < ... >


class cfg:
    MAGIC_STRING = "SHAPELESS:CONFIG"
    term = {"homedisk": "/dev/dsk1/"}  # not implemented
    default_config_location = os.path.join(term["homedisk"], "/shapeless.config")

    def edit(variable, value, system=False):
        if not system:
            try:
                if int(con["silent"]) > 1:
                    sendmsg("Learned")  # demo
            except ValueError:
                raise ValueError("Unstable config")
            except NameError:
                return 2
            except KeyError:
                con["silent"] = 0
        con[variable] = value
        if not system:
            sendterm(
                BM
                + "Changed value"
                + NC
                + " of "
                + BC
                + variable
                + NC
                + " to "
                + BC
                + value
                + NC,
                "config",
            )
        else:
            sendterm("Value of " + BC + variable + NC + " is loaded", "config")
        return 1

    def encode(a):
        return str(base64.b64encode(a.encode("utf-8")), "utf-8")

    def decode(a):
        try:
            return str(base64.b64decode(a), "utf-8")
        except Exception:
            return 1

    # def restore(absolute_path = None):
    # if absolute_path is None:
    # absolute_path = cfg.default_config_location
    def restore(system=False):
        sendmsg("...")
        # x = fs.readlines(cfg.default_config_location,_) # example; do not comment this line in real code
        # if isinstance(x,int) and x < 1: # example; do not comment this line in real code
        # return 1 # example; do not comment this line in real code
        _ = config_storage_demo  # example; do not use in real code
        if _[0] > 15:
            if _[1] == cfg.MAGIC_STRING:
                for i, s in enumerate(_):
                    if i > 0:
                        x = s.find(":")
                        if x == -1:
                            continue
                        cfg.edit(s[0:x], cfg.decode(s[x + 1 :]), system)
        sendmsg("Restored 💾")

    # def save(absolute_path = None):
    # if absolute_path is None:
    # absolute_path = cfg.default_config_location
    def save(system=False):
        sendmsg("...")
        _ = [False, cfg.MAGIC_STRING]
        for i, s in enumerate(con):
            if i > 0:
                try:
                    _.append(str(list(con.keys())[i]) + ":" + cfg.encode(str(s)))
                except KeyError:
                    try:
                        sendterm(
                            "Could not access value of "
                            + BC
                            + list(con.keys())[i]
                            + NC,
                            "config",
                        )
                    except:
                        raise KeyError("Could not access value of a key at config")
                        continue
        # if fs.writelines(cfg.default_config_location,_) < 1: #example; do not comment this line in real code
        sendmsg("Saved 💾")


if __name__ == "__main__":  # demo
    sendmsg = lambda s: print(GC + "Chat + term. : " + NC + s)  # not implemented
    sendterm = (
        lambda s, mgrp="": print(SC + "[Config]" + NC, s)
        if mgrp == "config"
        else print(GC + "Terminal only: " + NC + s)
    )  # not implemented
    BM = "\033[7m"  # demo
    BC = "\033[3m"  # demo
    SC = "\033[0;91m"  # demo
    GC = "\033[0;94m"  # demo
    NC = "\033[0m"  # demo
    config_storage_demo[0] = 0  # exaple; do not use in real code
    for i, s in enumerate(config_storage_demo):  # example; do not use in real code
        config_storage_demo[0] += len(str(s))  # example; do not use in real code
    config_storage_demo[0] += len(
        config_storage_demo
    )  # example; do not use in real code
    cfg.restore(True)  # demo
    usend("BOTCON name_lasts=true")  # demo
    usend("BOTSAVECON")  # demo
