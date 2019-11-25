#!/usr/bin/python
import time
import os
def scp_Retry(cmd):
    while True:
        try:
            run = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
            logger.info('Executing: '+ cmd)
            out, err = run.communicate()
        except:
            print("Something went wrong")
            time.sleep(5)
            print(out,err)
            logger.info('SCP StdOut: '+ out)
            if err == "":
                print('copied*****')
                break
            elif "Operation timed out" in err:
                print("SCP StdErr: Connection timed out")
            elif "Network is unreachable" in err:
                print("SCP StdErr: Network Error, con connectivity")
            elif "Permission denied (publickey,password,keyboard-interactive)" in err:
                print("SCP StdErr: Ssh is not ready yet ...")

    return True
scp_cmd = "scp nic@bell.ceas.wmich.edu:~/site/logicGates.png ~"
scp_Retry(scp_cmd)
