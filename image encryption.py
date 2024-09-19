def process_image(image, key, mode):
    processed_image = []
    
    for row in image:
        processed_row = []
        for pixel in row:
            processed_pixel = pixel ^ key
            processed_row.append(processed_pixel)
        processed_image.append(processed_row)
    
    return processed_image

image = [
    [int(x) for x in input("Enter pixel values for row 1 (comma separated): ").split(",")],
    [int(x) for x in input("Enter pixel values for row 2 (comma separated): ").split(",")],
    [int(x) for x in input("Enter pixel values for row 3 (comma separated): ").split(",")],
    [int(x) for x in input("Enter pixel values for row 4 (comma separated): ").split(",")],
    [int(x) for x in input("Enter pixel values for row 5 (comma separated): ").split(",")]
]

key = int(input("Enter the key (integer) for encryption/decryption: "))
mode = input("Type 'e' for encryption or 'd' for decryption: ").lower()

if mode == 'e':
    result = process_image(image, key, mode)
    print("Encrypted Image:")
    for row in result:
        print(row)
elif mode == 'd':
    result = process_image(image, key, mode)
    print("Decrypted Image:")
    for row in result:
        print(row)
else:
    print("Invalid mode! Please enter 'e' for encryption or 'd' for decryption.")
