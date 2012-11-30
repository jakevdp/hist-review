.SUFFIXES: .tex .pdf

all: histograms.pdf

LATEX = pdflatex
BIBTEX = bibtex
CHECK_RERUN = grep Rerun $*.log

histograms.pdf: histograms.tex histograms.bib
	${LATEX} histograms
	${BIBTEX} histograms
	( ${CHECK_RERUN} && ${LATEX} histograms ) || echo "Done."
	( ${CHECK_RERUN} && ${LATEX} histograms ) || echo "Done."
