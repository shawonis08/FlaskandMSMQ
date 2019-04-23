import os
import win32com.client


# msginfo = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
print(qinfo)
computer_name = os.getenv('COMPUTERNAME')
print(computer_name)
qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\flaskmsmqtest"
queue=qinfo.Open(2,0)   # Open a ref to queue
print(type(qinfo))
print(queue)
msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
print(msg)
msg.Label="a"+ str(queue)
msg.Body = "dfdfd"
msg.Send(queue)

queue.Close()