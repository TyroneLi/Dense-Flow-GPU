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

def generator_spec(dataPath):
    for i in dataPath:
        print("--------------------")
        k = i + ".mp4"
        opticalflow_save_path = i.replace('mpeg4_videos', 'new_optical_flow_fromMPEG4')
        frame_save_path = i.replace('mpeg4_videos', 'new_extract_frames_fromMPEG4')
        print(k)
        print(opticalflow_save_path)
        print(frame_save_path)
        # ensureDir(opticalflow_save_path)
        # ensureDir(frame_save_path)
        cmd = ("./denseFlow_gpu --vidFile="+k+" --xFlowFile="+opticalflow_save_path+
                "/flow_x --yFlowFile="+opticalflow_save_path+"/flow_y --imgFile="+
                frame_save_path+"/ --bound=20 --type=1 --device_id=7 --step=1")
        print("Running ......")
        print(cmd)
        subprocess.run(cmd, shell=True)
        print("---------------------")
        print()

def check_empty(folder):
    parent_fils = os.listdir(folder)
    parent_fils = [os.path.join(folder, i) for i in parent_fils]
    c = 0
    p = 0
    result = []
    for i in parent_fils:
        sub_files = os.listdir(i)
        sub_files = [os.path.join(i, j) for j in sub_files]
        for k in sub_files:
            p += 1
            if len(os.listdir(k)) == 0:
                # print(k)
                c += 1
                result.append(k)
    print("video nums : ", p)
    print("total : ", c)
    return result

def check_UCF(folder):
    parent_files = os.listdir(folder)
    parent_files = [os.path.join(folder, i) for i in parent_files]
    all_videos = []
    for i in parent_files:
        sub_files = os.listdir(i)
        sub_files = [os.path.join(i, j) for j in sub_files]
        for k in sub_files:
            all_videos.append(k)
    
    # for i in all_videos:
    #     print(i)
    print(len(all_videos))

    # TODO
    # UCF光流图还没提取完成，完成后检查是否有空缺

if __name__ == "__main__":
    folder = sys.argv[1]
    result = check_empty(folder)
    src_files = []
    for i in result:
        print("===============")
        print(i)
        print(type(i))
        i = i.replace('(', '"("')
        i = i.replace(')', '")"')
        i = i.replace('&', '"&"')
        i = i.replace(';', '";"')
        j = i.replace('new_optical_flow_fromMPEG4', 'mpeg4_videos')
        print(i)
        src_files.append(j)
        print(j)
        print("===============")
        print()
    print(len(result))
    print(src_files)
    generator_spec(src_files)
    print(len(src_files))
    # check_UCF(folder)