import os
import imagehash
from PIL import Image

#path variable takes a dirctory that contains image frames that are extracted from a video with certain sampling rate
#remove_frame has three arguements, path, threshold, and queue_size
#The frames to be deleted will be determined by threshold value
#The queue_size is the size of window that will be slided through iteration

def main():
    path = ''
    remove_frame(path, threshold=2, queue_size=3)

def sort_key(filename):
    parts = filename.split("_")
    suffix = parts[-1]
    num = int(suffix.split(".")[0])
    return num

def hash_diff(img1, img2):
    hash1 = imagehash.average_hash(Image.open(img1))
    hash2 = imagehash.average_hash(Image.open(img2))
    return hash1 - hash2

def remove_frame(path, threshold, queue_size):

    files = os.listdir(path)
    sorted_imgdir = sorted(files, key=sort_key)

    check_point = queue_size
    end_state = False
 
    queue = sorted_imgdir[:check_point]
    while len(queue) >= 2 or end_state:
        print('---while loop iteration---')
        remove_list = []
        count = 0
        for i in range(1, len(queue)):
            img_ref = os.path.join(path, queue[0])
            print('for loop iteration',i)
            img = os.path.join(path, queue[i])
            diff = hash_diff(img_ref, img)
            print('difference btween {} and {} is'.format(queue[0][37:], queue[i][37:]), diff)
            if diff <= threshold:
                print(queue[i], 'will be removed')
                remove_list.append(queue[i])
                count +=1
        print('remove list:',remove_list)
        for tbr in remove_list:
            os.remove(os.path.join(path, tbr)) #By commenting this out this code will remove your files 
            queue.remove(tbr)
        queue.pop(0)
        print("after removing the 1st eleement and elements in the remove list, the queue length is ", len(queue))

        if end_state:
            pass
        
        else:            
            queue.extend(sorted_imgdir[check_point:check_point + count+1])
            if len(queue) <= 2:
                print("you reach the last two elements and queue won't be loaded")
                end_state = False
            else:
                print('queue is loaded with the next elements and its size is ', len(queue))
                print(queue)
                check_point+=count+1
                print('check point: ', check_point)

if __name__ == '__main__':
    main()