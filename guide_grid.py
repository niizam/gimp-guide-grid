from gimpfu import *

# This function creates a grid of guides with specified spacing in the given image and drawable.
def guide_grid(image, drawable, hspace, vspace, percent):
    # Start an undo group for the image.
    pdb.gimp_image_undo_group_start(image)
    
    # Get the dimensions of the image.
    imageHeight = pdb.gimp_image_height(image)
    imageWidth = pdb.gimp_image_width(image)
    
    # If the percent flag is set, recalculate the pixel spacing by percentage.
    if (percent == 1):
        hspace = int(hspace * (imageHeight * 0.01))
        vspace = int(vspace * (imageWidth * 0.01))
    
    # Check if the input values for spacing are valid (greater than 0).
    if (hspace <= 0 or vspace <= 0):
        return
    
    # Calculate the number of guides to be added.
    hGuides = int(imageHeight/hspace)
    vGuides = int(imageWidth/vspace)
    
    # Add guides to the edges of the image.
    for i in range(2):
        pdb.gimp_image_add_hguide(image, i * imageHeight)
        pdb.gimp_image_add_vguide(image, i * imageWidth)
        
    # Add the horizontal guides.
    for i in range(1, hGuides):
        pdb.gimp_image_add_hguide(image, i * hspace)
        
    # Add the vertical guides.
    for i in range(1, vGuides):
        pdb.gimp_image_add_vguide(image, i * vspace)
    
    # End the undo group for the image.
    pdb.gimp_image_undo_group_end(image)

# Register the function as a plugin for GIMP.
register(
    "python_fu_guide_grid",  # Name of the plugin.
    "Guide Grid",  # Description of the plugin.
    "Creates a grid of guides with specified spacing.",  # Detailed description of the plugin.
    "Theodoros Balasis",  # Author of the plugin.
    "",  # Copyright information for the plugin.
    "2019",  # Date of creation for the plugin.
    "Guide Grid",  # Name to display in the menu.
    "*",  # Image type (all image types).
    [
        (PF_IMAGE, "image", "Input Image", None),  # (Type, name, description, default value)
        (PF_DRAWABLE, "drawable", "Input Layer", None),
        (PF_FLOAT, "hspace", "Horizontal Spacing", 1.0),
        (PF_FLOAT, "vspace", "Vertical Spacing", 1.0),
        (PF_BOOL, "percent", "By percent?", 0)
    ],  # Input parameters for the plugin.
    [],  # Output parameters for the plugin.
    guide_grid,  # Function to call when plugin is run
