echo off
title Clear Directory
echo Starting cleaning process... 

rm -f *.aux *.bbl *.blg *.log *.out *.pdf *.lof *.lol *.lot *.toc *.ps *.parabola.* *.loa *.synctex.gz

echo Cleaning process fininshed!

echo Making new pdf...
pdflatex -shell-escape thesis-main.tex
bibtex thesis-main.aux
pdflatex thesis-main.tex
pdflatex thesis-main.tex
echo Done