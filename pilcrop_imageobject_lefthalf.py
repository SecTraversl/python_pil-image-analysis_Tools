# %%
#######################################
def pilcrop_imageobject_lefthalf(image_object: PIL.Image.Image):
    """Takes a given PIL Image object and crops the left half of the image, returning the cropped image.

    References:
        https://www.geeksforgeeks.org/python-pil-image-crop-method/\n
        https://blog.finxter.com/how-to-crop-an-image-using-pil/\n
        https://stackoverflow.com/questions/9983263/how-to-crop-an-image-using-pil\n

    Args:
        image_object (PIL.Image.Image): Reference an existing PIL Image object.

    Returns:
        PIL.Image.Image: Returns a PIL Image object.
    """
    orig_width, orig_height = image_object.size
    half_width = int(orig_width / 2)
    top_start = 0
    bottom_stop = orig_height
    left_start = half_width
    right_stop = orig_width
    new_image = image_object.crop( (left_start, top_start, right_stop, bottom_stop) )
    return new_image

