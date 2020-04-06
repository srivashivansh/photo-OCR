import cv2
import numpy as np
import requests
import io
import json

img = cv2.imread(r"C:\Users\Shivansh\Desktop\3.jpeg")
height, width, _ = img.shape
#print(img.shape)  #shape of image

#cutting image
roi = img[0: height, 50: width]

#ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".png", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
              files = {r"C:\Users\Shivansh\Desktop\screenshot.png": file_bytes},
              data = {"apikey": "549efedbfa88957", "language": "eng"})

result = result.content.decode()
result = json.loads(result)

#extracting the text
parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")

print(text_detected)
#cv2.imshow("roi", roi)    #showing the image
#cv2.imshow("Img",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
