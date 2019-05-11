#  Final Project CS 6963 Ron Chan
#
#   ImageAI for fragmented JPEG files
#    Synopsis: Use Pillow to crop the image and then use ImageAI to 
#                  perform image recognition
#    Version: I use Python 3.7.3

from imageai.Prediction import ImagePrediction
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog

def one():
    print('One')
    prediction.setModelTypeAsSqueezeNet()
    prediction.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
    fp = open("SqueezeData.txt","w+")
    return fp
def two():
    prediction.setModelTypeAsInceptionV3()
    prediction.setModelPath(os.path.join(execution_path, "inception_v3_weights_tf_dim_ordering_tf_kernels.h5"))
    fp = open("InceptionData.txt","w+")
    return fp
def three():
    prediction.setModelTypeAsResNet()
    prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
    fp = open("ResData.txt","w+")
    return fp
def four():
    prediction.setModelTypeAsDenseNet()
    prediction.setModelPath(os.path.join(execution_path, "DenseNet-BC-121-32.h5"))
    fp = open("DenseData.txt","w+")
    return fp

switcher = {
        1: one,
        2: two,
        3: three,
        4: four
    }

execution_path = os.getcwd()

# The test image
print('Choose an input Jpg file')
root = tk.Tk()
root.withdraw()

infile = filedialog.askopenfilename()
print('You selected %s' % (infile))

from PIL import Image
#infile = '1.jpg'
img = Image.open(infile)
width, height = img.size
print(' %d x %d ' % (width, height))

# Eventually have a case statement to choose algorithm:
prediction = ImagePrediction()

which_algo = simpledialog.askstring("Select","Pick an algorithm\n1 = SqueezeNet\n2 = Inception\n3 = ResNet\n4 = DenseNet",parent = root)

fp = switcher[int(which_algo)]()

prediction.loadModel()


# Scan over all possible fragmentations
for percentage in range (30,101,5):
    chopsize = int (percentage/100.0 * height)
    print('Chopsize = %d ' % (chopsize))

    box = (0, 0, width-1, chopsize)
    img.crop(box).save('zchop.jpg')

    predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "zchop.jpg"), result_count=5 )
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction,  " : " , eachProbability)
        fp.write("%s  %d %7.4f \n" % (eachPrediction, percentage, eachProbability))

fp.close()
