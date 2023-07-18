# Script for crop fiber samples from OFDA screenshots
import cv2
import os

y = 74
h = 198
x = 833
w = 189

def find_png_files(directory):
    png_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png'):
                png_files.append(os.path.join(root, file))
    return png_files

# Example usage:
directory_path = '/Volumes/Externo/CARABAYA'  # Replace with the actual directory path
png_files = find_png_files(directory_path)
num_img = 1
for file in png_files:
    print(file)
    #para todas las imagenes encontradas
    img = cv2.imread(file)
    if img is not None:
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # recortar imagen
        cropped_img = img[y:y+h,x:x+w]
        print(cropped_img.shape)
        # guardar archivo
        ret = cv2.imwrite('/Users/admin/development/ofda_capture/cropped/'+str(num_img).zfill(4) + '.png', cropped_img)
        print(ret)
        num_img += 1

print("Archivos generados")