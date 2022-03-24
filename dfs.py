#!/usr/bin/env python3

"""
Shapeless bot for MsgRoom @ Windows96.net

Shapeless bot © Diicorp95. MIT License
Windows 96 © Mikesoft. All rights reserved, except for some parts

Open-Source Part: Disk File System
"""

global devs, config, GC, lng_devs, NC
devs = ["/dev/ram/"]
"""Always being mounted. Unmount to halt bot activity.
                         Terminal will be still available -- it's possible to
                         send messages, read them, change your nickname, block
                         users, and other actions that terminal API covered."""


def usend(msg):  # In real code it's used only as a command from terminal
    # < ... >
    # progs.received(msg) # not implemented; will be useless here
    if msg == "BOTDISKS":
        dfs.disklist()
    if msg[0:8] == "BOTMOUNT":
        if msg[8:9] == " ":
            dfs.mount(msg[9:])
        else:
            dfs.mount()
    if msg[0:10] == "BOTUNMOUNT":
        if msg[10:11] == " ":
            dfs.unmount(msg[11:])
        else:
            dfs.unmount()
    # < ... >


class dfs:
    def disklist():
        will_print = lngt_disks + ": "
        for i, _ in enumerate(devs):
            mntpath = devs[i]
            if i > 0:
                will_print += "; "
            will_print += "[" + str(i) + "] "
            will_print += lng_devs[
                mntpath[5:-1] if not mntpath[-2:-1].isdigit() else mntpath[5:-2]
            ]
            if mntpath[-2:-1].isdigit():
                will_print += " " + mntpath[-2:-1]
            will_print += " (" + mntpath + ")"
        sendmsg(will_print)

    def mount(mntpath=None):
        if mntpath is None:
            skipped = 0
            for i, _ in enumerate(devs):
                # if not devices.present(devs): # not implemented; will be useless here
                if devs[i] == "/dev/cd2/":  # demo
                    try:
                        devices.new(devs[i])
                    except Exception as e:
                        skipped += 1
                        errors = {""}
            sendmsg("Mounted " + str(skipped) + " skipped devices.")
            if skipped > 0:
                errors = list(errors)
                for i, _ in enumerate(errors):
                    errs = errors[i]
                    try:
                        sendterm("Could not mount " + errs[0] + ": " + list(errs[1]))
                    except:
                        pass
            return 0
        mntpath = mntpath.lower()
        if (
            (mntpath[0:5] == "/dev/")
            and (mntpath[-1:] == "/")
            and not (mntpath in devs)
        ):
            try:
                devs.append(mntpath)
                # devices.new(mntpath) # not implemented; will be useless here
                sendmsg(lng_md)
                sendterm("Mounted by user: " + mntpath)
            except:
                return 1
            return 0

    def unmount(mntpath=None):
        if mntpath is None:
            skipped = 0
            for i, _ in enumerate(devs):
                # if not devices.present(devs): # not implemented; will be useless here
                if False:  # demo
                    try:
                        devices.remove(devs[i])
                    except Exception as e:
                        skipped += 1
                        errors[devs[i]]
            sendmsg("Unmounted " + str(skipped) + " skipped devices.")
            if skipped > 0:
                errors = list(errors)
                for i, _ in enumerate(errors):
                    errs = errors[i]
                    try:
                        sendterm("Could not mount " + errs[0] + ": " + list(errs[1]))
                    except:
                        pass
            return 0
        mntpath = mntpath.lower()
        if (mntpath[0:5] == "/dev/") and (mntpath[-1:] == "/") and (mntpath in devs):
            try:
                devs.remove(mntpath)
                # devices.detach(mntpath) # not implemented; will be useless here
                sendmsg(lng_umd)
                sendterm("Dismounted by user: " + mntpath)
            except:
                return 1
            return 0


if __name__ == "__main__":  # demo

    def sendmsg(s):
        return print(GC + "Chat + term. : " + NC + s)  # not implemented

    def sendterm(s):
        return print(GC + "Terminal only: " + NC + s)  # not implemented

    config = {
        "lang_dfs_devs": {
            "ram": "RAM",
            "fdd": "Floppy Drive",
            "disk": "Fixed Disk",
            "cd": "CD-ROM Drive",
        },
        "lang_dfs_mounted": "Mounted successfully.",
        "lang_dfs_unmounted": "Unmounted successfully.",
        "lang_dfs_disklist_disks": "Disks",
    }  # not implemented
    lng_devs = config["lang_dfs_devs"]  # example
    lng_md = config["lang_dfs_mounted"]  # example
    lng_umd = config["lang_dfs_unmounted"]  # example
    lngt_disks = config["lang_dfs_disklist_disks"]  # example
    GC = "\033[0;94m"  # demo
    NC = "\033[0m"  # demo
    usend("BOTMOUNT /dev/disk1/")  # demo
    usend("BOTMOUNT /dev/fdd3/")  # demo
    usend("BOTDISKS")  # demo
    usend("BOTUNMOUNT /dev/fdd3/")  # demo
    devs.append("/dev/cd2/")  # demo
    usend("BOTMOUNT")  # demo
    usend("BOTDISKS")  # demo
