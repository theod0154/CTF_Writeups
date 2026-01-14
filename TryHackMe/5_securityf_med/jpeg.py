print('reading file\n')

with open('jpeg.raw','rb') as file:
    data = file.read()

parts=data.split(b'image/jpeg')

print('processing file\n')

for num, part in enumerate(parts):
    jpeg_start=part.find(b'\xff\xd8')
    jpeg_end = part.find(b'\xff\xd9\x0d\x0a\x0d\x0a')
    if jpeg_start != -1 and jpeg_end !=-1:
        jpeg_image = part[jpeg_start:jpeg_end]

        with open(f'jpegs/frame{num}.jpeg','wb') as img:
            img.write(jpeg_image)

print(f'file processed.{num} images found.\n')
