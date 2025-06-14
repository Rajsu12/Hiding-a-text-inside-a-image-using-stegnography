from PIL import Image

# ✅ Open the original image
org_img = Image.open(r"C:\Users\priya\Downloads\Image-Steganography-hiding-text-inside-image-using-python-master\Image-Steganography-hiding-text-inside-image-using-python-master\original_image.png")

# ✅ Load the pixel values
org_pixelMap = org_img.load()

# ✅ Create a new image with same mode and size
enc_img = Image.new(org_img.mode, org_img.size)
enc_pixelsMap = enc_img.load()

# ✅ Read the message from user
msg = input("Enter the message: ")
msg_index = 0

# ✅ Calculate length of the message
msg_len = len(msg)

# ✅ Traverse through each pixel
for row in range(org_img.size[0]):
    for col in range(org_img.size[1]):

        # Get RGB values from original image
        r, g, b = org_pixelMap[row, col]

        if row == 0 and col == 0:
            # Store message length in R value of first pixel
            enc_pixelsMap[row, col] = (msg_len, g, b)

        elif msg_index < msg_len:
            # Store ASCII of character in R channel
            ascii_val = ord(msg[msg_index])
            enc_pixelsMap[row, col] = (ascii_val, g, b)
            msg_index += 1

        else:
            # Copy original pixel if message is done
            enc_pixelsMap[row, col] = (r, g, b)

# ✅ Close original image
org_img.close()

# ✅ Show and Save new image
enc_img.show()
enc_img.save(r"C:\Users\priya\Downloads\Image-Steganography-hiding-text-inside-image-using-python-master\Image-Steganography-hiding-text-inside-image-using-python-master\encrypted_image.png")
enc_img.close()
