from MODULE_SAVA_ENTERE import save_to_db
from colorama import Fore, Style, init
from ultralytics import YOLO
from queue import Queue
import sqlite3
import time
import cv2
import os

init(autoreset=True)


try:
    model = YOLO("yolov10n.pt")
except Exception as e:
    print(f"{Fore.RED}Could not load model: {str(e)}{Style.RESET_ALL}")
    exit(1)


def read_video_frames():
    cap = None
    try:
        cap = cv2.VideoCapture('VL_VIDEO.mp4')
        if not cap.isOpened():
            raise ValueError("Could not open video file: 'VL_VIDEO.mp4'")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        exit(1)

    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_queue = Queue(maxsize=0)

    frame_counter = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame_queue.put(frame)
            frame_counter += 1
            print(
                 f"{Fore.BLUE}Thread Video----> (Video Frame) =  {frame_counter}/{length} ({int(frame_counter / length * 100)}%) {Style.RESET_ALL}")
        else:
            break
    frame_queue.put(None)
    return frame_queue

def process_and_save_frames(obj_dict, frame_queue):
    process = sqlite3.connect("FRAME_PROCESSING.db")
    thread_start_time = time.time()

    while True:
        frame = frame_queue.get()
        if frame is None:
            print(f"{Fore.RED}❗️THREAD PROCESSING FINISHED❗️{Style.RESET_ALL}")
            break

        try:
            results = model(frame, verbose=False)
            res = results[0]
            my_orig_img = res.orig_img
            my_names = res.names
            my_cls = res.boxes.cls
            my_xyxy = res.boxes.xyxy

            for i in range(len(my_cls)):
                class_name = my_names[int(my_cls[i])]

                new_xyxy = [int(item) for item in my_xyxy[i]]
                x0, y0, x1, y1 = new_xyxy
                new_im = my_orig_img[y0:y1, x0:x1]

                # Create directories
                main_dir = os.path.join(os.getcwd(), '⚠️_AMIN_FRAME_⚠️')
                os.makedirs(main_dir, exist_ok=True)
                obj_dir = os.path.join(main_dir, class_name)
                os.makedirs(obj_dir, exist_ok=True)

                file_path = os.path.join(obj_dir, f"{class_name}_{obj_dict.get(class_name, 0) + 1}.jpg")
                cv2.imwrite(file_path, new_im)

                obj_dict[class_name] = obj_dict.get(class_name, 0) + 1

                # Save to dynamically created table
                save_to_db(process, class_name, file_path)

                print(
                    f"{Fore.GREEN}🖊Thread Processing🖊 ---->   ♾️Saved {class_name} {obj_dict[class_name]}.jpg♾️{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}ERROR PROCESSING FRAME: {str(e)}{Style.RESET_ALL}")

    thread_end_time = time.time()

    print(f"{Fore.CYAN}Thread execution time: {thread_end_time - thread_start_time:.4f} seconds{Style.RESET_ALL}")
    process.close()
