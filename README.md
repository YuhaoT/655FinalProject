## Installation 
**install miniconda for both ml and flask servers**
* download miniconda installer and make it executable
```
sudo wget -c https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sudo chmod +x Miniconda3-latest-Linux-x86_64.sh
```
* install miniconda, and source your `.bashrc` file
```
./Miniconda3-latest-Linux-x86_64.sh 
source /users/<XXX>/.bashrc
```
* create a new environment with flask, torch, and pillow :  

```
conda create -n dlflask python=3.7 torch flask pillow
conda activate dlflask
```
**deploying pytorch and all nesseary library to ml server machine for machine learning.**
```
pip install libjpeg-dev zlib1g-dev Pillow torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu --no-cache-dir
```
**deploying flask to webserver machine for website.**
```
pip install flask
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

