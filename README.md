to make the bot read the chat to you!

python2 bot.py | espeak
------------------------------------------------
HOW TO: on UBUNTU STUDIO Version 20.04.4 LTS Focal Fossa (Xfce Desktop)
------------------------
sudo apt install python2
sudo apt install pip2
-------------------------------------
pip2 install websocket-client==0.48.0
pip2 install beautifulsoup4==4.6.1
--
OR
-------------------------------------------------------
https://pypi.org/project/websocket-client/0.48.0/#files
https://pypi.org/project/beautifulsoup4/4.6.1/#files
-
https://files.pythonhosted.org/packages/8e/37/84b216b36760d157ea81ad7cba48ba2052abe54c604784e7b04668fcb281/beautifulsoup4-4.6.1.tar.gz
https://files.pythonhosted.org/packages/28/85/df04ec21c622728316b591c2852fd20a0e74324eeb6ca26f351844ba815f/websocket_client-0.48.0.tar.gz
-----------------------------------
ls ~/Downloads
cd ~/Downloads
tar -xf beautifulsoup4-4.6.1.tar.gz
tar -xf websocket_client-0.48.0.tar.gz
cd websocket_client-0.48.0
python2 setup.py install
OR
python2 setup.py
cd ..
cd beautifulsoup4-4.6.1
python2 setup.py install
--------------------------------------
THEN
-----------------------------------------
pip2 install2 requests colorama simplejson`
---
AND
--------------------------------------------------------------------------------------------
OPEN YOUR WEB BROWSER, TYPE CTRL + SHIFT + N on CHROME or OPERA, CTRL + SHIFT + P on FIREFOX
GO TO: tinychat.com/logout
LOGIN YOUR BOT ACCOUNT
GO TO THE ROOM WHERE THE BOT WILL BE JOINING
REFRESH THE CHAT 5 TIMES UNTIL YOU GET THE CAPTCHA, AND CAN SEE THE CAMERAS
CLOSE THE WEB BROWSER

Ls ~/
ls ~/Downloads
ls $HOME
ls $home\Downloads
cd ~/bot2
python2 bot.py

windows? not using pip2... no need. just regular pip!
MAKE SURE YOU INSTALL PYTHON 2.7.1(6?) AS IT HAS THE PYTHON PATH AUTOMATICALLY ADDED TO THE DOS PROMPT!



























------------------------------- old tut -----------------------------------------
## Nortbot

A bot for Tinychat chat rooms.

This started out with some improvements to a few files for the bot in the room I go to. This basically led to a complete rewrite of almost everything.


## Setup
For a Windows user that wants a bot without having to deal with the Python aspect, I have provided a compiled Windows executable in the [**Releases**](https://github.com/nortxort/nortbot/releases) section.

It is somewhat based on pinylib-rtc/tinybot-rtc so Python 2.7.16+ is required. It has been tested on Windows 10, Debian 9/10, and Ubuntu 16/18/19.


### Requirements

[Requirements.txt](https://github.com/nortxort/nortbot/blob/master/requirements.txt) contains a list of requirements which can be installed with `pip install -r /path/to/requirements.txt`


## Usage

Change [config.ini](https://github.com/nortxort/nortbot/blob/master/config.ini) settings to fit your needs. ***Don’t forget to change the default key!*** Then run `nortbot.py`. 

For a detailed explanation of the different config settings, read through the [**config settings**](https://github.com/nortxort/nortbot/blob/master/CONFIG.md).

Command explanations can be found [**HERE**](https://github.com/nortxort/nortbot/blob/master/COMMANDS.md).


## Compiling

In order to compile simply run `compile.bat`, located in the `compile` folder. You will need the following:
* Python 2.7.16+ in your path.
* Possibly [Microsoft Visual C++ 2008 Redistributable Package](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en).
* May need elevated permission on first run.

*More details about pyinstaller's requirements can be found [HERE](https://pyinstaller.readthedocs.io/en/v3.3.1/usage.html#windows)*


### Using Pyinstaller

You will need [pyinstaller](http://www.pyinstaller.org/), it can be installed with the following command: `pip install pyinstaller` 

Next, change directory to the directory containing the source code: `cd path/to/source/code/files` 

from there run: `pyinstaller --onefile nortbot.py`.

2 new directories will be created, build and dist. The **dist** directory will contain **nortbot.exe**. Copy **cacert.pem** and **config.ini** to the **dist** directory.

You can now run `nortbot.exe`!


## Submitting an issue

Please read through the [ISSUES](https://github.com/nortxort/nortbot/issues) before submitting a new one. If you want to submit a new issue, then use an [ISSUE TEMPLATE](https://github.com/nortxort/nortbot/issues/new/choose). **_Please_ use an issue template, they're there for a reason!** If you need more help or have questions that are not already answered in the issues, you can [join this Discord server](https://discord.gg/cHawfkb).


## Author

* [nortxort](https://github.com/nortxort)


## License

The MIT License (MIT)
See [LICENSE](https://github.com/nortxort/nortbot/blob/master/LICENSE) for more details.


## Acknowledgments

*Thanks to the following people, who in some way or another, have contributed to this project:*

[Technetium1](https://github.com/Technetium1)

[Aida](https://github.com/Autotonic)
