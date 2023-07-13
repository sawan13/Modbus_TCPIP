import snap7
from snap7.util import*
from snap7.types import*
import time #library time
def ReadMemory(plc,byte,bit,datatype):  
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype==S7WLBit:
        return get_bool(result,0,1)
    elif datatype==S7WLByte or datatype==S7WLWord:
        return get_int(result,0)
    elif datatype==S7WLReal:
        return get_real(result,0)
    elif datatype==S7WLDWord:
        return get_dword(result,0)
    else:
        return None

def WriteMemory(plc, byte, bit, datatype, value):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype==S7WLBit:
        set_bool(result,0,bit,value)
    elif datatype==S7WLByte or datatype==S7WLWord:
        set_int(result,0,value)
    elif datatype==S7WLReal:
        set_real(result,0,value)
    elif datatype==S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(areas['MK'],0,byte,result)

    IP = '192.168.0.2'
    RACK = 0
    SLOT = 1

    plc = snap7.client.Client()
    plc.connect(IP,RACK,SLOT)

    state = plc.getr_cpu_state()
    print(f'State:{state}')
    a = 0
    b = 0
    c = 0
    while True:
        #read tags

        readbit = ReadMemory(plc,100,0,S7WLBit) #read m0.0
        print('readbit:',readbit)
        readword = ReadMemory(plc,1,0,S7WLWord) #read mw1
        print('readbyte:',readword)
        readreal = ReadMemory(plc,2,0,S7WLReal) #read md2
        print('readreal:',readreal)
        readDword = ReadMemory(plc,3,0,S7WLDWord) #read md3
        print('readDword:',readDword)

        a=a+1
        b=b+2.4
        c=c+10

        #wirte tags
        WriteMemory(plc,0,3,S7WLBit,True)  #write m0.3 true
        time.sleep(1)  #delay 1sec
        WriteMemory(plc,0,3,S7WLBit,False)  #write m0.3 true
        time.sleep(1)  #delay 1sec
        WriteMemory(plc,5,1,S7WLWord,a)  #write mw5 from a variable
        WriteMemory(plc,6,1,S7WLReal,b)  #write mw6 from b variable
        WriteMemory(plc,7,1,S7WLDWord,c)  #write mw7 from c variable