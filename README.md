# craft_hw_ocr
Recognition of handwritten text using CRAFT text detection and TrOCR

## CRAFT

[CRAFT(Character Region Awareness for Text Detection)](https://arxiv.org/abs/1904.01941) is a way of doing OCR on images by exploring the region around the text. On high level the algorithm generates heatmap of the image and convolute upon them rather than on the image directly. Also for generating bounding boxes it will model respective thresholds with anchor points between individual character and individual words

## TrOCR

TrOCR is essentially an 
