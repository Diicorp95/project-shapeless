#!/usr/bin/env python3

'''
Shapeless bot for MsgRoom @ Windows96.net

Shapeless bot © Diicorp95. MIT License
Windows 96 © Mikesoft. All rights reserved, except for some parts

Open-Source Part: File System API (excerpt)
'''

import os.path # not implemented

def askterm(s,mgrp):
    s+=' (y/n): '
    if mgrp=="file":
        print(SC+'[File I/O]'+NC+" "+s,end='')
    else:
        print(GC+"Terminal only: "+SC+s,end='')
    x = input();
    return True if x.lower().strip()[0:1] == "y" else False

class fs:
    absp = lambda path:os.path.abspath(path)
    def readlines(path):
        path=abs(path)
        try:
            f = open(path,"r")
        except IOError:
            return 1
        try:
            _ = [ os.path.getsize(path) ]
        except IOError:
            return 1
        try:
            read = f.read().splitlines()
        except IOError:
            return 1    
        ln = 0
        for s in read:
            ln += 1
            _.append(s)
        f.close()
        sendterm("Readed to a list from file: "+path,'file')
        return _ 
    def writelines(path, input_list):
        path=fs.absp(path)
        try:
            f = open(path,"w")
        except IOError:
            return 1
        if input_list[0] == False:
            try:
                for i,s in enumerate(input_list):
                    if i > 0:
                        f.write(s+"\n")
            except IOError:
                return 1
        else:
            for s in input_list:
                try:
                    f.write(s+"\n")
                except IOError:
                    return 1
        f.close()
        sendterm("Saved a list to file: "+path,'file')
        return 0
    def delete(path,ask=True):
        path=fs.absp(path)
        try:
            with open(path,"w") as f:
                f.write('')
        except IOError:
            return 1
        try:
            if ask or not (askterm('Remove file: '+path+'?','file')):
                return 2
            if os.path.isdir(path): raise IsADirectoryError
            os.unlink(path)
        except IsADirectoryError:
            if ask or not askterm('Remove directory: '+path+'?','file'):
                return 2
            shutil.avoids_symlink_attacks = False
            try:
                shutil.rmtree(path)
            except Exception as e:
                return e
        except:
            return 1
        return 0
    def mkdir(path):
        path=fs.absp(path)
        if os.path.isdir(path):
            try:
                os.mkdir(path)
            except:
                return 1
            sendterm("Created directory: "+path,'file')
        else:
            return 1
    def touch(path):
        path=fs.absp(path)
        try:
            with open(path,"w") as f:
                f.write('')
        except IOError:
            return 1
        sendterm("Created empty file: "+path,'file')

if __name__=="__main__": # demo
    sendmsg=lambda s:print(GC+'Chat + term. : '+NC+s) # not implemented
    sendterm=lambda s,mgrp='':print(SC+'[File I/O]'+NC,s) if mgrp=='file' else print(GC+'Terminal only: '+NC+s) # not implemented
    BM='\033[7m' # demo
    BC='\033[3m' # demo
    SC='\033[0;91m' # demo
    GC='\033[0;94m' # demo
    NC='\033[0m' # demo
    # Test it on yourself!
