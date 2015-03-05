StickApproach
==============

Why?
--------------

Nearly everyone had sometimes a problem to find something in *Downloads* directory. It is typical that meanwhile using the computer lots of old files and other stuff are in your temporary folders.
StickApproach is a set of small python scripts which helps you to keep personal filesystem clean with the stick approach. It won't offer you a carrot and ask: *could you be so kind and clean up the old files?*. It will remove the files if you won't do anything with it.
Scripts are ready to put them into any scheduler on your system.

CleanUp
--------------

First script *cleanup.py* is for cleaning directory from old files and folders.
If the file in path is older that x days it will change the name of this file TAGoldname (ie. name will be changed to !!!name). This is your last chance to recover this file, because on next run script will remove every file and folder with name with TAG at the beggining.

It takes three parameters:
- -p path to directory
- -t tag sign (default !!!)
- -d how many days file can be safe in path.
