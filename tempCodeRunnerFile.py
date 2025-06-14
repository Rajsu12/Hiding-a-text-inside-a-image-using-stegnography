from PIL import Image

# ✅ Open the image (use raw string for Windows path)
enc_img = Image.open(r"C:\Users\priya\Downloads\Image-Steganography-hiding-text-inside-image-using-python-master\Image-Steganography-hiding-text-inside-image-using-python-master\encrypted_image.png")

# ✅ Load the pixel values
enc_pixelMap = enc_img.load()

# ✅ Initialize empty message string
msg = ""
msg_index = 0

# ✅ Traverse the image pixel-by-pixel
for row in range(enc_img.size[0]):
    for col in range(enc_img.size[1]):

        pixel = enc_pixelMap[row, col]
        r = pixel[0]  # R channel

        if col == 0 and row == 0:
            msg_len = r  # 1st pixel's R value is length of message

        elif msg_index < msg_len:
            msg += chr(r)  # Convert R value to character
            msg_index += 1

# ✅ Close image
enc_img.close()

# ✅ Print the hidden message
print("\nThe hidden message is:\n")
print(msg)
