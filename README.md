# Pelican Driven Website
This is the source code for my web site [www.jeffskinnerbox.me][03].
The site is generated using [Pelican][04],
written mostly in [markdown][05],
and it is hosted using [Github Pages][06].

## Makefile
The Makefile is engineered for doing common tasks with the static site generator Jekyll, such as,

* generating your site
* creating a new post or page from a default template
* preview it in your default browser
* publish you draft posting
* transfering it to a remote git repository, a remote host/server or a local git repository.

### Rake Commands
This information was copied from  https://github.com/gummesson/jekyll-rake-boilerplate
* `rake post["Title"]` -- creates a new post in the `_posts` directory by reading the default template file, adding the title you've specified and generating a filename by using the current date and the title.
* `rake draft["Title"]` -- creates a new post in the `_drafts` directory by reading the default template file, adding the title you've specified and generating a filename.
* `rake publish` moves a post from the `_drafts` directory to the `_posts` directory and appends the current date to it. It'll list all drafts and then you'll get to choose which draft to move by providing a number.
* `rake page["Title","path/to/folder"]` creates a new page. If the file path is not specified the page will get placed in the site's source directory.
* `rake build` just generates the site.
* `rake watch` generates the site and watches it for changes. If you want to generate it with a post limit, use `rake watch[1]` or whatever number of posts you want to see. If you want to generate your site with your drafts, use `rake watch["drafts"]`.
* `rake preview` launches your default browser and then builds, serves and watches the site.
* `rake deploy["Commit message"]` adds, commits, and pushes your site to the site's remote git repository with the commit message you've specified. It also uses the `rake build` task to generate the site before it goes through the whole git process.
* `rake transfer` uses either `robocopy` or `rsync` to transfer your site to a remote host/server or a local git repository. It also uses the `rake build` task to generate the site before it goes through the whole transfering process.

### A Collection of Notebooks for using IPython 
The following notebooks showcase multiple aspects of IPython, from its basic use to more advanced scenarios.
It has been create from my personal experimentation with IPython and from lifting notebooks from other sources.

## Sources and Credits
The Rakefile has been adopted from [Jekyll Rake Boilerplate][01].

## License
Copyright (c) 2013 Jeffrey C. Irland.  MIT Licensed, see [LICENSE][02] for details.



[01]:https://github.com/gummesson/jekyll-rake-boilerplate
[02]:https://github.com/jeffskinnerbox/jeffskinnerbox.github.com/blob/development/LICENSE.md
[03]:http://jeffskinnerbox.me/
[04]:http://blog.getpelican.com/
[05]:http://daringfireball.net/projects/markdown/
[06]:http://pages.github.com/
