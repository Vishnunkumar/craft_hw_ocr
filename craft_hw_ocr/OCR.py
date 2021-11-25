import os
import cv2
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
from craft_text_detector import Craft


def load_image(path):
  
  """
  Loading image 
  """
  return cv2.imread(path)


def load_TrOCRmodel():
  
  """
  Loading TrOCR model which has achieved SOTA metrics on IAM handwriting dataset
  """
  processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
  model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")
  return processor, model


def craft_detection(img):
  
  """
  Text detection using CRAFT text detector
  """

  craft = Craft(output_dir=None, 
                crop_type="poly",
                export_extra=False,
                link_threshold=0.1,
                text_threshold=0.3,
                cuda=torch.cuda.is_available())

  prediction_result = craft.detect_text(img)
  return img, prediction_result


def text_recoginition(img, prediction_result, processor, model):
  
  """
  OCR using TrOCR
  """  
  text = []
  for i,j in enumerate(prediction_result['boxes']): 
    roi = img[int(prediction_result['boxes'][i][0][1]): int(prediction_result['boxes'][i][2][1]), 
              int(prediction_result['boxes'][i][0][0]): int(prediction_result['boxes'][i][2][0])]
    image = Image.fromarray(roi).convert("RGB")
    pixel_values = processor(image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    text.append(generated_text)
    print('line ' + str(i) + ' has been recoginized')
    
  return prediction_result['boxes'], ('\n').join(text)


def visualize(img, prediction_result):

  for i,j in enumerate(prediction_result['boxes']):
    
    y1 = int(prediction_result['boxes'][i][0][1])
    y2 = int(prediction_result['boxes'][i][2][1])
    
    x1 = int(prediction_result['boxes'][i][0][0])
    x2 = int(prediction_result['boxes'][i][2][0])
    
    cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)

  return Image.fromarray(img)