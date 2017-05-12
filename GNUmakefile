build:
	mkdir $@

html: scratch2python.xml build
	@test -d build || mkdir build
	xmlto -o build html-nochunks scratch2python.xml

txt: scratch2python.xml build
	xmlto -o build txt scratch2python.xml

epub: scratch2python.xml build
	@mkdir build || true
	xmlto -o dist epub scratch2python.xml

pdf: scratch2python.xml build
	@mkdir build || true
	@mkdir dist  || true
	xmlto -o build fo scratch2python.xml
	fop build/scratch2python.fo dist/scratch2python.pdf

clean:	build
	@rm -rf build

