PY = python
PELICAN = pelican
PELICANOPTS = 

BASEDIR = $(CURDIR)
METADATA = $(BASEDIR)/metadata
INPUTDIR = $(BASEDIR)/content
DRAFTDIR = $(INPUTDIR)/drafts
OUTPUTDIR = $(BASEDIR)/output
CONFFILE = $(BASEDIR)/pelicanconf.py
PUBLISHCONF = $(BASEDIR)/publishconf.py
LOGOS = $(INPUTDIR)/images/logos
SUMMARY = $(INPUTDIR)/images/summary

BACKUPDIR = "/home/jeff/tmp/blog_backup_$(shell date | tr ': ' '_')"
SLUG = $(shell echo $(TITLE) | tr '[:upper:]' '[:lower:]' | tr -d '!@$%^&*()?:;|{}[]",.' | tr -s ' ' | tr '_ ' '-')
AUTHOR = "Jeff Irland"
TMPFILE = "/tmp/temp.file"

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for a Pelican Web Site'
	@echo ' '
	@echo 'Usage:'
	@echo '   make html                         generate content for local server'
	@echo '   make clean                        remove the generated HTML files'
	@echo '   make process                      create thumbnails for the web site'
	@echo '   make regenerate                   regenerate files upon modification'
	@echo '   make publish                      generate content for production server'
	@echo '   make serve [PORT=8000]            serve site at http://localhost:8000'
	@echo '   make devserver [PORT=8000]        start/restart develop_server.sh'
	@echo '   make stopserver                   stop local server'
	@echo '   make backup                       create backup of blogs content and tools'
	@echo '   make github [COMMENT="<string>"]  upload the content to production server'
	@echo '   make article TITLE="<string>"     create new article with title <string> and start vim'
	@echo ' '
	@echo 'Set the DEBUG variable to 1 to enable debugging (e.g. make html DEBUG=1)'
	@echo ' '

# Create a draft article: make article TITLE="<string>"
article:
ifdef TITLE
	cat $(METADATA)/article.metadata > $(TMPFILE)
	cat $(TMPFILE) | sed 's/Title: xxx/Title: $(TITLE)/' | sed 's/Slug: xxx/Slug: $(SLUG)/' | sed 's/Author: xxx/Author: $(AUTHOR)/' > $(DRAFTDIR)/$(SLUG).md
	vim $(DRAFTDIR)/$(SLUG).md
else
	echo 'You must provide a title.  Usage: make article TITLE="<string>"'
	exit
endif

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	rm -rf $(BASEDIR)/*.pyc $(BASEDIR)/.pelican.pid $(BASEDIR)/.srv.pid

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	kill -9 `cat .pelican.pid`
	kill -9 `cat .srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

# convert logo's to thumbnails (and other such things) for web site formatting
process:
	rm -rf $(LOGOS)/thumbnail $(SUMMARY)/thumbnail
	mkdir $(LOGOS)/thumbnail $(SUMMARY)/thumbnail
	cd $(LOGOS); . ./create.sh
	cd $(SUMMARY); . ./create.sh
	cd $(BASEDIR)

# prepare for publishing content to your web site
publish: clean process
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

# make a backup of your web site content
backup: html
	mkdir $(BACKUPDIR)
	cp -r $(BASEDIR)/content $(BACKUPDIR)
	cp -r $(BASEDIR)/theme $(BACKUPDIR)
	find . -maxdepth 1 -type f -exec cp {} $(BACKUPDIR) \;

# push the web site to its domain and place the content into GitHub
github: backup publish
	ghp-import $(OUTPUTDIR)
	git push origin gh-pages:master
	git add --all
ifdef COMMENT
	git commit -m "$(COMMENT)"
else
	git commit -m "Created $(shell date)"
endif
	git push origin master:source

.PHONY: html help clean regenerate serve devserver publish backup process github
