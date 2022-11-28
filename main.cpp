#include <iostream>
#include <chrono>
#include <fstream>
#include <cstring>


// Name:
// Email:
// Phone number (optional):


const int HEIGHT = 512;
const int WIDTH = 512;


void perform_operation(unsigned char* input_image, unsigned char* output_image, int ksize);

int main(int argc, char** argv)
{
    unsigned char input_image[HEIGHT*WIDTH*3];
    unsigned char output_image[HEIGHT*WIDTH*3];

    std::fstream fin("baboon_buf.dat", std::ios::in | std::ios::binary);
    fin.read((char*)input_image, HEIGHT*WIDTH*3);

    auto start = std::chrono::high_resolution_clock::now();
    perform_operation(input_image, output_image, 23);
    auto end = std::chrono::high_resolution_clock::now();

    std::fstream fout("baboon_processed.dat", std::ios::out | std::ios::binary);
    fout.write((char*)output_image, HEIGHT*WIDTH*3);

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << duration.count() << std::endl;

    return 0;
}

int get_index(int x, int y, int ch)
{
    int index = HEIGHT*WIDTH*ch + y*WIDTH + x;
    return index;
}


void perform_operation(unsigned char* input_image, unsigned char* output_image, int ksize)
{
    memcpy(output_image, input_image, HEIGHT*WIDTH*3);

    // your code goes here!
}
