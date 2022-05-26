import os
import hou
import sys

def main():
    hipPath =  sys.argv[1]
    print "Load Hip @ :" + hipPath
    hou.hipFile.load(hipPath)
    hou.node("/out/OutRender").parm('execute').pressButton()
    
if __name__ == '__main__':
    main()