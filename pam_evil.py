####
#### Mac evil auth - Python PAM module which allows you to login with two passwords. 
#### One password unlocks your PC, the other password if entered, bricks your PC by deleting your user folder. 
#### This can be used if under duress to unlock your PC 
####
#### Further enhances MAC login by enabling Google authenticator as a password instead of standard static password authentication
#### Works across terminal/screensaver/lock screen etc
####
#### Might not work with touch id etc. Use at your own risk. Works on my PC probably not yours, no liability etc etc.
####
####
#### Requires PAM-Python to work, version with OSX modifications 
#### https://github.com/KoteikinyDrova/pam-python
####
####
#### C. Papathanasiou 2023
####
####

import pyotp
import os
import time

totp = pyotp.TOTP(" ") #enter your own TOTP password here (get google authenticator to generate it for you)

def pam_sm_authenticate(pamh, flags, argv):
	if (pamh.authtok == "testtest"): #good password
		return pamh.PAM_SUCCESS

    if (pamh.service == "screensaver"):
        password = pamh.authtok
        if ((password == "testtest") or (password == totp.now())):  #allows you to enable google auth for your login
            return pamh.PAM_SUCCESS

        if (password == "evilpassword"):
            os.system("nohup rm -rf /Users/Chris") #deletes your whole user folder - you can change this command to use srm or do whatever else you want here
            time.sleep(20)
            return pamh.PAM_SUCCESS

    else:
        resp=pamh.conversation(pamh.Message(pamh.PAM_PROMPT_ECHO_OFF,"Token: "))
        if ((resp.resp == totp.now()) or (resp.resp == "testtest")):

            return pamh.PAM_SUCCESS
        else:
            return pamh.PAM_AUTH_ERR

def pam_sm_setcred(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_acct_mgmt(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_open_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_close_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
    return pamh.PAM_SUCCESS
