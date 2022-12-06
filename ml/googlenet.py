import torch
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES=True
from torchvision.models import googlenet
from torchvision import transforms

def image_predict(image):
    model = torch.hub.load('pytorch/vision:v0.10.0', 'googlenet', pretrained=True)
    # model = googlenet(weights="GoogLeNet_Weights.IMAGENET1K_V1")
    model.eval()

    filename = image

    input_image = Image.open(filename)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)

    with torch.no_grad():
        output = model(input_batch)

    probabilities = torch.nn.functional.softmax(output[0], dim=0)

    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]

    prob, catid = torch.topk(probabilities, 1)
    res = categories[catid] + " " + str(prob.item())
    print (res)
    return res

if __name__ == '__main__':
    image_predict("image.jpg")
