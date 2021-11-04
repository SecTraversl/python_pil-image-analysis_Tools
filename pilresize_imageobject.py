# %%
#######################################
def pilresize_imageobject(image_object: PIL.Image.Image, size: "tuple[int, int]"):
    """Takes a given PIL Image object and resizes the image per the 2 integers within the tuple given to the "size" paramter.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> import PIL\n
        >>> from PIL import Image\n

        >>> pic6 = Image.open('6.jpg')\n
        >>> pic6.size\n
        (600, 800)
        
        >>> pilresize_imageobject( pic6, (200, 200) )\n
        <PIL.Image.Image image mode=RGB size=200x200 at 0x7FC233B2B490>\n

        >>> ##### EXAMPLE 2 #####
        >>> resize_pic6_width200 = pilresize_imageobject_keep_aspect_ratio(pic6, width=200)\n
        >>> resize_pic6_width200.size\n
        (200, 266)

        >>> ##### EXAMPLE 3 #####
        >>> resize_pic6_height200 = pilresize_imageobject_keep_aspect_ratio(pic6, height=200)\n
        >>> resize_pic6_height200.size\n
        (150, 200)
        
        >>> ##### EXAMPLE 4 #####
        >>> pilresize_imageobject_keep_aspect_ratio(pic6, 200, 200)\n

        Either reference the "width" or the "height" parameter to be used as the 'anchor' for the resizing operation.  Do not supply arguments to both.\n

    Args:
        image_object (PIL.Image.Image): Reference an existing PIL Image object.
        size (tuple[int, int]): Submit two integers to represent the (Width, Height) for the resizing operation.

    Returns:
        PIL.Image.Image: Returns a PIL Image object.
    """
    import PIL
    from PIL import Image
    if isinstance(image_object, PIL.Image.Image):
        return image_object.resize( size , Image.ANTIALIAS)

