import os
import imagehash
from PIL import Image
import numpy as np

#stat_frame is function to investigate difference  between two images within window

def main():
    path = ''
    matrix_profile = stat_frame(path, queue_size=3)
    print(matrix_profile)
    print((matrix_profile.ravel()).mean(0))
    print(np.var((matrix_profile.ravel())))
    max_val = int(np.max(matrix_profile))
    print(max_val)
    plt.hist(matrix_profile.ravel(), bins=max_val, range=[0, max_val])
    plt.title("Frequency Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

def sort_key(filename):
    parts = filename.split("_")
    suffix = parts[-1]
    num = int(suffix.split(".")[0])
    return num

def hash_diff(img1, img2):
    hash1 = imagehash.average_hash(Image.open(img1))
    hash2 = imagehash.average_hash(Image.open(img2))
    return hash1 - hash2
    
def stat_frame(path, queue_size):

    files = os.listdir(path)
    sorted_imgdir = sorted(files, key=sort_key)

    check_point = queue_size
    end_state = False
 
    matrix_profile = np.zeros((len(files) - queue_size-1, queue_size-1))
    for i in range(matrix_profile.shape[0]):
        queue = sorted_imgdir[i:check_point+i]
        row = np.zeros(queue_size-1)
        for j in range(1, len(queue)):
            img_ref = os.path.join(path, queue[0])
            img = os.path.join(path, queue[j])
            diff = hash_diff(img_ref, img)
            # print('difference btween {} and {} is'.format(queue[0][37:], queue[j][37:]), diff)
            row[j-1] = diff 
        # print(row)
        matrix_profile[i] = row
        # queue = sorted_imgdir[i:check_point+i]
    return matrix_profile

if __name__ == '__main__':
    main()