.PHONY: all clean document.pdf fast

all : document.pdf

clean :
	rm -f *.aux *.bbl *.blg *.log *.out *.pdf *.lof *.lol *.lot *.toc *.ps *.parabola.* *.loa *.synctex.gz

document.pdf : 
	pdflatex -shell-escape thesis-main.tex
	bibtex thesis-main.aux
	pdflatex thesis-main.tex
	pdflatex thesis-main.tex

fast :
	pdflatex -shell-escape thesis-main.tex
