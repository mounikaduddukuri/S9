## S9s
1. In this assignment we are implementing gradCAM.
2. And Image augmentations using albumentations.
To use albumentations wrote it in [this file](https://github.com/Lakshman511/EVA4/blob/master/s9/myLibrary/eva4albumentations.py)
Also we implemented gradCAM code in [this file](https://github.com/Lakshman511/EVA4/blob/master/s9/myLibrary/eva4gradcam.py)
For remaining parts including data loading,model training etc., are done with previous file
### [Code1](https://github.com/Lakshman511/EVA4/blob/master/s9/eva4_s9_albumentations_grad_cam.ipynb)
1.In this we use data augmentations: rotate,HorizontalFlip,Normalize.
2.However this modelmachieved 91.5% accuracy.There is significant difference between train and test accuracies(overfitting)
3.gradCAMs of this model are
![](https://github.com/Lakshman511/EVA4/blob/master/s9/heatmaps_1.png)



We may reduce gap between by adding augmentation techniques like cutout

### [Code2](https://github.com/Lakshman511/EVA4/blob/master/s9/eva4_s9_albumentations_grad_cam_with_cutout.ipynb)
1. In this model we added cutout and RGBShift.
2.We achieved 91.73 and overfitting is reduced when compared to previous one.
3.GradCAM of visualisations this model are
![](https://github.com/Lakshman511/EVA4/blob/master/s9/heatmaps_2.png)
