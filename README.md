# Raster_to_Vector
## An algorithm for raster to vector data conversion.
I have devised an image processing algorithm that can efficiently convert a boundary raster image to its equivalent vector image in minimum time complexity till date.
One mentionable highlight of my approach is that, it does not need to thin the boundary before data conversion, therefore the time required for pre-processing of the image (by various thinning algorithms) is not taken anymore.
Currently under research to improve in a corner case of shadow concavity, where some region (if exists) in a concavity of the boundary is shadowed by an outer boundary of the same closed curve in consideration.
