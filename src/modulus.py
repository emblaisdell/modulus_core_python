import sys
import os
import shutil


def calculation(inputTypes):
    def decorator(func):
        def newFunc(inputs):
            output = func(*inputs)
            if not isinstance(output, list):
                output = [output]
            return output
        newFunc.inputTypes = inputTypes
        return newFunc
    return decorator

def bytesToObject(data, dataType):    
    if dataType == "string":
        return data.decode("utf-8")
    if dataType == "integer":
        return int.from_bytes(data, byteorder='big')

def objectToBytes(obj):
    if isinstance(obj, str):
        return obj.encode("utf-8")
    if isinstance(obj, int):
        return obj.to_bytes(4, byteorder='big')


WORD_LENGTH = 4

byteorder = "little"

def decode(inputBytes):
    numArgs = int(int.from_bytes(inputBytes[0:WORD_LENGTH], byteorder=byteorder) / WORD_LENGTH)
    pointers = [int.from_bytes(inputBytes[WORD_LENGTH*i:WORD_LENGTH*(i+1)], byteorder=byteorder) for i in range(numArgs)]
    pointers.append(len(inputBytes))
    return [inputBytes[pointers[i]:pointers[i+1]] for i in range(numArgs)]

def encode(outputs):
    ln = len(outputs)
    if ln == 0:
        return b'\x00\x00\x00\x00' # TODO: test
    runningLength = WORD_LENGTH * ln
    outputBytes = b''
    for i in range(ln):
        outputBytes += runningLength.to_bytes(WORD_LENGTH, byteorder=byteorder)
        runningLength += len(outputs[i])
    for i in range(ln):
        outputBytes += outputs[i]
    return outputBytes
    