import os
import sys
import numpy as np
import subprocess

def ensureDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def generator(dataPath, optical_flow_Path, frame_Path):
    allFils = os.listdir(dataPath)
    allFils = [os.path.join(dataPath, i) for i in allFils]
    for i in allFils:
        subAllFiles = os.listdir(i)
        subAllFiles = [os.path.join(i, j) for j in subAllFiles]
        for k in subAllFiles:
            tmp = k.split('.')[0]
            print("--------------------")
            print(tmp)
            tmp = tmp.split('/')
            opticalflow_save_path = os.path.join(optical_flow_Path, tmp[-2], tmp[-1])
            frame_save_path = os.path.join(frame_Path, tmp[-2], tmp[-1])
            print(opticalflow_save_path)
            print(frame_save_path)
            ensureDir(opticalflow_save_path)
            ensureDir(frame_save_path)
            cmd = ("./denseFlow_gpu --vidFile="+k+" --xFlowFile="+opticalflow_save_path+
                "/flow_x --yFlowFile="+opticalflow_save_path+"/flow_y --imgFile="+
                frame_save_path+"/ --bound=20 --type=1 --device_id=4 --step=1")
            print("Running ......")
            print(cmd)
            subprocess.run(cmd, shell=True)
            print("---------------------")
            print()

if __name__ == "__main__":
    dataPath = sys.argv[1]
    optical_flow_Path =sys.argv[2]
    frame_Path =sys.argv[3]
    generator(dataPath, optical_flow_Path, frame_Path)