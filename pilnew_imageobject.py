# %%
#######################################
def pilnew_imageobject(image_file: str):
    """Returns a PIL image object from a referenced image file.

    Args:
        image_file (str): Reference an existing image file.
        
    Returns:
        PIL.Image.Image: Returns a PIL image object
    """
    from PIL import Image
#
    image_object = Image.open(image_file)
    return image_object

