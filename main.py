import Modules.Serial as s
import Modules.logReg as lg 

baudrate = 9600
portConfig = s.SerialBegin(baudrate)
 
while(True):
    if(s.SerialAvailable(portConfig)):
        data = str(s.SerialRead(portConfig))
        lg.logRegister(data)
