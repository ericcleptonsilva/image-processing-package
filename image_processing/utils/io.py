from skimage.io import imsave, imread

def read_image(path, is_gray = False):
    image = imread(path,is_gray = is_gray) 
    return image

def save_image(image, path):
    imsave(path, image)