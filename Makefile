PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
LOGOS=$(INPUTDIR)/images/logos
SUMMARY=$(INPUTDIR)/images/summary
BACKUPDIR=/home/jeff/tmp/blog_backup

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for a Pelican Web Site'
	@echo ' '
	@echo 'Usage:'
	@echo '   make html							generate content for local server (i.e. localhost:8000'
	@echo '   make clean						remove the generated HTML files'
	@echo '   make process						create thumbnails and other files required by the web site'
	@echo '   make regenerate					regenerate files upon modification'
	@echo '   make publish						generate content ready for production server (i.e. GitHub)'
	@echo '   make serve [PORT=8000]			serve site at http://localhost:8000'
	@echo '   make devserver [PORT=8000]		start/restart develop_server.sh'
	@echo '   make stopserver					stop local server'
	@echo '   make backup                   	create backup of the blogs content and tools'
	@echo '   make github [COMMENT="string"]	upload the content to production server (i.e. GitHub)'
	@echo ' '
	@echo 'Set the DEBUG variable to 1 to enable debugging (e.g. make html DEBUG=1)'
	@echo ' '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	rm $(BASEDIR)/*.pyc

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
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

# convert logo's to thumbnails and other such things
process:
	cd $(LOGOS); . ./create.sh
	cd $(SUMMARY); . ./create.sh
	cd $(BASEDIR)

publish: clean process
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

backup: html
	mkdir $(BACKUPDIR)
	cp -r $(BASEDIR)/content $(BACKUPDIR)
	cp -r $(BASEDIR)/theme $(BACKUPDIR)
	find . -maxdepth 1 -type f -exec cp {} $(BACKUPDIR) \;

github: publish
	ghp-import $(OUTPUTDIR)
	git push origin gh-pages:master
	git add --all
ifdef COMMENT
	git commit -m "$(COMMENT)"
else
	git commit -m "$(shell date)"
endif
	git push origin master:source

.PHONY: html help clean regenerate serve devserver publish backup process github
