import cv2
import matplotlib.pyplot as plt
import cvlib as cl
from cvlib.object_detection import draw_bbox
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

# Ask user to select image file
filename = askopenfilename(title='Select image file', filetypes=[('Image files', '*.jpg;*.jpeg;*.png;*.bmp')])

if filename:
    # Read the image
    image = cv2.imread(filename)

    # Detect object
    box, label, conf = cl.detect_common_objects(image)
    output_image = draw_bbox(image, box, label, conf)

    # Convert to matplotlib format
    output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)

    # Show the result
    plt.imshow(output_image)
    plt.axis('off')
    plt.show()

    # Print number of detected cars
    print('Number of cars detected in the picture: ' + str(label.count('car')))
else:
    # Give message
    print('No images selected.')