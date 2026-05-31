import os
import sys
import subprocess

def install_pillow():
    try:
        import PIL
        print("Pillow is already installed.")
    except ImportError:
        print("Pillow is missing. Installing Pillow...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
            print("Pillow successfully installed!")
        except Exception as e:
            print(f"Error installing Pillow: {e}")
            sys.exit(1)

install_pillow()

from PIL import Image

def convert_png_to_webp():
    img_dir = os.path.join(os.path.dirname(__file__), "source", "img")
    if not os.path.exists(img_dir):
        print(f"Directory not found: {img_dir}")
        return

    png_files = [f for f in os.listdir(img_dir) if f.endswith(".png")]
    print(f"Found {len(png_files)} PNG files to optimize.")

    for file_name in png_files:
        png_path = os.path.join(img_dir, file_name)
        base_name = os.path.splitext(file_name)[0]
        webp_name = f"{base_name}.webp"
        webp_path = os.path.join(img_dir, webp_name)

        # Skip if already exists and is valid
        if os.path.exists(webp_path):
            print(f"Optimized WebP already exists for {file_name}. Skipping.")
            continue

        try:
            print(f"Optimizing {file_name}...")
            original_size = os.path.getsize(png_path) / (1024 * 1024) # MB
            
            with Image.open(png_path) as img:
                # Save as WebP with 80% quality (great balance of quality and file size)
                img.save(webp_path, "WEBP", quality=80, method=6)
                
            new_size = os.path.getsize(webp_path) / (1024 * 1024) # MB
            savings = (1 - (new_size / original_size)) * 100
            print(f"✓ Converted to WebP: {webp_name} | Size: {original_size:.2f}MB -> {new_size:.2f}MB ({savings:.1f}% saved!)")
        except Exception as e:
            print(f"✗ Failed to convert {file_name}: {e}")

if __name__ == "__main__":
    convert_png_to_webp()
