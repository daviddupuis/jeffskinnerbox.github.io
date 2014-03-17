# Pelican Driven Website
This is the source content and tools for creating my web site [www.jeffskinnerbox.me][03].
The site is generated using [Pelican][04], written mostly in [markdown][05],
and it is hosted using [Github Pages][06].
The web sites user-interface theme was developed by reusing & modifing the [pelican-bootstrap3][10] Pelican Theme and
reusing & modifing the [Bootswatch][09] [Bootstrap][07] theme called [flatly][08].
The web site also makes use of pages that were formated using the [IPython][12] tool [nbconvert][11].
All these tools (and [several more][13]) are used to create the content for the web site.

The building and publishing of the web site is manage via a Makefile, and the two Pelican configuration files

## Makefile
The Makefile is engineered for doing common tasks with the static site generator Jekyll, such as,

* generating your site
* creating a new post or page from a default template
* preview it in your default browser
* publish you draft posting
* transfering it to a remote git repository, a remote host/server or a local git repository.

### Make Commands
* `make html` - generate content for local server (i.e. localhost:8000)
* `make publish` - generate content ready for production server (i.e. via GitHub)
* `make github [COMMENT="string"]` - upload the content to production server and update GitHub (i.e. GitHub)
* `make process` - create thumbnails and other files required by the web site
* `make clean` - remove the generated HTML files for the web site (i.e. deletes output directory)
* `make regenerate` - automatically regenerate files upon modification
* `make serve [PORT=8000]` - serve site at http://localhost:8000
* `make devserver [PORT=8000]` - start/restart develop_server.sh
* `make stopserver` - stop local server
* `make backup` - Create backup of the blog's contents and tools

TBD
* `make article [TITLE="string"]` - Create a draft article
* `make page [TITLE="string"]` - Create a draft page

### A Collection of Notebooks for using IPython 
The following notebooks showcase multiple aspects of IPython, from its basic use to more advanced scenarios.
It has been create from my personal experimentation with IPython and from lifting notebooks from other sources.

## License
Copyright (c) 2013 Jeffrey C. Irland.  MIT Licensed, see [LICENSE][02] for details.



[01]:https://github.com/gummesson/jekyll-rake-boilerplate
[02]:https://github.com/jeffskinnerbox/jeffskinnerbox.github.com/blob/development/LICENSE.md
[03]:http://jeffskinnerbox.me/
[04]:http://blog.getpelican.com/
[05]:http://daringfireball.net/projects/markdown/
[06]:http://pages.github.com/
[07]:http://getbootstrap.com/
[08]:http://bootswatch.com/flatly/
[09]:http://bootswatch.com/
[10]:https://github.com/DandyDev/pelican-bootstrap3
[11]:http://ipython.org/ipython-doc/rel-1.0.0/interactive/nbconvert.html
[12]:http://ipython.org/
[13]:http://jeffskinnerbox.me/pages/this-blog-is-powered-by.html
[14]:
