import imagehash
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np

#this file is designed to invesitgate distance matrix between images
#multi-threading is used since the computation is expensive

def main():
    path = ''
    imgdir = ''
    n_samples = len(imgdir)
    def compute_row(i):
        row = np.zeros(n_samples)
        for j in range(n_samples):
            hash1 = imagehash.average_hash(Image.open(os.path.join(path, imgdir[i])))
            hash2 = imagehash.average_hash(Image.open(os.path.join(path, imgdir[j])))
            row[j] = hash1 - hash2
        return row

    distance_hash_matrix = np.zeros((n_samples, n_samples))
    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_row = {executor.submit(compute_row, i): i for i in range(n_samples)}
        for future in as_completed(future_to_row):
            i = future_to_row[future]
            distance_hash_matrix[i] = future.result()

    print(distance_hash_matrix)
    print(distance_hash_matrix.shape)
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the first subplot
    axs[0].imshow(distance_hash_matrix, cmap='hot')
    axs[0].set_title('Distance Hash Matrix')
    axs[0].set_xlabel('X Label')
    axs[0].set_ylabel('Y Label')
    axs[0].set_xticks([])
    axs[0].set_yticks([])
    fig.colorbar(axs[0].imshow(distance_hash_matrix, cmap='hot'), ax=axs[0])

    # Extract the upper triangular matrix
    upper_triangular = np.triu(distance_hash_matrix)

    # Flatten the matrix into a 1D array
    distance_hash_values = upper_triangular[upper_triangular != 0].flatten()

    # Plot the second subplot
    axs[1].hist(distance_hash_values, bins=100)
    axs[1].set_title('Histogram of Distance Values')
    axs[1].set_xlabel('Distance Values')
    axs[1].set_ylabel('Frequency')

    # Adjust the spacing between subplots
    fig.tight_layout()


if __name__ == "__main__":
    main()