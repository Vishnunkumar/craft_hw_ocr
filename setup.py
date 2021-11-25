from distutils.core import setup

setup(
  name = 'craft_hw_ocr',         
  packages = ['craft_hw_ocr'],   
  version = '1.1',      
  license='MIT',        
  description = 'Deep learning for document processing',   
  author = 'Vishnu N',                  
  author_email = 'vishnunkumar25@gmail.com',      
  url = 'https://github.com/Vishnunkumar/craft_hw_ocr/',   
  download_url ='https://github.com/Vishnunkumar/craft_hw_ocr/archive/refs/tags/v-1.1.tar.gz',    
  keywords = ['NLP', 'OCR', 'Deep learning', 'Computer Vision'],   
  install_requires = [            
          'transformers',
          'craft_text_detector',
          'opencv-python',
          'Pillow',
          'numpy'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
