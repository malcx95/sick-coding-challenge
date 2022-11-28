import numpy as np
import os
import imageio.v2 as imageio
import subprocess


IMAGE_PATH = "./baboon.png"


def convert_image(image, output_name):
    with open(output_name, "wb") as f:
        f.write(image.tobytes(order="F"))


def read_image(buffer_file, height, width):
    with open(buffer_file, 'rb') as f:
        buf = np.frombuffer(f.read(), dtype=np.uint8)
    return np.reshape(buf, (height, width, 3), order="F")


def write_png(image, filename):
    imageio.imwrite(filename, image)
    print(f"Saved image to {filename}")


def compile_code():
    subprocess.check_output(
        ["g++", "main.cpp", "-std=c++17", "-O3", "-o", "main"]
    )


def run_code():
    result = subprocess.run(
        ["./main"],
        capture_output=True,
        text=True
    )
    result.check_returncode()
    total_microseconds = int(result.stdout)
    return total_microseconds


def main():
    image = imageio.imread(IMAGE_PATH)
    height, width, _ = image.shape
    if not os.path.isfile("baboon_buf.dat"):
        print("Converting image to buffer...")
        convert_image(image, "baboon_buf.dat")

    print("Compiling...")
    try:
        compile_code()
    except subprocess.CalledProcessError:
        print("Compilation failed!")
        return
    print("Running...")
    total_microseconds = None
    try:
        total_microseconds = run_code()
        seconds = total_microseconds / 1000000
    except subprocess.CalledProcessError as e:
        print(f"Program failed to run: {e}")
        return

    print(f"Execution took {seconds} seconds.")

    converted_image = read_image("baboon_processed.dat", height, width)
    ground_truth = read_image("ground_truth.dat", height, width)

    write_png(converted_image, "baboon_processed.png")

    images_match = np.all(ground_truth == converted_image)
    if images_match:
        print("Solution is correct! Image matches with ground truth!")
    else:
        print("Images don't quite match up.")
        incorrect_mask = (ground_truth != converted_image).astype(np.uint8) * 255
        print("Writing incorrect pixel image (the color of each pixel indicates which color channel is incorrect, black means correct)")
        write_png(incorrect_mask, "incorrect_pixels.png")


if __name__ == "__main__":
    main()
