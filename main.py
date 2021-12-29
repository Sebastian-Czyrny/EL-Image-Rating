
# import os, os.path # Needed for importing entire folder
from PIL import Image
import ELImage

# Insert path to image
path = "C:/Users/might/Documents/BSSR/Array Team/ELImages/Dora.jpg"
img = Image.open(path)


### Import an entire folder at once ###
### ONLY FOR BEEFY COMPUTERS ###
# imgs = []
# valid_images = [".jpg",".gif",".png",".tga"]
# for f in os.listdir(path):
#     ext = os.path.splitext(f)[1]
#     if ext.lower() not in valid_images:
#         continue
#     imgs.append(Image.open(os.path.join(path,f)))


def main():
    ### import entire folder ###
    # ELimages = []
    # for img in imgs:
    #     ELimages.append(ELImage(img, img.filename))
    # for ELimage in ELimages:
    #     ELimage.ELprint()

    ### import only one image ###
    # RECOMMENDED: Find the required relevantPixelDelimiter 
    #   by first cropping out the part of image where there is unwanted bright pixels
    #   and then setting the relevantPixelDelimiter to be the maxPixel value in the cropped image
    ELimage = ELImage.ELImg(img,img.filename, relevantPixelDelimiter=100)
    ELimage.ELprint()

    ### show the information of only a section of the image ###
    # width, height = img.size
    # box = (0, height-1100, width, height)
    # croppedImage = img.crop(box)
    # croppedImage.save('cropped_image.jpg')
    # # croppedImage.show()
    # ELcropped = ELImage.ELImg(croppedImage, 'croppedImage', relevantPixelDelimiter=100)
    # ELcropped.ELprint()



if __name__ == '__main__':
    main()


