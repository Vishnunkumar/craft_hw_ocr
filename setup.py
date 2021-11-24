from distutils.core import setup

setup(
  name = 'craft_hw_ocr',         
  packages = ['craft_hw_ocr'],   
  version = '0.1',      
  license='MIT',        
  description = 'Deep learning for document processing',   
  author = 'Vishnu N',                  
  author_email = 'vishnunkumar25@gmail.com',      
  url = 'https://github.com/Vishnunkumar/craft_hw_ocr/',   
  download_url ='https://github.com/Vishnunkumar/craft_hw_ocr/archive/refs/tags/v-1.tar.gz',    # I explain this later on
  keywords = ['NLP', 'OCR', 'Deep learning', 'Computer Vision'],   # Keywords that define your package best
  install_requires = [            # I get to this in a second,
          'transformers',
          'craft_text_detector',
          'opencv-python',
          'Pillow',
          'numpy'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)