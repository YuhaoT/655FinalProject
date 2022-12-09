import torch
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES=True
from torchvision.models import googlenet
from torchvision import transforms

def image_predict(image):
    # import model, use older implementation for compatibility
    model = torch.hub.load('pytorch/vision:v0.10.0', 'googlenet', pretrained=True)
    # model = googlenet(weights="GoogLeNet_Weights.IMAGENET1K_V1")
    model.eval()

    filename = image

    # read and preprocess images into model suable format
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
        # apply the model on the images
        output = model(input_batch)

    # calculate probabilities
    probabilities = torch.nn.functional.softmax(output[0], dim=0)

    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]

    # read the list of results and compare it to the top one
    prob, catid = torch.topk(probabilities, 1)
    res = categories[catid] + " " + str(prob.item())
    print (res)
    # return the results
    return res

if __name__ == '__main__':
    image_predict("image.jpg")
