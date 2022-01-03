from PIL import Image
from PIL import ImageDraw

white = (255)
black = (0)

# contains relevant EL image information
class ELImg:

    def __init__(self, image, id, relevantPixelDelimiter=100, extremaDelimiter=300):
        self.id = id
        self.relevantPixelDelimiter = relevantPixelDelimiter
        self.pixelList = list(image.getdata())

        # number of pixels with summed values greater than the relevantPixelDelimiter
        self.relevantPixelCount = 0

        # total pixels in image
        self.totalPixelCount = 0

        # number of pixels with summed values greater than the extremaDelimiter
        self.extremaPixelCount = 0      

        # % of image that is relevant
        self.relevantTotalRatio = 0.0   

        # % of relevant pixels that are extrema pixels
        self.extremaRelevantRatio = 0.0 

        # % of image with intense luminosity as defined by the extrema delimiter
        self.extremaTotalRatio = 0.0    

        # highest summed up pixel value in whole image
        self.pixelMax = 0               

        # key is the summed up pixel value, value is the the number of that pixel value's occurrences in image
        self.extremaMode = dict()       

        # summed up weighting of all pixel values above the relevantPixelDelimiter threshold
        self.intensityRating = 0.0      

        # the 'true' luminosity of the cell, the area of the solar cell represented in picture does not matter
        self.intensityRelevantRatio = 0.0   
        
        
        # calculate totalPixelCount to be the number of pixels in the image in total
        self.width, self.height = image.size
        self.totalPixelCount = self.width * self.height 


        # find the largest pixel value
        for colour in image.getextrema():
            self.pixelMax = self.pixelMax + colour[1]
        
        # Initialize relevantPixelCount to be the number of pixels where the R + G + B value is greater than 100
        # Find the extrema, and the number of occurences

        for pixel in self.pixelList:
            currPixel = pixel[0] + pixel[1] + pixel[2]

            # evaluate the relevant pixels
            if currPixel > relevantPixelDelimiter:   
                self.relevantPixelCount = self.relevantPixelCount + 1
                self.intensityRating = self.intensityRating + 5*currPixel/3000  - 5*relevantPixelDelimiter/3000


            # evaluate the extrema pixels
            if currPixel >= extremaDelimiter: 
                self.extremaPixelCount = self.extremaPixelCount + 1
                if currPixel in self.extremaMode.keys():
                    self.extremaMode[currPixel] = self.extremaMode[currPixel] + 1
                else:
                    self.extremaMode[currPixel] = 1
        
        self.intensityRating = round(self.intensityRating, 3)
        
        
        # calculate pixel count ratios (to 3 decimal places)
        self.relevantTotalRatio = round(self.relevantPixelCount / self.totalPixelCount * 100, 3)
        if self.relevantPixelCount == 0:
                self.extremaRelevantRatio = 0.0
        else:
            self.extremaRelevantRatio = round(self.extremaPixelCount / self.relevantPixelCount * 100, 3)
        self.extremaTotalRatio = round(self.extremaPixelCount / self.totalPixelCount * 100, 3)
        if self.relevantPixelCount == 0:
                self.intensityRelevantRatio = 0.0
        else:
            self.intensityRelevantRatio = round(self.intensityRating / self.relevantPixelCount * 100, 3)    


    # creates a projection of the relevant pixels of the image
    def ProjImage(self, fp, weighted=False):
        size = (self.width, self.height)
        projectedImage = Image.new('L', size, color=black)
        draw = ImageDraw.Draw(projectedImage, mode='L')
        if not weighted:
            currentPosition = [0,0]
            for pixel in self.pixelList:
                currPixel = pixel[0] + pixel[1] + pixel [2]
                if currPixel > self.relevantPixelDelimiter:
                    draw.point(currentPosition, fill=white)

                # increment position by 1
                if currentPosition[0] < self.width - 1:
                    currentPosition[0] = currentPosition[0] + 1
                else:
                    currentPosition[0] = 0
                    currentPosition[1] = currentPosition[1] + 1
        else:
            currentPosition = [0,0]
            for pixel in self.pixelList:
                currPixel = pixel[0] + pixel[1] + pixel [2]
                if currPixel > self.relevantPixelDelimiter:
                    draw.point(currentPosition, fill=currPixel)

                # increment position by 1
                if currentPosition[0] < self.width - 1:
                    currentPosition[0] = currentPosition[0] + 1
                else:
                    currentPosition[0] = 0
                    currentPosition[1] = currentPosition[1] + 1
        projectedImage.save(fp)



    # print out contents of ELimage
    def ELprint(self):
        print(self.id, ':', sep='')
        print("Total Pixels: \t\t", self.totalPixelCount, sep='')
        print("Relevant Pixels: \t", self.relevantPixelCount, sep='')
        print("Extrema Pixels: \t", self.extremaPixelCount, sep='')
        print("Intensity Rating: \t", self.intensityRating, sep='')
        print("Largest Pixel Value: \t", self.pixelMax, sep='')
        print("Relevant-Total Ratio: \t", self.relevantTotalRatio, '%',sep='')
        print("Extrema-Relevant Ratio: ", self.extremaRelevantRatio, '%', sep='')
        print("Extrema-Total Ratio: \t", self.extremaTotalRatio, '%', sep='')
        print("Intensity-Rel Ratio: \t", self.intensityRelevantRatio, '%', sep='')
        
