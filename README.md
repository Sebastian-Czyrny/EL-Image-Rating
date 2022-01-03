# EL-Image-Rating
By Sebastian Czyrny

Makes use of Python image library, to install:
- pip install Pillow

Image Evaluation:
- Evaluation of the image is done in the constructor of the ELImage class
- evaluator relies on use the R + G + B pixel value, where the values of the red, green, and blue pixels are summed up to take into account each colour contribution
- the main evaluator of the image is the Intensity-Relevant ratio, which takes the intensity rating and divides it by the number of relevant pixels
- relevant pixels are pixels that have an R + G + B value above the relevantPixelDelimiter, default set at 100
- intensity rating is a weighting of pixels above the relevantPixelDelimiter, with proportionate scaling 
- in this sense, it does not matter how much of the image is luminescent, only how bright it its luminescent parts are
    - i.e., an EL image with only 1 solar cell can have a higher intensity-relevant ratio than an imge containing 3 solar cells
- Weighting uses proportionate scaling with constant 5/3. Can play around with this constant, although increasing it would only serve to separate the intensity-relevant ratio of 
    dimmer images from brighter images by a greater amount

To run the script (one image at a time):
  1. Download the image that is to be scanned 
  2. Add the path to the image in main.py, near the top of the file where indicated
  3. Run main.py

Running multiple images at once:
  1. Comment out code that runs for only one image in main.py -- there are comments indicating which code this is
  2. Uncomment code to run multiple image in main.py -- there are comments indicating which code this is
  3. Add the path to the folder in main.py, near the top of the file where indicated 
  4. run main.py

You may also want to crop out a part of the image and then compare it to the whole image to find out what the relevantPixelDelimiter value 
    for the whole image should be, where the relevantPixelDelimiter value will be the max pixel value that appears in the cropped image 
    (or just crop out the image manually before scanning it)
    
Image Projection
- To see what pixels are being considered as relevant in the image, use ELImage.ELImg.ProjImage*(fp, weighted=True/False)
- fp is the filepath to save the projected image to
- set weighted to true to see the intensity of each pixelValue  
 
