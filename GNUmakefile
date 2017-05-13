build:
	mkdir $@

check:	scratch2python.tmp.xml
	@xmllint --noout scratch2python.tmp.xml

cat:
	cat header.xml topics/preface.xml \
	topics/intro.xml \
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
	topics/colophon.xml > scratch2python.tmp.xml

html: cat check scratch2python.tmp.xml build
	@test -d build || mkdir build
	xmlto -o build --skip-validation html-nochunks scratch2python.tmp.xml

txt: cat check scratch2python.tmp.xml build
	xmlto -o build --skip-validation txt scratch2python.tmp.xml

epub: cat check scratch2python.tmp.xml build
	@mkdir build || true
	xmlto -o dist --skip-validation epub scratch2python.tmp.xml

pdf: cat check scratch2python.tmp.xml build
	@mkdir build || true
	@mkdir dist  || true
	xmlto -o build fo --skip-validation scratch2python.tmp.xml
	fop build/scratch2python.tmp.fo dist/scratch2python.pdf

clean:
	@rm -rf build || true
	@rm scratch2python.tmp.xml


