# Similar Image Removal in Video Frames

This Python script removes similar images in video frames. The script works by comparing image hashes and deleting the images that fall below a specified threshold.

## Usage
```sh
python remove_similar_images.py
```

## Configuration
The script can be customized by modifying the following parameters:

- `path` (str): The path to the folder containing the images.
- `threshold` (int): The difference threshold between two images to be considered similar (default: 2).
- `queue_size` (int): The number of images to be compared in a single iteration (default: 3).

## Functionality
- `sort_key(filename)`: A helper function that sorts image filenames based on their numerical suffix.
- `hash_diff(img1, img2)`: A function that calculates the difference between two image hashes.
- `remove_frame(path, threshold, queue_size)`: The main function that performs image comparison and removal.

## How it works
1. The script starts by sorting the images in the specified folder based on their filename suffix.
2. It then iteratively compares the images in a queue of a specified size.
3. The script calculates the hash difference between the images and checks if it falls below the specified threshold.
4. If the difference is below the threshold, the image is considered similar and marked for removal.
5. Once all the images in the queue are compared, the marked images are deleted, and the queue is updated with new images for the next iteration.

## Note
To prevent the actual deletion of images during testing, comment out the following line in the 'remove_frame()' function:
