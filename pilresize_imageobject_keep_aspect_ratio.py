# %%
#######################################
def pilresize_imageobject_keep_aspect_ratio(image_object: PIL.Image.Image, width=None, height=None):
    """Takes a given PIL Image object and will resize the image while keeping the aspect ration.  Either the "width" parameter or "height" parameter must receive an integer value for the desired 'anchor' property to be used when doing the resize (the function will automatically calculate the the other length, so only use one of the two, either "width" or "height"; do not specify both).

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> import PIL\n
        >>> from PIL import Image\n
        >>> pic6 = Image.open('6.jpg')\n
        >>> pic6.size\n
        (600, 800)

        >>> resize_pic6_width200 = pilresize_imageobject_keep_aspect_ratio(pic6, width=200)\n
        >>> resize_pic6_width200.size\n
        (200, 266)

        >>> ##### EXAMPLE 2 #####
        >>> resize_pic6_height200 = pilresize_imageobject_keep_aspect_ratio(pic6, height=200)\n
        >>> resize_pic6_height200.size\n
        (150, 200)
        
        >>> ##### EXAMPLE 3 #####
        >>> pilresize_imageobject_keep_aspect_ratio(pic6, 200, 200)\n

        Either reference the "width" or the "height" parameter to be used as the 'anchor' for the resizing operation.  Do not supply arguments to both.\n

        >>> ##### EXAMPLE 4 #####
        >>> pilresize_imageobject( pic6, (200, 200) )\n
        <PIL.Image.Image image mode=RGB size=200x200 at 0x7FC233B2B490>\n


    Args:
        image_object (PIL.Image.Image): Reference an existig PIL Image object
        width (int, optional): Reference the desired width for the resize. Defaults to None.
        height (int, optional): Reference the desired height for the resize. Defaults to None.
    """
    from PIL import Image
#    
    orig_width, orig_height = image_object.size
#
    if width and height:
        print('\nEither reference the "width" or the "height" parameter to be used as the \'anchor\' for the resizing operation.  Do not supply arguments to both.\n')
        return
    elif width:
        ratio_change = width / orig_width
        new_width = int( orig_width * ratio_change )
        new_height = int( orig_height * ratio_change )
        new_image = image_object.resize( (new_width, new_height ) , Image.ANTIALIAS)
    elif height:
        ratio_change = height / orig_height
        new_width = int( orig_width * ratio_change )
        new_height = int( orig_height * ratio_change )
        new_image = image_object.resize( (new_width, new_height ) , Image.ANTIALIAS)
    return new_image

