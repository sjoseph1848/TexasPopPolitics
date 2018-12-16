import textract
text = textract.process('popmakeup.jpg', encoding='ascii', 
                        method='tesseract')