#!/usr/bin/env python2.7
# encoding: utf-8
import datetime
import os.path
import logging
import cmd
import yaml

# requirements.txt
import doko

# CHANGE ROOT if you want it to be elsewhere
ROOT = os.path.expanduser('~/Documents/')
LANDMARK_FILE = os.path.expanduser('~/.doko_landmarks')
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
        """return the current location.
        If a <keyword> is given return the location for this key."""
        if keyword:
            # convert a keyword into the location info if known
            if os.path.exists(LANDMARK_FILE):
                with open(LANDMARK_FILE, 'r') as f:
                    locationdata = yaml.safe_load(f)
                try:
                    latitude, longitude = locationdata[keyword]
                    logging.info("Location: {latitude}, {longitude}".format(
                        latitude=latitude,
                        longitude=longitude
                        ))
                except Exception, e:
                    print u'location %s unknown' % (e)
        else:
            # adding location through corelocation on MacOSX
            latitude, longitude, source = doko.location('corelocation')
            print u'location= %s,%s' % (latitude, longitude)
            logging.info("Location: {latitude}, {longitude}".format(
                latitude=latitude,
                longitude=longitude
                ))

    def default(self, line):
        if line:
            addcontent(line)

    def do_EOF(self, line):
        return True

    def postloop(self):
        print

if __name__ == "__main__":
    NoteBook().cmdloop()
