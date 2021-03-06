# A Catalogue of Sampling Algorithms for Sensor Data

## Compiled Version

<https://drive.google.com/file/d/1E7HOBt4HsYQrdSpNTzBRjPzJfHmKVleP/view?usp=sharing>

## Published Version

This thesis was published (in adapted/extended form by Dimitrios Giouroukis) in DEBS 2020.

<https://2020.debs.org/accepted-papers/>

<https://www.youtube.com/watch?v=riBJXRpuDuA&feature=youtu.be>

## How to use the files provided here

### Building the latex

The best way to build the document is to use the makefile.

You will need pdflatex to compile the files.

`make all` or just `make` in the `latex` directory will build the document.

### Clean up before commit

You can use `make clean` to delete all build files.

### Quick build

You can use `make fast`, to run a quick build. This will not rebuild the bibliography and only run pdflatex once. Some
changes need three compilations to be reflected in the output pdf.
