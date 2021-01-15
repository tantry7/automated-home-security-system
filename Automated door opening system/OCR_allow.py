import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image



reader = easyocr.Reader(['en'])

output = reader.readtext('image.png')

Name = output[-1][1]
print(Name)
if Name =="Unknown":
    import window_check
    exit()
else:
    import window_allowed
    exit()
