from pathlib import Path
from PIL import Image
import os

ASCII_BITS = '0', '1'
#imagepath = Path('frame27.png')

folder_dir = "frames_animate_test"
anim_w=0
anim_h=0
display_list = "{"

filenames = sorted(os.listdir(folder_dir))

current_img_index=0

for images in os.listdir(folder_dir):

    
    try:    
        img = Image.open("frames_animate_test/"+"frame"+str(current_img_index)+".png").convert('1')  # Convert image to bitmap.
    except:
        print("File over!")
        break
    width, height = img.size
    anim_w = width
    anim_h = height
    # Convert image data to a list of ASCII bits.
    data = [ASCII_BITS[bool(val)] for val in img.getdata()]
    # Convert that to 2D list (list of character lists)
    data = [data[offset: offset+width] for offset in range(0, width*height, width)]

    imagepath = Path("frames_animate_test/"+images)

    for row in data:        
        raw_data=''.join(row) + '\n'
        processed_list = [raw_data[i:i+8] for i in range(0, len(raw_data), 8)]
        binary_formatting = ['0b'+ str(processed_list[i]) for i in range(0, len(processed_list))]
        binary_formatting = binary_formatting[:-1]

        output = "{"
        for i in binary_formatting:
            output+=(str(i)+",")
        output = output[:-1]
        output += "}"

    print("frame"+str(current_img_index)+".png" + " processed")
    display_list += output + ","

    current_img_index+=1
    
display_list = display_list[:-1]
display_list += "}"

file = open("output.txt",'w')
file.write(display_list)
file.close()

print("Finished! \n\nWidth:" + str(anim_w) +" Height:"+ str(anim_h))
