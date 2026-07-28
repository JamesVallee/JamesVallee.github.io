from PIL import Image
from pathlib import Path

files = [
    ('assets/images/BRP_Cover.jpeg', 'assets/images/BRP_Cover-mobile.webp', 900),
    ('assets/images/NRC_Cover.jpg', 'assets/images/NRC_Cover-mobile.webp', 900),
    ('assets/images/DCC_Cover.jpg', 'assets/images/DCC_Cover-mobile.webp', 900),
    ('assets/images/about_Headshot.jpg', 'assets/images/about_Headshot-mobile.webp', 900),
]

for src, dst, max_w in files:
    img = Image.open(src).convert('RGB')
    w, h = img.size
    if w > max_w:
        ratio = max_w / w
        img = img.resize((max_w, int(h * ratio)), Image.LANCZOS)
    img.save(dst, format='WEBP', quality=72, optimize=True)
    print(f'created {dst}')
