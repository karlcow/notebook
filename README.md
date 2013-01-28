A very simple python script to create a diary of notes on the CLI with one file a day. The purpose would be to add a few commands little by little.

## Usage ##

    python nb.py

In the shell you get a prompt log.

    log>

You can start typing things that will be saved in a dated space. For example, today is 27 January 2013. All entries will be saved into 

    …/2013/01/27/notes.md

Typing 

    log> Moved nb.py to its own repository at https://github.com/karlcow/notebook

will save the following message in notes.md

    2013-01-27 18:50:01,346 - Moved nb.py to its own repository at https://github.com/karlcow/notebook

### help ###

    log> help

    Documented commands (type help `<topic>`):
    ========================================
    here

    Undocumented commands:
    ======================
    EOF  help

    log> help here
    return the current location.
            If a `<keyword>` is given return the location for this key.
    log> 