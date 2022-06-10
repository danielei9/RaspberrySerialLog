import glob
import serial
import time
import logReg as lg
def serialBegin(self):
        try:
            ports = self.serial_ports()
            print("Connecting to " + str(ports[0]))
            portConfig = serial.Serial(port=ports[0],
                                       baudrate=self.baudrate,
                                       bytesize=serial.EIGHTBITS,
                                       parity=serial.PARITY_NONE,
                                       stopbits=serial.STOPBITS_ONE)
        except:
            print("ReConnecting to " + str(ports))
            time.sleep(5)
            self.serialBegin()
            return False
            # pass
        return portConfig
def SerialWrite(portConfig,xData):
    portConfig.write(str(xData).encode())

def SerialClose(portConfig):
    portConfig.close()

def SerialOpen(portConfig):
    portConfig.open()

def SerialRead(portConfig):
   return portConfig.readline()

def SerialAvailable(portConfig):
    if(portConfig.in_waiting):
        return True
    else:
        return False

def serialBeginAllPorts(self):
        ports = glob.glob('/dev/ttyUSB*')
        result = []
        for port in ports:
            try:
                s = serial.Serial(port=port,
                                       baudrate=self.baudrate,
                                       bytesize=serial.EIGHTBITS,
                                       parity=serial.PARITY_NONE,
                                       stopbits=serial.STOPBITS_ONE)
                lg.logRegister(" portbegin: " + str(s))
                print(" portbegin: " + str(s))
                result.append(s)
            except (OSError, serial.SerialException):
                lg.logWarning("OSERROR: " + str(OSError) + " \n SerialException: " + str(serial.SerialException))
                print("OSERROR: ",OSError, "SerialException: ",serial.SerialException)
                pass
        print(result)
        return result