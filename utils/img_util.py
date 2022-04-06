import cv2
import torch


def img2tensor(imgs, bgr2rgb=True, float32=True):
    """Numpy array to tensor

    Args:
        imgs (list[ndarray] | ndarray): Input images.
        bgr2rgb (bool): Whether convert bgr to rgb. Defaults to True.
        float32 (bool): Whether change to float32. Defaults to True.

    Returns:
        list[tensor] | tensor: Tensor images.If returned results only have
            one element, just return tensor.
    """

    def _totensor(img, bgr2rgb, float32):
        if img.shape[2] == 3 and bgr2rgb:
            if img.dtype == "float64":
                img = img.astype("float32")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = torch.from_numpy(img.transpose(2, 0, 1))
        if float32:
            img = img.float().div(255.)
        return img

    if isinstance(imgs, list):
        return [_totensor(img, bgr2rgb, float32) for img in imgs]
    else:
        return _totensor(imgs, bgr2rgb, float32)
