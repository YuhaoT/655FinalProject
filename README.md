## Installation 

* deploying pytorch and all nesseary library to ml server machine for machine learning.
```
pip3 install libjpeg-dev zlib1g-dev Pillow torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu --no-cache-dir
```
* deplying flask to webserver machine for website.
```
pip3 install flask
```

## Predict a image

* First start server.py with the following command on the ml server machine, it will run in loop.
```
python3 server.py
```
* Then, start file_upload.py using on the webserver machine
```
python3 file_upload.py
```
At this moment a website can be accessed via 143.215.216.196:80.
Interact with the website and upload image, soon after you will get a result displayed on the website.

