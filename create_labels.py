from ultralytics.data.converter import convert_voc_to_yolo_obb, segment_label

#convert_voc_to_yolo_obb(r'C:\Users\AnneKjerstineDesler\OneDrive - CPHI Shared Services A S\Dokumenter\Object detection\ultralytics\VOC')

im_dir = r'C:\Users\AnneKjerstineDesler\OneDrive - CPHI Shared Services A S\Dokumenter\Object detection\ultralytics\VOC\images\all'
segment_label(im_dir)