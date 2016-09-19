
default:
	@latexmk -r latex.rc -pdf rootpy-talk.tex

clean:
	@latexmk -C
	@rm -rf _minted*
	@find . -name "*.log" -exec rm {} \;
	@find . -name "*-converted-to.pdf" -exec rm {} \;
	@find . -name "*.aux" -exec rm {} \;
	@find . -name "*.blg" -exec rm {} \;
	@find . -name "*.bbl" -exec rm {} \;
	@find . -name "*.bcf" -exec rm {} \;
	@find . -name "*.lst" -exec rm {} \;
	@find . -name "*.vrb" -exec rm {} \;
	@find . -name "*.nav" -exec rm {} \;
	@find . -name "*.snm" -exec rm {} \;
	@find . -name "*.run.xml" -exec rm {} \;
