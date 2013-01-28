#!/usr/bin/env python2.7
# encoding: utf-8
import datetime
import os.path
import logging
import cmd

# requirements.txt
import doko

# CHANGE THE USER directory
# For example on a mac if the username is foobar
# ROOT = "/Users/foobar/Documents/"
ROOT = "MyPathToChange/"
NOTENAME = "notes.md"


def todaynotepath(rootpath, notename):
    isodate = datetime.date.today().isoformat()
    isodate.replace("-", "/")
    return rootpath + isodate.replace("-", "/") + "/%s" % (notename)


def addcontent(content):
    logging.info(content)


class NoteBook(cmd.Cmd):
    """Simple cli notebook."""
    prompt = "log> "

    def precmd(self, line):
        # What is the date path NOW
        notepath = todaynotepath(ROOT, NOTENAME)
        # if the directory of the note doesn't exist, create it.
        notedir = os.path.dirname(notepath)
        if not os.path.exists(notedir):
            os.makedirs(notedir)
        # if the file for notes today doesn't exist, create it.
        logging.basicConfig(filename=notepath,
                            level=logging.INFO,
                            format='%(asctime)s - %(message)s')
        return cmd.Cmd.precmd(self, line)

    def do_here(self, keyword):
        "return the location on here"
        if keyword:
            # should convert a keyword into the location info
            # to define
            pass
        else:
            location = doko.location()
            latitude = location.latitude
            longitude = location.longitude
            print u'location= %s,%s' % (latitude, longitude)
            logging.info("Location: {latitude}, {longitude}".format(
                latitude=latitude,
                longitude=longitude
                ))

    def default(self, line):
        if line:
            print datetime.date.today().isoformat(), line
            addcontent(line)

    def do_EOF(self, line):
        return True

    def postloop(self):
        print

if __name__ == "__main__":
    NoteBook().cmdloop()
