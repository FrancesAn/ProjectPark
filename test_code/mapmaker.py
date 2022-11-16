# import cv2 library
import cv2
  
# read the images
img1 = cv2.imread('libre.png')
img2 = cv2.imread('ocupado.png')
img3 = cv2.imread('especial.png')
# define a function for vertically
# concatenating images of the
# same size and horizontally
def concat_vh(list_2d):
	
	# return final image
	return cv2.vconcat([cv2.hconcat(list_h)
						for list_h in list_2d])
# image resizing
img1_s = cv2.resize(img1, dsize = (0,0),
					fx = 0.5, fy = 0.5)
img2_s = cv2.resize(img2, dsize = (0,0),
					fx = 0.5, fy = 0.5)
img3_s = cv2.resize(img3, dsize = (0,0),
					fx = 0.5, fy = 0.5)


# function calling
img_tile = concat_vh([[img1_s, img2_s, img3_s],
					[img2_s, img1_s, img2_s],
					[img2_s, img1_s, img2_s]])
# show the output image
cv2.imwrite('concat_vh.jpg', img_tile)
