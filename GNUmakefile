TITLE = "Learn Python through games"
VER   = $(shell date +%y.%m.%d)

PDFTK = $(shell which pdftk 2>/dev/null || false)

ifeq "$(PDFTK)" ""
	PDFTK = pdf-stapler
endif

build:
	@mkdir build || true
	@mkdir dist  || true

concat:
	cat \
	article/dice.adoc \
	article/pygame.adoc \
	article/player.adoc \
	article/move.adoc \
	article/enemy.adoc \
	article/platform.adoc \
	article/gravity.adoc \
	article/jump.adoc \
	article/scroll.adoc \
	article/loot.adoc \
	article/score.adoc \
	article/throw.adoc \
	article/pip.adoc \
	article/gimp-alpha-channel.adoc \
	article/windows-python-install.adoc >> book.adoc


convert: build book.adoc
	asciidoc --backend docbook \
	--doctype book \
	--out-file book.xml \
	book.adoc

epub:	build concat convert
	@mkdir build/epub || true
	xsltproc --output build/epub/ docbook/epub/docbook.xsl book.xml
	#@cp img/cover_front.jpeg build/epub/OEBPS/cover.jpeg
	@find font -type f -iname "*ttf" -exec cp {} build/epub/OEBPS/ \;
	@cat style/style.css > build/epub/OEBPS/style.css 
	@sed -i 's_../img/__g' build/epub/OEBPS/index.html
	@sed -i 's_../img/__g' build/epub/OEBPS/content.opf
	@sed -i 's_jpeg" media-type=""/>_jpeg" media-type="image/jpeg"/>_g' build/epub/OEBPS/content.opf
	@sed -i 's_ncx"/>_ncx"/><item id="idm0" href="Andada-Regular.ttf" media-type="application/x-font-ttf"/><item id="idm2" href="cover.jpeg" media-type="image/jpeg"/><item id="idm3" href="junction-bold.ttf" media-type="application/x-font-ttf"/><item id="idm4" href="junction-light.ttf" media-type="application/x-font-ttf"/><item id="idm5" href="junction-regular.ttf" media-type="application/x-font-ttf"/><item id="idm6" href="style.css" media-type="text/css"/><item id="idm7" href="texgyrebonum-bold.ttf" media-type="application/x-font-ttf"/><item id="idm8" href="texgyrebonum-bolditalic.ttf" media-type="application/x-font-ttf"/><item id="idm9" href="texgyrebonum-italic.ttf" media-type="application/x-font-ttf"/><item id="idm10" href="texgyrebonum-regular.ttf" media-type="application/x-font-ttf"/>_' build/epub/OEBPS/content.opf
	@find build/epub/OEBPS/ -name "*html" -exec sed -i 's_<head>_<head>\n\n_' {} \;
	@find build/epub/OEBPS/ -name "*html" -exec sed -i 's_</head>_<link rel="stylesheet" href="style.css" /></head>_' {} \;
	@mv build/epub/OEBPS .
	@mv build/epub/META-INF .
	@cat article/mimetype > mimetype
	@zip -X -0 $(TITLE).epub mimetype
	@rm mimetype
	@zip -X -9 $(TITLE).epub -r META-INF OEBPS
	@rm -rf META-INF OEBPS
	@mv $(TITLE).epub dist


pdf:	build concat convert
	@sed -i 's_fileref=\"img/_fileref=\"../img/_g' book.xml
	xsltproc --output build/tmp.fo \
	 --stringparam paper.type  Letter \
	 --stringparam page.width 8.25in \
	 --stringparam page.height 10in \
	 --stringparam ulink.show 0 \
	 --stringparam redist.text "sa" \
	 --stringparam column.count.titlepage 1 \
	 --stringparam column.count.lot 1 \
	 --stringparam column.count.front 1 \
	 --stringparam column.count.body 1 \
	 --stringparam column.count.back 1 \
	 --stringparam column.count.index 2 \
	 --stringparam footer.column.widths "1 0 0" \
	 --stringparam body.font.master 10 \
	 --stringparam body.font.size 10 \
	 --stringparam page.margin.inner .5in \
	 --stringparam page.margin.outer .5in \
	 --stringparam page.margin.top .5in \
	 --stringparam page.margin.bottom .5in \
	 --stringparam title.margin.left 0 \
	 --stringparam title.start.indent 0 \
	 --stringparam body.start.indent 0 \
	 --stringparam chapter.autolabel 0 \
	style/mystyle.xsl book.xml
	fop -c style/rego.xml \
	build/tmp.fo \
	build/tmp.pdf 2>&1 | tee log.txt

clean:
	rm book.adoc || true
	rm book.xml || true
	rm -r build  || true
	rm -r dist || true
	rm log.txt || true
