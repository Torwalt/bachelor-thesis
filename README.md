# Thesis Template
This is a document template for bachelor and master theses.

## How to use the files provided here:
### Building the latex
The best way to build the document is to use the makefile.
<code> make all </code> or just <code>make</code>
will build the document.

If on windows run: 
<code> makefile.bat </code>

### Clean up befor commit
You can use <code> make clean </code> to delete all build files.

### Quick build
You can use <code> make fast </code>, to run a quick build. This will not rebuild the bibliography and only run pdflatex once. Some changes need three compilations to be reflected in the output pdf.

