from ast import arg
import matplotlib.pyplot as plt 

def plot_image(image):
    plt.figure(figsize=(12,4))
    plt.imshow(image, cmap='gray')
    plt.axis("off")
    plt.show()
    
def plot_result(*args):
    number_images = len(arg)
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12,4))
    names_lst = [f'Image{i}' for i in range(1, number_images)]
    names_lst.append("Result")
    for ax, name, image in zip(axis, names_lst, arg):
        ax.set_title(name)
        ax.imshow(image, cmap="gray")
        ax.axis("off")
    fig.tight_layout()
    plt.show()

def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12,4), sharex=True, sharey=True)
    color_lst = ["red", "green", "blue", "yellow"]
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title(f"{color.title()}  hisogram")
        ax.hist(image[:,:, index].ravel(), bins= 256, color=color, alpha=0)
    fig.tight_layout()
    plt.show()