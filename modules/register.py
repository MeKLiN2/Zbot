# User Level Registration
# Banned Account Check
# VIP Mode Check
# Guest Mode
# Lurker Mode

# Odsum

import pinylib
import time
from time import sleep
import random
from random import randint
from apis import tinychat


class Registration:

    def __init__(self, tinybot, spamcheck, conf):
        """
        Initialize the Spam class.

        :param tinybot: An instance of TinychatBot.
        :type tinybot: TinychatBot
        :param spamcheck: check if room is in lockdown
        :type spamcheck: True/False
        :param conf: The config file.
        :type conf: config
        """
        self.tinybot = tinybot
        self.spamcheck = spamcheck
        self.config = conf
        self.lockdown = False
        self.greet = None



    def on_publish(self, uid):
        _user = self.users.search(uid)

        if pinylib.CONFIG.B_ALLOW_BROADCASTS:
            if _user is not None:
                if _user.user_level == 8 or _user.nick in self.cambans:
                    self.score = 10
                    self.send_close_user_msg(_user.id)
                    self.handle_msg('%s is banned from camming up.' % _user.nick)
                    _user.is_broadcasting = False
                    self.send_kick_msg(_user.id)
            _user.is_broadcasting = True

        else:
            self.send_close_user_msg(_user.id)
            self.handle_msg('Broadcating is disabled, allowcam to enable.')
            _user.is_broadcasting = False


    def user_register(self, _user):

        if not _user.account:
            _user.user_level = 7  # guest
            self.tinybot.console_write(pinylib.COLOR['cyan'],
                                       '[User] Guest %s:%d' % (_user.nick, _user.id))

            if not self.config.B_ALLOW_GUESTS:
                if _user.user_level == 7:
                    if self.spamcheck.lockdown:
                        self.tinybot.process_ban(_user.id)
                    else:
                        self.tinybot.send_ban_msg(_user.id)
                    if self.config.B_VERBOSE:
                        self.tinybot.handle_msg('%s was banned (No Guests allowed).' % _user.nick)
                        self.tinybot.console_write(pinylib.COLOR['red'],
                                                   '[Security] %s was banned on no guest mode' % _user.nick)
                    return False

            if _user.is_lurker and not self.config.B_ALLOW_LURKERS:
                if _user.user_level > 5:
                    if self.spamcheck.lockdown:
                        self.tinybot.process_ban(_user.id)
                    else:
                        self.tinybot.send_ban_msg(_user.id)
                    if self.config.B_VERBOSE:
                        self.tinybot.handle_msg('%s is a lurker, no captcha. No Lurker Mode' % _user.nick)
                    self.tinybot.console_write(pinylib.COLOR['red'],
                                               '[Security] %s was banned on no lurkers mode' % _user.nick)
                    return False

        else:

            buddyusr = self.tinybot.buddy_db.find_db_user(_user.account)
            tc_info = tinychat.user_info(_user.account)

            if tc_info is not None:
                _user.tinychat_id = tc_info['tinychat_id']
                _user.last_login = tc_info['last_active']
                self.greet = tc_info['biography']

            if _user.is_owner:
                _user.user_level = 2  # account owner
                self.tinybot.console_write(pinylib.COLOR['cyan'], '[User] Room Owner %s:%d:%s' %
                                           (_user.nick, _user.id, _user.account))
            elif _user.is_mod:
                _user.user_level = 3  # mod
                self.tinybot.console_write(pinylib.COLOR['cyan'], '[User] Moderator %s:%d:%s' %
                                           (_user.nick, _user.id, _user.account))

            if buddyusr:
                _level = buddyusr['level']

                if not _user.is_mod:
                    _user.user_level = _level

                if _level < 6:
                    if buddyusr['greet'] != '':
                        self.greet = buddyusr['greet']

                if _level == 4 and not _user.is_mod:
                    _user.user_level = _level  # chatmod

                if _level == 5 and not _user.is_mod:
                    _user.user_level = _level  # whitelist

                if _level == 2:  # overwrite mod to chatadmin
                    _user.user_level = _level

                self.tinybot.console_write(pinylib.COLOR['cyan'], '[User] Found, level(%s)  %s:%d:%s' % (
                    _user.user_level, _user.nick, _user.id, _user.account))

            if self.tinybot.buddy_db.find_db_account_bans(_user.account) and self.tinybot.is_client_mod:
                if self.spamcheck.lockdown:
                    self.tinybot.process_ban(_user.id)
                else:
                    self.tinybot.process_ban(_user.id)
                if self.config.B_VERBOSE:
                    self.tinybot.handle_msg('%s is an banned account.' % _user.account)
                    self.tinybot.console_write(pinylib.COLOR['red'],
                                               '[Security] Banned: Account %s' % _user.account)
                return False

            if _user.user_level is None:
                _user.user_level = 6  # account not whitelisted
                self.tinybot.console_write(pinylib.COLOR['cyan'],
                                           '[User] Not Whitelisted %s:%d:%s' % (_user.nick, _user.id, _user.account))

            if self.config.B_VIP and not buddyusr:
                if self.spamcheck.lockdown:
                    #self.tinybot.process_ban(_user.id)
                    sleep(randint(3,6))
                else:
                    sleep(randint(3,6))
                    #self.tinybot.send_ban_msg(_user.id)
                    if _user.is_broadcasting:
                        self.send_close_user_msg(_user.id)
                        _user.is_broadcasting = False

                if self.config.B_VERBOSE:
                    self.tinybot.handle_msg(
                        '%s is banned account, only known accounts allowed in VIP Mode.' % _user.account)
                self.tinybot.console_write(pinylib.COLOR['red'],
                                           '[Security] %s was banned, VIP mode' % _user.nick)
                return False
        return True

        if cmd == prefix + 'acc':  # !acc add <account> level note/msg  or !acc del <account>
            self.accountmanager(cmd_arg)

        if cmd == prefix + 'camban':  # dirty 2 minutes hack code /// requested guest camban
            _user = self.users.search_by_nick(cmd_arg)
            if _user is None:
                if cmd_arg in self.cambans:
                    self.cambans.remove(cmd_arg)
                    _user.user_level = 7
                    self.handle_msg('%s is allowed to broadcast again.' % cmd_arg)
                    return
                else:
                    _user.user_level = 8
                    self.cambans.append(cmd_arg)
                    if _user.is_broadcasting:
                        self.send_close_user_msg(_user.id)
                        _user.is_broadcasting = False
            else:
                self.handle_msg('no such user')
            self.handle_msg('%s is now banned from camming' % cmd_arg)

        self.console_write(pinylib.COLOR['green'], self.active_user.nick + ': ' + cmd + ' ' + cmd_arg)
