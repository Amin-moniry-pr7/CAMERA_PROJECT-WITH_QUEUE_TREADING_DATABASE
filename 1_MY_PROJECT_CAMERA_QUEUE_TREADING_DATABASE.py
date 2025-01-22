from MODULE_READ_PROCESS import read_video_frames, process_and_save_frames
from MODULE_SAVA_ENTERE import ENTERE
from colorama import Fore, Style
import threading

if __name__ == '__main__':

    obj_dict = {}
    thread_list = []

    try:
        n = int(input(f"{Fore.YELLOW}Enter the number of threads to use: {Style.RESET_ALL}"))
        if n <= 0:
            raise ValueError("Number of threads must be greater than 0")
    except ValueError as e:
        print(f"{Fore.RED}Invalid input: {str(e)}{Style.RESET_ALL}")
        exit(1)

    frame_queue = read_video_frames()

    for i in range(n):
        thread_list.append(threading.Thread(target=process_and_save_frames, args=(obj_dict, frame_queue)))

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    process = ENTERE()
    process.close()
