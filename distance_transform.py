# create distance maps from binary segmented samples of fiber

import cv2
import os



def find_png_files(directory):
    png_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png'):
                png_files.append(os.path.join(root, file))
    return png_files

def get_bin_images(source_path):
    pass

def create_distance_maps(bin_images, dest_path):
    for filename in bin_images:
        print(filename)
        image = cv2.imread(filename, 0)
        distance_map = cv2.distanceTransform(image, cv2.DIST_L2, 3)
        #print(distance_map.max())
        dest_name = os.path.basename(filename)
        cv2.imwrite(dest_path + "/" + dest_name, distance_map)

if __name__ == "__main__":
    print('batch distance transform')
    print(os.getcwd())
    print(os.path.dirname(os.path.realpath(__file__)))

    root = os.path.dirname(os.path.realpath(__file__));
    source_path = root + "/cropped/exported/g1"
    dest_path = root + "/distance_maps/g1"

    bin_images = find_png_files(source_path)

    print(f"len: {len(bin_images)}")

    create_distance_maps(bin_images, dest_path)