from PIL import Image


### Config ###
#im_width = 768
#im_height = 432
im_width = 500
im_height = 125
#character_list = ['.', ',', '-', '=', '#', '%', '&', '@']
#character_list = [' ', '.', '"', ':', 'I', '!', '>', '~', '_', '?', '[', ')', '|', '/', 'f', 'r', 'n', 'z', 'Y', 'L', '0', 'Z', 'w', 'p', 'b', 'h', 'o', '#', 'W', '8', 'B', '$']
character_list = [' ', '-', '.', "'", ':', '"', '>', '!', ';', '/', 'c', 'r', '?', '=', ')', 'l', 'n', 'T', 'o', 'f', 'X', 'H', 'm', 'O', '#', 'W', 'N', '8', '&', '$', 'Q', '@']

#picture_dir = r"C:\# Work\Python Practice\ascii_art\Shopee-Building-Exterior-6-1024x576.jpg"
file_name = "poe.jpeg"
parent_dir = r"C:\# Work\Python Practice\ascii_art\\"
output_dir = r"C:\# Work\Python Practice\ascii_art\canvas.txt"

picture_dir = parent_dir + file_name



# Data structure: matrix (list of lists)
def build_empty_matrix(image_width, image_height):
    final = []
    for i in range(image_height):
        row_list = [None]*image_width
        final.append(row_list)
    return final

# extract greyscale pixel values from image and populate the string matrix
def generate_string_matrix(image, image_width, image_height):
    string_matrix = build_empty_matrix(image_width, image_height)
    for width_value in range(image_width):
        for height_value in range(image_height):
            pixel_value = image.getpixel((width_value, height_value))
            string_matrix[height_value][width_value] = pixel_value
    return string_matrix

# for printing the art on cmd
def print_ascii_art(ascii_matrix):
    for row in ascii_matrix:
        row_string = ''.join(row)
        print(row_string)

# for writing the image to a file for easier scrolling
def write_ascii_art(ascii_matrix, output_dir):
    f = open(output_dir, 'w')
    for row in ascii_matrix:
        row_string = ''.join(row) + '\n'
        f.write(row_string)
    f.close()


if __name__ == '__main__':
    ### Load in raw image
    im = Image.open(picture_dir)
    # Shrink image
    im = im.resize((im_width, im_height))
    # Convert to B and W
    im = im.convert(mode = 'L')
    # Converted image into pixel values
    pixel_matrix = generate_string_matrix(im, im_width, im_height)  
    # Need to convert pixel values into characters from character_list above
    #ascii_character_matrix = list(map(lambda x: list(map(lambda y: character_list[y//32], x)), pixel_matrix))
    ascii_character_matrix = list(map(lambda x: list(map(lambda y: character_list[y//(int(256/len(character_list)))], x)), pixel_matrix))
    write_ascii_art(ascii_character_matrix, output_dir)
