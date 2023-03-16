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

