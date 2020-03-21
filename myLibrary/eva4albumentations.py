import numpy as np
import albumentations as A
from albumentations.pytorch import ToTensor
class Albumentations:
  def __init__(self,Normalize_mean_std=None,Rotate=None,HorizontalFlip=False,RGBshift=None,cutout=None):
    self.transforms=[]
    if Rotate is not None:
      self.transforms.append(A.Rotate(Rotate))
    if HorizontalFlip:
      self.transforms.append(A.HorizontalFlip())
    if RGBshift is not None:
      self.transforms.append(A.RGBShift(*RGBshift))
    if Normalize_mean_std is not None:
      self.transforms.append(A.Normalize(Normalize_mean_std[0],Normalize_mean_std[1]))
    if cutout is not None:
      self.transforms.append(A.Cutout(*cutout))
    self.transforms.append(ToTensor())
    self.Transforms=A.Compose(self.transforms)
  def __call__(self,img):
    img=np.array(img)
    img=self.Transforms(image=img)['image']
    return img
    