import os

root_dir = '/home/cyl/Pictures/selfie/'
readme_path = os.path.join(root_dir, 'README.md')

image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}

folder_images = {}
for subdir, _, files in os.walk(root_dir):
    folder_name = os.path.relpath(subdir, root_dir)
    if folder_name == '.':
        continue

    for file in files:
        if any(file.lower().endswith(ext) for ext in image_extensions):
            image_path = os.path.relpath(os.path.join(subdir, file), root_dir)
            folder_images.setdefault(folder_name, []).append(image_path)

with open(readme_path, 'w') as f:
    f.write('# Image Gallery\n\n')
    for folder, images in folder_images.items():
        f.write(f'## {folder}\n\n')
        for image in images:
            f.write(f'![{os.path.basename(image)}]({image})\n\n')

print(f'Updated {readme_path} with images from {len(folder_images)} folders.')