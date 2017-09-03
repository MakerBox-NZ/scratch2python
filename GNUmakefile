build:
	mkdir $@

check:	scratch2python.tmp.xml
	@xmllint --noout scratch2python.tmp.xml

coverp:	img/cover_front.jpg
	@test -d build || mkdir build
	@convert img/cover_front.jpg build/front.pdf

cat:
	cat header.xml topics/preface.xml \
	topics/intro.xml \
	topics/pygame.xml \
	topics/dice.xml \
	topics/world.xml \
	topics/player.xml \
	topics/move.xml \
	topics/platform.xml \
	topics/gravity.xml \
	topics/collision.xml \
	topics/jump.xml \
	topics/scroll.xml \
	topics/loot.xml \
	topics/enemy.xml \
	topics/score.xml \
	topics/osdc.xml \
	topics/colophon.xml > scratch2python.tmp.xml

html: cat check coverp scratch2python.tmp.xml build
	@test -d build || mkdir build
	xmlto -o build --skip-validation html-nochunks scratch2python.tmp.xml
	@mv dist/scratch2python.tmp.html dist/scratch2python.html

txt: cat check coverp scratch2python.tmp.xml build
	xmlto -o dist --skip-validation txt scratch2python.tmp.xml
	@mv dist/scratch2python.tmp.txt dist/scratch2python.txt

epub: cat check coverp scratch2python.tmp.xml build
	@mkdir build || true
	xmlto -o dist --skip-validation epub scratch2python.tmp.xml
	@mv dist/scratch2python.tmp.epub dist/scratch2python.epub

pdf: cat check coverp scratch2python.tmp.xml build
	@mkdir build || true
	@mkdir dist  || true
	xsltproc --output tmp.fo \
	 --stringparam paper.type  A4 \
	 --stringparam page.width 8in \
	 --stringparam page.height 10in \
	 --stringparam redist.text "sa" \
	 --stringparam admon.graphics 1 \
	 --stringparam admon.graphics.path "img/" \
	 --stringparam admon.graphics.extension ".png" \
	 --stringparam column.count.titlepage 1 \
	 --stringparam column.count.lot 1 \
	 --stringparam column.count.front 1 \
	 --stringparam column.count.body 1 \
	 --stringparam column.count.back 1 \
	 --stringparam column.count.index 2 \
	 --stringparam body.font.family "Liberation Serif" \
	 --stringparam title.font.family "Prociono" \
	 --stringparam symbol.font.family "UniCons" \
	 --stringparam footer.column.widths "1 0 0" \
	 --stringparam body.font.master 10 \
	 --stringparam body.font.size 10 \
	 --stringparam page.margin.inner .5in \
	 --stringparam page.margin.outer .5in \
	 --stringparam page.margin.top .45in \
	 --stringparam page.margin.bottom .45in \
	 --stringparam title.margin.left 0 \
	 --stringparam shade.verbatim 1 \
	 --stringparam title.start.indent 0 \
	 --stringparam body.start.indent 0 \
	 --stringparam chapter.autolabel 0 \
	style/mystyle.xsl scratch2python.tmp.xml
	fop -c style/rego.xml tmp.fo build/tmp.pdf
	pdftk A=build/tmp.pdf B=build/front.pdf cat B A2-end output dist/scratch2python.pdf || mv build/tmp.pdf dist/scratch2python.pdf

clean:
	@rm -rf build || true
	@rm scratch2python.tmp.xml
