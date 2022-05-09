import numpy,cv2,os 
def imagen_descomposer(file='Image-Trainer-Set/Dataset/Dataset_train'):
    img_dir = os.listdir(f'{os.getcwd()}/{file}')
    print(img_dir)
    data_set = []
    for img in img_dir:
        im_gray = cv2.imread(f'{file}/{img}', cv2.IMREAD_GRAYSCALE)
        data_set.append(im_gray)
    return numpy.array(data_set)