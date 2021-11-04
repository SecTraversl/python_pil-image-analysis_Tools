# %%
#######################################
def pilrotate_45(image_object: PIL.Image.Image):
    """Takes a given PIL Image object, rotates the image 45 degrees counter-clockwise, and returns the modified version of the image.

    Args:
        image_object (PIL.Image.Image): Reference an existing PIL Image object.

    Returns:
        PIL.Image.Image: Returns a PIL Image object.
    """
    new_image = image_object.rotate(45)
    return new_image

