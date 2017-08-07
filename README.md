# Scratch2Python

Have you outgrown Scratch? Looking to graduate to something more
advanced? Learn to make your very own side-scrolling platformer with
Python 3 and Pygame.

## How do I read this thing?

This git repository is primarily the place where I work on the code
that goes into the book. If all you want to do is read the book so you
can learn Python and Pygame, you can download the latest build of the
book from the `dist` folder.

Once I feel it's truly ready, I'll also publish the book on Smashwords
or some similar site, too.

## How do I report bugs?

Found an error? report it as an issue on Gitlab. I prefer Gitlab
because it's fully open source, and you can log in to it using your
Github credentials. However, if you must, you can report issues on
Github, too, where this book is mirrored in the interest of redundant
backup.

## How do hack on this thing?

If you want to learn Docbook, or you see some stupid Python code in
this book that you think could be better, then please feel free to
clone this repository and send me patches.

To work with this book with the least amount of resistance, you should
have:

* Linux
* A good text editor (I use and recommend [GNU Emacs](https://www.gnu.org/software/emacs)
* xmllint
* xmlto (you can get by with pure xsltproc)
* fop (if you want to go out to PDf)

The GNUmakefile included in this repo builds to text, HTML, PDF, and EPUB.