# %%
#######################################
def pilexif_imageobject_gps_googlemaps_url(image_object: PIL.Image.Image):
    """Takes a given PIL Image object and returns the Google Maps URL with the appropriate Latitude and Longitude derived from the exif GPS coordinates metadata of the image (if that metadata is available for the image).

    Examples:
        >>> import PIL\n
        >>> from PIL import Image\n
        >>> ##### EXAMPLE 1 #####
        >>> # In this example, there is no GPS exif metadata
        >>> pic1 = Image.open('1.jpg')\n
        >>> pilobj_exif_gps_coordinates(pic1)\n
        (0, 0)
        >>> pilexif_imageobject_gps_googlemaps_url(pic1)\n
        The image does not appear to have any exif GPS metadata\n
        >>> ##### EXAMPLE 2 #####
        >>> # In this example, there is GPS exif metadata
        >>> pic29 = Image.open('29.jpg')\n
        >>> pilobj_exif_gps_coordinates(pic29)\n
        (1.2631666666666668, 103.822)
        >>> pilexif_imageobject_gps_googlemaps_url(pic29)\n
        'https://maps.google.com/maps?q=001.26317,103.82200&z=15'

    References:
        The original was written by Mark Baggett and has been modified by me\n
        https://www.sans.org/cyber-security-courses/automating-information-security-with-python/\n

    Args:
        image_object (PIL.Image.Image): Reference an existing PIL Image object.

    Returns:
        str: If the image has exif GPS metadata, returns the URL for Google Maps.  Otherwise, returns None
    """
    exifdata = image_object.getexif()
    if not exifdata or not exifdata.get_ifd(0x8825):
        print('The image does not appear to have any exif GPS metadata')
        return None
    latDegrees = float(exifdata.get_ifd(0x8825)[2][0])
    latMinutes = float(exifdata.get_ifd(0x8825)[2][1])/60
    latSeconds = float(exifdata.get_ifd(0x8825)[2][2])/3600
    lonDegrees = float(exifdata.get_ifd(0x8825)[4][0])
    lonMinutes = float(exifdata.get_ifd(0x8825)[4][1])/60
    lonSeconds = float(exifdata.get_ifd(0x8825)[4][2])/3600
    # correct the lat/lon based on N/E/W/S
    latitude = latDegrees + latMinutes + latSeconds
    if exifdata.get_ifd(0x8825)[1] == 'S':
        latitude *= -1
    longitude = lonDegrees + lonMinutes + lonSeconds
    if exifdata.get_ifd(0x8825)[3] == 'W':
        longitude *= -1
    maps_url = 'https://maps.google.com/maps?q={0:09.5f},{1:09.5f}&z=15'.format(latitude, longitude)
    return maps_url

