.SUFFIXES: .tex .pdf

all: histograms.pdf

LATEX = pdflatex
BIBTEX = bibtex
CHECK_RERUN = grep Rerun $*.log

%.pdf: %.tex
	${LATEX} $*
	${BIBTEX} $*
	( ${CHECK_RERUN} && ${LATEX} $* ) || echo "Done."
	( ${CHECK_RERUN} && ${LATEX} $* ) || echo "Done."