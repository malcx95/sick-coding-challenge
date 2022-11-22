# SICK Coding Challenge

Welcome to this coding challenge! This repository contains all the necessary code and instructions
to enter the competition, where you as a student can win a gift card worth 1000 SEK and increase your
chances of getting picked when applying for a [summer job at SICK Linköping](https://career.sicklinkoping.se/student#page-block-65246). Please read through
this README before entering, to make sure you understand the task at hand. __Good luck and have fun!__

## Task

Your task is to implement a special image filter in C++, which given an image and a radius ksize performs the following operation:

- For each pixel `p` in the image, consider a square region `R` around the pixel which is
    `2*ksize + 1` wide and high:
    - Find the most frequent pixel value `v` in `R` (including `p` itself).
    - Set the value of the pixel to `v`.
    - If multiple values are just as common, default to the lowest value of these.
    - Example: if `R` is `[(1, 1, 2), (3, 3, 3), (1, 2, 6)]`, then `v` should be 1.
- Pixels outside the image should be considered to have a value of 0.
    - For instance, in the top left corner, all pixels above and to the left have the value 0.
- Each color channel in the RGB image should be processed independently.

The region `R` is illustrated below, for when `ksize = 3`:

![](region.png "The region R")

__The focus of the task is to implement this as efficiently as possible__. Given the image below
to the left and a `ksize` of 23, the image below to the right shows the result of the operation :

Before                     |  After
:-------------------------:|:-------------------------:
![](lena.png "Before")     |  ![](ground_truth.png "After")

## How do I win?

__The correct solution which executes the fastest on the evaluation machine wins__. You may use as much memory as will be available to you. If two solutions execute equally fast within 1 millisecond, they will be graded on how readable, scalable and maintainable the code is and how easy the solution is to understand. If they are considered equal in this regard as well, the winner will be randomly picked among these.

### Prizes

The winner will recieve a gift card worth 1000 SEK at [Dustin Home](https://www.dustinhome.se/).
The people who submit the 2:nd to 5:th best solutions will recieve a smaller prize. Note that __only university students__ are eligible to win prizes, but
you are still welcome to try to solve the challenge anyway for fun.

__Everyone who submits a correct solution will have a greater chance at getting a summer job at SICK Linköping should they apply for one, especially if it's one of the winning solutions__.


## Rules and constraints

The code is to be written in C++ using the provided template `main.cpp`.
In here, you will find the following function:

```cpp
void perform_operation(unsigned char* input_image, unsigned char* output_image, int ksize)
{
    memcpy(output_image, input_image, HEIGHT*WIDTH*3);

    // your code goes here!
}
```

This is the function which performs the image operation, currently it does nothing but copy
the input to the output. This is where you can put your code (although you can of course create
more functions), but you may change anything in the file under the following conditions:

- __You may not include any libraries which are not part of the C/C++ standard libraries__. If the code does not compile with g++ without any compiler flags or if you have added other files to the folder, the solution will not be accepted.
- __You may not output anything or read anything other than the input image and output image, except for debugging purposes__. This includes reading and printing from the console as well as reading and writing files, so remove debug prints before submitting the solution.
- You may not change the way `main.cpp` reads the input or writes the output, the processed image must be put in the `output_image` array.
- All of the code performing the image operation (`perform_operation()`) must be surrounded with the code which times the solution. You may not move or remove the timing code, the only parts of the solution which are not timed are the reading and writing of the image buffers. Image processing code written outside the timing area will not be accepted.
- Do not change the name of `main.cpp`.

Furthermore:

- The final solution will be evaluated with a `ksize` of 23 (and may be optimized for this), __but it must work for all values of__ `ksize` __between 1 and 30__.
- `main.cpp` must compile on a Linux machine. Any solution which does not compile will be discarded.
- A ground truth image is provided, and your processed image at `ksize = 23` __must equal it pixel perfectly__.
- You may discuss a solution with your friends, as well as look up related theory, programming hints and documentation, __but the solution and your code must be your own, you may not use any complete solution you have found online or elsewhere__. You must be able to explain every part and design choice of your solution if asked about it.
- Although you can test your solution on the provided image, we will also test it on a different image with the same size when evaluating your solution, on which it also must work.

The solutions will be run using Ubuntu in Windows subsystem for Linux, meaning any solution built for WSL or a Linux machine will work. Assume that the machine used for grading will have 8 virtual CPU:s and 16 GB of RAM (some of it will be taken up by the OS of course). The image is provided as a single-dimensional array, a hint about how the pixels are arranged in the array can be found in the provided `get_index(int x, int y, int ch)` function, which calculates an index of the image given an `x` and `y` coordinate and a color channel `ch` (0 is red, 1 is green, 2 is blue):

```cpp
int get_index(int x, int y, int ch)
{
    int index = HEIGHT*WIDTH*ch + y*WIDTH + x;
    return index;
}
```

## How to test your solution

In order to test your solution, install [Python](https://www.python.org/) (version 3.7 or higher), and install the python packages `numpy` and `imageio` using `pip install -r requirements.txt`. Also, make sure you have the C++ compiler `g++` installed on your system. Now you can run the included python script `run.py` using `python run.py` (on some systems it's `python3 run.py`). Before you have implemented the solution, you will see this output:

```
Compiling...
Running...
Execution took 3.9e-05 seconds.
Saved image to lena_processed.png
Images don't quite match up.
Writing incorrect pixel image (the color of each pixel indicates which color channel is incorrect, black means correct)
Saved image to incorrect_pixels.png
```

The script converts the sample image `lena.png` into a raw image buffer file `lena_buf.dat`, which is the file to be read by the C++ code. Next, it compiles your code using `g++ main.cpp -O3 -o main`, before it runs the code. It then extracts how long it took and saves the image to the PNG file `lena_processed.png`. Next, it reads the ground truth image (can be seen in `ground_truth.png`) and compares the processed image against it. Here, since you have not implemented the solution yet, it says the images don't match up, and writes an error image. When a correct solution is implemented, this will be printed to the screen:

```
Compiling...
Running...
Execution took 3.795093 seconds.
Saved image to lena_processed.png
Solution is correct! Image matches with ground truth!
```

## What if I don't have Linux?

There are a few options here:

- You can use [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install), which allows you to run a minimal Linux virtual machine in Windows.
- You can install a full Linux virtual machine using [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
- You can use a Linux computer at the university, the B house of LiU has plenty.
- You could try using the windows C++ compiler, but you will then have to validate your solution yourself and cannot use any windows-specific libraries.

If you're on a Mac, everything _should_ work just as it does on Linux, including the same libraries, although this has not been tested by us.

## How to submit a solution

Send __only__ the `main.cpp` file to [malcolm.vigren@sick.se](mailto:malcolm.vigren@sick.se). Use the subject line "Code Challenge Solution". Write your contact details as a comment in the code:

```cpp
// Name: My Nameson
// Email: myemail@example.com
// Phone number (optional): 07xxxxxxxx
```

If you have any questions, send them to [malcolm.vigren@sick.se](mailto:malcolm.vigren@sick.se) with the subject line "Code Challenge Question". You can also create an issue in this repository if you run into any issues (try not to post any hints about the solution if you do so).

__Good luck and have fun!__

