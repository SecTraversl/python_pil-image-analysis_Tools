# %%
#######################################
def pilsave_imageobject(image_object: PIL.Image.Image, file_name: str, format=None):
    """Takes the give PIL Image object and saves/writes the image to a file by the given "file_name".  By default the extension given to "file_name" is used to determine the file format to use (e.g. .png, .jpeg, .gif, etc.).  See the 'image-file-formats' documentation mentioned in the references for more information.

    Example:
        >>> import PIL\n
        >>> from PIL import Image\n
        >>> import pathlib\n
        >>> pathlib.Path('test.jpg').read_bytes()[:20]\n
        b'\\xff\\xd8\\xff\\xe0\\x00\\x10JFIF\\x00\\x01\\x01\\x01\\x00H\\x00H\\x00\\x00'
        >>> testgif = Image.open('test.jpg')\n
        >>> pilsave_imageobject(testgif, 'test.gif')\n
        >>> pathlib.Path('test.gif').read_bytes()[:20]\n
        b'GIF87a\\x80\\x00\\x80\\x00\\x87\\x00\\x00\\xff\\xfe\\xf7\\xfd\\xfd\\xf9\\xfb'

    References:
        https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html\n
        https://stackoverflow.com/questions/14452824/how-can-i-save-an-image-with-pil\n
        https://en.wikipedia.org/wiki/List_of_file_signatures\n

    Args:
        image_object (PIL.Image.Image): Reference an existing PIL Image object
        file_name (str): Reference the name to save the image file along with the appropriate extension.
        format ([type], optional): Use this to explicitly specify the format to be used, regardless of the given extension. Defaults to None.
    """
    image_object.save(file_name, format=format)

