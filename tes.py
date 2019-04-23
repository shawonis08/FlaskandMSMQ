import os
import win32com.client
import time


# msginfo = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
#
# computer_name = os.getenv('COMPUTERNAME')
#
# msginfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\flaskmsmqtest"
# msgqueue = msginfo.Open(2, 0)   # Open a ref to queue
#
# msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
#
# msg.Label=time.strftime("%d%m%y%H%M%S")
# msg.Body = "dfdfd"
# msg.Send(msgqueue)
#
# msgqueue.Close()

timestr = time.strftime("%d%m%y%H%M%S")
print (timestr)