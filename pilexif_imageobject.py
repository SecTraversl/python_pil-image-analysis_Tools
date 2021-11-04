# %%
#######################################
def pilexif_imageobject(image_obj: PIL.Image.Image):
    """Takes a given PIL Image object and returns the exif data for the given image in the form of a dictionary, where the key is the exif field name and the value is the exif field value.

    Examples:
        >>> ##### EXAMPLE 1 #####\n
        >>> import PIL\n
        >>> from PIL import Image\n
        >>> pilget_exif_data('29.jpg')\n
        {'ExposureMode': 0, 'WhiteBalance': 0, 'GPSInfo': 556, 'SceneCaptureType': 0, 'ResolutionUnit': 2, 'ExifOffset': 254, 'Sharpness': 2, 'Make': 'Apple', 'Model': 'iPhone 4', 'Software': '4.1', 'DateTime': '2010:12:23 17:31:29', 'YCbCrPositioning': 1, 'SubjectLocation': (1295, 967, 699, 696), 'XResolution': 72.0, 'YResolution': 72.0}

        >>> ##### EXAMPLE 2 #####\n
        >>> pic29 = Image.open('29.jpg')\n
        >>> pilexif_imageobject(pic29)\n
        {'ExposureMode': 0, 'WhiteBalance': 0, 'GPSInfo': 556, 'SceneCaptureType': 0, 'ResolutionUnit': 2, 'ExifOffset': 254, 'Sharpness': 2, 'Make': 'Apple', 'Model': 'iPhone 4', 'Software': '4.1', 'DateTime': '2010:12:23 17:31:29', 'YCbCrPositioning': 1, 'SubjectLocation': (1295, 967, 699, 696), 'XResolution': 72.0, 'YResolution': 72.0}

    Args:
        image_obj (PIL.Image.Image): Reference an existing PIL Image object.
        
    Returns:
        dict: Returns a dictionary of the exif data for the Image
    """
    from PIL import Image
    from PIL.ExifTags import TAGS
#  
    results_dict = {}
    exifdata = image_obj.getexif()
    for tag_num, val in exifdata.items():
        exiffield = TAGS.get(tag_num, 'Unknown-Tag')
        results_dict[exiffield] = val
#
    return results_dict

