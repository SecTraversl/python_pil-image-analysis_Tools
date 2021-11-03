# %%
#######################################
def pilshow_imageobject_vscode(image_object: PIL.Image.Image):
    """When used with a VS Code "Interactive Window", displays the referenced image object.

    Args:
        image_object (PIL.Image.Image): Reference an existing Image object
    """
    import PIL
    from PIL import Image
#   
    if isinstance(image_object, PIL.Image.Image):
        return image_object

