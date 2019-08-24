# Dense-Flow-GPU
## 1.usage:
use opencv 3 to extract optical flow image frame-by-frame in videos.Such as flow_x and flow_y.
Some times use these code to get optical flow frame by frame to train models.
Enjoy it.
## 2.command use:
./denseFlow_gpu --vidFile=<input_video_path> --xFlowFile=<optical_flow_save_path>/flow_x --yFlowFile=<optical_flow_save_path>/flow_y --imgFile=<extracted_frames_save_path>/ --bound=20 --type=1 --device_id=7 --step=1
## 3.update use:
- [x] update `DensePyrLKOpticalFlow algorithm` :muscle:
- [x] update `FarnebackOpticalFlow algorithm` :muscle:
- [x] update `OpticalFlowDual_TVL1 algorithm` :muscle:
- [x] update `BroxOpticalFlow algorithm` :muscle:
