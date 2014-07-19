DEBUG ?= 0

# Use Bash shell instead of the default /bin/sh
SHELL := /bin/bash

# Shell loops will continue past errors without this.
EXIT_ON_ERROR = set -e

# Parameters set for debugging
ifeq ($(DEBUG), 1)
	DEBUG_PELICANOPTS = -D
else
	DEBUG_PELICANOPTS =
endif

# These options will be passed to "python".
PYTHONOPTS =

# These options will be passed to "pelican".
PELICANOPTS += $(DEBUG_PELICANOPTS)

# These are the locations where temporary files will be stored.
TMP = $(HOME)/tmp
TMPFILE = "$(TMP)/temp_file_$(shell date +%H%M%S)"

# Directory structure of the blogging directory (at least what's required for this work flow).
BASEDIR = $(HOME)/blogging
METADATA = $(BASEDIR)/metadata
INPUTDIR = $(BASEDIR)/content
OUTPUTDIR = $(BASEDIR)/output
ARTICLESDIR = $(INPUTDIR)/articles
DRAFTSDIR = $(INPUTDIR)/drafts
EXTRADIR = $(INPUTDIR)/extra
IDEASDIR = $(INPUTDIR)/ideas
IMAGESDIR = $(INPUTDIR)/images
NOTEBOOKSDIR = $(INPUTDIR)/notebooks
PAGESDIR = $(INPUTDIR)/pages
LOGOS = $(IMAGESDIR)/logos
SUMMARY = $(IMAGESDIR)/summary

CONFFILE = $(BASEDIR)/pelicanconf.py
PUBLISHCONF = $(BASEDIR)/publishconf.py

# If a backup is requested, this is the backup file's location/name.
BACKUPDIR = "$(TMP)/blog_backup_$(shell date | tr ': ' '_')"

# If an idea, draft, or article is created, this will capture the title
# and make it part of the URL for the document.
SLUG = $(shell echo "$(TITLE)" | tr -d '!@$%^&*()?:;|{}[]",.' | tr '[:upper:]' '[:lower:]' | tr -s ' ' | tr '_ ' '-' | tr -s '-' )

# Author of the idea, draft, or article
AUTHOR = Jeff Irland

# Date and time stamp to be applied to an article's header.
DATETIME =  $(shell date "+%Y-%m-%d %H:%M")

################################################################################

help:
	@echo 'Makefile for a Pelican Web Site'
	@echo ' '
	@echo 'Usage:'
	@echo '   make draft TITLE="<str>"       starting with a file in /ideas, '
	@echo '                                    create a file for /drafts with title <str>'
	@echo '   make article                   pick a file in /drafts to move to /articles'
	@echo '   make html                      generate content for local server'
	@echo '   make clean                     remove the generated HTML files'
	@echo '   make process                   create thumbnails for the web site'
	@echo '   make regenerate                regenerate files upon modification'
	@echo '   make publish                   generate content for production server'
	@echo '   make serve [PORT=8000]         serve site at http://localhost:8000'
	@echo '   make startserver [PORT=8000]   start/restart develop_server.sh'
	@echo '   make stopserver                stop the local server'
	@echo '   make backup                    create a backup of the blogs content and tools'
	@echo '   make github [COMMENT="<str>"]  upload the content to production server'
	@echo ' '
	@echo 'Set the DEBUG variable to 1 to enable debugging (e.g. make html DEBUG=1)'
	@echo ' '

# Create a draft file for $(BASEDIR)/content/drafts diretory from a file within the $(BASEDIR)/content/ideas directory
draft:
ifdef TITLE
	@echo " "
	@echo "Enter the number of the file you wish to process. Pick the last number to exit."
	@$(EXIT_ON_ERROR) ; \
	PS3="Enter Number: " ; \
	cd $(IDEASDIR) ; \
	select file in * exit ; \
	do \
    	case $$file in \
        	exit) \
            	echo "Exiting from select loop!" ; \
            	exit 1 ; \
            	;; \
        	*) \
            	echo "You picked the file $$file" ; \
				mv $$file $(TMPFILE) ; \
            	break ; \
            	;; \
    	esac ; \
	done
	cat $(METADATA)/article.metadata $(TMPFILE) | sed 's/Title: xxx/Title: $(TITLE)/' | sed 's/Slug: xxx/Slug: $(SLUG)/' | sed 's/Author: xxx/Author: $(AUTHOR)/' > $(DRAFTSDIR)/$(SLUG).md
	vim $(DRAFTSDIR)/$(SLUG).md &
else
	@echo 'You must provide a title.  Usage: make article TITLE="<str>"'
	@exit
endif


# Create a article file for $(BASEDIR)/content/articles diretory from a file within the $(BASEDIR)/content/drafts directory
article:
	@echo " "
	@echo "Enter the number of the file you wish to process. Pick the last number to exit."
	@$(EXIT_ON_ERROR) ; \
	PS3="Enter Number: " ; \
	cd $(DRAFTSDIR) ; \
	select file in * exit ; \
	do \
    	case $$file in \
        	exit) \
            	echo "Exiting from select loop!" ; \
            	exit 1 ; \
            	;; \
        	*) \
            	echo "You picked the file $$file" ; \
				sed 's/Date: 2100-01-01 00:00/Date: $(DATETIME)/' $$file > $(ARTICLESDIR)/$$file ; \
				mv $$file $(TMPFILE) ; \
            	break ; \
            	;; \
    	esac ; \
	done


html:
	pelican $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)


clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	rm -rf $(BASEDIR)/*.pyc $(BASEDIR)/.pelican.pid $(BASEDIR)/.srv.pid


regenerate:
	pelican -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)


serve:
ifdef PORT
	cd $(OUTPUTDIR) && python $(PYTHONOPTS) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && python $(PYTHONOPTS) -m pelican.server
endif


# This runs in the background, Pelican and a HTTP Server.  As updates are made to
# the blog pages and articles, the blog can be view at "http://localhost:8000/" using a browser.
startserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif
	@echo 'Started Pelican and SimpleHTTPServer processes running in background.'


# This stops the Pelican and HTTP Server running in the background.
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
	pelican $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)


# make a backup of your web site content
backup: html
	mkdir $(BACKUPDIR)
	cp -r $(BASEDIR)/content $(BACKUPDIR)
	cp -r $(BASEDIR)/theme $(BACKUPDIR)
	find . -maxdepth 1 -type f -exec cp {} $(BACKUPDIR) \;


# push the web site to its domain and place the contents into GitHub
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


.PHONY: draft article html help clean regenerate serve startserver publish backup process github
