Title: Building My New Blog Using Jekyll...Scratch That...Pelican
Date: 2014-02-21 18:20
Category: Blogging
Tags: Jekyll, Pelican, Blog, Bootstrap
Slug: building-my-new-blog-using-jekyll-scratch-that-pelican
Author: Jeff Irland
Summary: This article give a "how I setup Pelican" outline from start to finish. It shows you how to install Pelican, add supporting tools like Markdown, Disqus, Google Analytics, Bootstrap, etc.  It also show you how to use tools Make and GitHub to create a easy to maintain workflow.

* [Migrating from Octopress to Pelican](http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/)
* [How I setup Pelican](http://terriyu.info/blog/posts/2013/07/pelican-setup/)

Prior to setting up this blog, I initially started with [WordPress][47],
I felt limited by it and then  I discovered that many tech-savvy people were
using static site generators like [Jekyll][06] or [Pelican][10].
Static web site don't generate web pages upon request, like WordPress.
Instead, software on your local machine creates webpages and then these pages are uploaded to the webhost.
The webpages have fixed content, hence the description "static site."
For a personal blog, a static site can makes a lot of sense because it more secure, 
there is no maintenance of web server software,
your can write the blog in friendly language like [Markdown][19],
you can easily control versioning of you content with tools like Git,
and you blog is easily ported to any other site.

My orginal plan was to port [my WordPress blog][11] to GitHub and use [Jekyll][06].
I did this, and I used it for several months, but felt less and less satisfied with my choose.
I then read the post "[Moving Blogs to Pelican][01]" and I resounated with nearly ever word.
As a result, I have now change my direction, and ported my blog from Jekyll to [Pelican][10].
Like Jekyll, Pelican is a static site generator requiring no database or server-side logic,
but it makes use of Python, Make, and Shell, not Ruby.
This was an important factor, I never had a need to use Ruby and why should my blog force the issue?

The contents of a Pelican  blog is either a post (in Pelican terminalogy, an article) or a page.
The raw, unprocessed content (e.g. pages, articles, drafts, images, etc.)
is contained in a directory called `content`.
Both articles and pages can be written in
[Markdown][19], [reStructuredText][20], [AsciiDoc][21], or even raw [HTML][25].
Both articles and pages can have meta-data at the top of the document containing such things as
title, publication date, tags, etc. and even arbitrary custom meta-data.

The processed, ready to be published materials are contained in a directory called `output`.
It is this directory that will be pushed to your web server.
Their are other things that make up a Pelican blog,
such as plugins, themes, make files, and other publishing tools.
More on this later.

To create this posting, I leveraged the [Pelican Development Blog][02],
which provide much of the detail documentation needed
but to get started I followed the advice of the [Tutorial: Generating Static Sites with Pelican][07],
[Pelican Getting Started Guide][03], and [Pelican and Github Pages][04] very useful.
Also, reading [Creating a Blog with Python Pelican][17] and [How I setup Pelican][18] prove very helpful.
You can find the latest Pelican code, along with its [themes and plugins on GitHub][05].
You might find more information on [Pelican's GetHub][23] and [Pelican's Tips & Tricks][24].

##### Installing Pelican and Creating a Python Virtualenv
Pelican is a [Python][48] based tool.
To assure I have a clean Python envirnment to work in, that doesn't conflict with other Python work,
create a virtual environment using `virtualenv[49]`.
To install Pelican and other Python package dependencies in a virtual environment,
I roughly followed the instructions in the [official Pelican documentation][50].
See below:

```shell
cd ~
virtualenv --python python2.7 --no-site-packages blogging
cd blogging
source bin/activate
pip install Pelican==3.3
pip install Markdown
pip install typogrify
pip install ghp-import
deactivate
```

**Note:** Don't use `sudo` when installing these Python packages in a virtual environment,
otherwise you'll end up installing them globally,
which defeats the purpose of using virtual environments.

#### Run Quickstart Pelican
Pelican now comes with a quickstart command that will create a skeleton directory structure for your project.
When running the command will ask you a series of questions.
See the posting [How I setup Pelican][18] for recommendations on how to answer the questions.
I (more or less) followed what was done in this article.

```shell
pelican-quickstart
```

At this point, running the command `pelican -s pelicanconf.py` in the `blogging`
directory would generate all static files for the blog using the
default Pelican theme `notmyidea` into the `output/` directory.
You can no serve this directory as you would any other static html files.
You can test this out by doing the following:

```shell
make html
make serve
```

Then using a browser, enter `localhost:8000`.
Nothing much will be there since not content has been created but you see the shell for
your `notmyidea` themed blog.

#### Fork & Clone Pelican Themes and Plugins
I wanted to leverage the official [Pelican themes][12] and [Pelican plugins][13],
and have them under version control,
so I performed the standard procedure of [forking/cloning the GitHub][14].
First step is to fork these repositories on GitHub.
I did the following:

```shell
cd ~/blogging/pelican-plugins
git clone https://github.com/jeffskinnerbox/pelican-plugins.git
git remote add upstream https://github.com/jeffskinnerbox/pelican-plugins.git
git fetch upstream

cd ~/blogging/pelican-themes
git clone https://github.com/jeffskinnerbox/pelican-themes.git
git remote add upstream https://github.com/jeffskinnerbox/pelican-themes.git
git fetch upstream
```

#### Set Up Git
With what has been done so far,
you have the beginings of a project structure and you should initiate a Git repository to control it.
Do the `git init` and create a rudimentary `.gitignore` file:

```shell
git init
vi .gitignore

# Content of the .gitignore file:
*.pid
*.pyc
*.swp
output/
```

More work needs to be done, so updates will be required.
I have posted a final and more complete version of `.gitignore` [on Gist][51].

#### Pelican Configuration File
Pelican is configurable via setting is a Python module called `pelicanconf.py`.
The settings you define in this configuration file will be used within the Pewlican
templates that are part of the themes and to control Pelican processing.
The basic idea is that you can point Pelican at the template files in your
`pelican-themes/<theme>/templates/` directory to generate all static html files.
Pelican uses [Jinja][15] for its templating language.
In these templates, you should have access to all variables from `pelicanconf.py`
as well as template-specific variables (See “[Template and Variables][16]”
section of the Pelican documentation).

Think of Pelican as having two primary modes of operation:
local development and production deployment (i.e., `pelicanconf.py` and `publishconf.py`, respectively).
When developing locally, settings for things like Google Analytics and Disqus
are deliberately left out of `pelicanconf.py` by design.
Including those settings in local testing can have adverse effects:
inaccurate site statistics, spurious comment threads, and other unanticipated side effects.

When it is time to publish your site,
then of course you want those settings to be included.
The way to do that is to ensure your `publishconf.py` is being referenced at publish time:
`pelican content -s publishconf.py`.
I posted my `pelicanconf.py` and `publishconf.py` files on Gist here and here.  XXXX FINISH THIS XXXX

#### Pelican's Markdown
Pelican will support [Markdown][19], [reStructuredText][20], and [AsciiDoc][21]
for the creation of content.
I will be using Markdown to write my blog posts.
By default, Pelican uses a flavor of Markdown that comes with some [extentions][22].
I especially like using the footnotes extension......

#### Creating Content
Pelican considers “articles” to be chronological content, such as posts on a blog,
and thus associated with a date (e.g. a web posting about some project underway).
Pelican also supports “pages” that are usually not temporal in nature
and are used for content that does not change very often (e.g., “About Me” page).
Also like Jekyll, each of the content files contain metadata about the file.
When using Markdown, that metadata looks like:

     XXXX FINISH THIS XXXX
    Title: My Super Title For My Suppoer Post
    Date: 2010-12-03 10:20
    Category: Python
    Tags: pelican, publishing
    Slug: my-super-post
    Author: Jeff Irland
    Summary: Short version for index and feeds
    
    This is the content of my super blog post.

To Run it
pelican -s pelicanconf.py -o output content
cd output
python -m SimpleHTTPServer
# then localhost:8000 in your browser

OR

( pelican -s pelicanconf.py -o output content && cd output && python -m SimpleHTTPServer ) && cd -

OR

make html
make serve

OR

pelican --autoreload -s pelicanconf.py -o output content
make serve

#### Processing Content
Pelican support several automation tools for the processing of content and publishing.
It supports [make][09] and [fabric][08] build tools, but I'll onluy cover make here.
A Makefile is automatically created during the pelican-quickstart process.
Make can be used to automate the processing of content. 

If you want to generate your site, run:

    make html

If you’d prefer to have Pelican automatically regenerate your site every time a change is detected
(which is handy when testing locally), use the following command instead:

    make regenerate

To serve the generated site so it can be previewed in your browser at http://localhost:8000/:

    make serve

Normally you would need to run make regenerate and make serve in two separate terminal sessions,
but you can run both at once via:

    make devserver

The above command will simultaneously run Pelican in regeneration mode
as well as serve the output at http://localhost:8000.
Once you are done testing your changes, you should stop the development server via:

    ./develop_server.sh stop

When you’re ready to publish your site, you can upload it via the method(s)
you chose during the pelican-quickstart questionnaire.
I modified the `Makefile` to include the following:

    make github

#### Adding Content
The next step is to begin to adding content to the content folder that has been created for you.
Enter the `content` folder and create your markdown content files there.
While you are writing your post, you can generate your post using:

    make server

### Creating Pelican Theme
* [Theming Pelican with a little Boostrap](http://andresjruiz.com/theming-pelican-with-a-little-boostrap.html)
* [Pelican Bootstrap 3 theme released](http://dandydev.net/blog/pelican-bootstrap3-theme-released)
* [pelican-bootstrap3](http://floss.zoomquiet.io/data/20131218101822/index.html)

Pelican Tmemes allow you to seperate the contents of your blog from its look-and-feel.
You can find images of the available themes at [Pelican Themes][26].
This is accomplished in part via use of [Jinja][15] template engine to render Pelican pages and articles. 
Pelican makes it easy to make your own themes but clearly it is easiest when
you start with a theme that is close to what you want.
I started with [pelican-bootstrap3][27] to creat my theme.
This theme makes use of [Bootstrap 3][28],
a front-end framework for developing [responsive web sites][34].

# Customizing Bootstrap
1. Forking/cloning will let you fetch the new upcoming versions of Bootstrap easily
2. Do not modify the bootstrap.css file
3. Create your own css file and overwrite whenever you want original bootstrap stuff

* ["best practices" for customizing Bootstrap css template](http://stackoverflow.com/questions/8596794/customizing-bootstrap-css-template)
* [Customizing Bootstrap](http://coding.smashingmagazine.com/2013/03/12/customizing-bootstrap/)
* [How to customize Twitter Bootstrap to fit your web design](http://www.codeproject.com/Articles/594098/How-to-customize-Twitter-Bootstrap-to-fit-your-web)
* [Less Like Bootstrap – 5 Ways To Customize Your Designs](http://blog.jetstrap.com/2013/07/less-like-bootstrap/)
* [How to modify Bootstrap simply and effectively](http://www.webdesignerdepot.com/2013/07/how-to-modify-bootstrap-simply-and-effectively/)
* [Bootstrap ThemeRoller](http://www.bootstrapthemeroller.com/)
* [Free themes for Bootstrap](http://bootswatch.com/#gallery)
* [Shine Your Boots! Customizing Twitter Bootstrap](http://www.cognizo.com/2012/04/twitter-bootstrap-customization/)
* [Twitter Bootstrap 101](http://webdesign.tutsplus.com/series/twitter-bootstrap-101/)


Bootstrap is a popular web framework, and as a result of its growing popularity,
it has created uniformity between many websites.
[Bootswatch][35] was created to somewhat combate this trend,
enable developers, still using Bootstrap to try on a new look,
without investing much time or energy.

##### Pelican's File Structure
Jekyll expects your website directory to be laid out like so:

    # not correct .... XXXX FINISH THIS XXXX
    |-- _config.yml
    |-- _includes
    |-- _layouts
    |   |-- default.html
    |   |-- post.html
    |-- _posts
    |   |-- 20011-10-25-open-source-is-good.markdown
    |   |-- 20011-04-26-hello-world.markdown
    |-- _site
    |-- index.html
    |-- assets
        |-- css
            |-- style.css
        |-- javascripts

Theme
    : xxx
static
    : contains all the static assets, which will be copied to the output theme folder. I’ve put the CSS and image folders here, but they are just examples. Put what you need here.
templates
    :contains all the templates that will be used to generate the content. I’ve just put the mandatory templates here; you can define your own if it helps you keep things organized while creating your theme.

index.html
    : This is the home page of your blog, generated at output/index.html.
author.html
    : This template will be processed for each of the existing authors, with output generated at output/author/author_name.html.
category.html
    : This template will be processed for each of the existing categories, with output generated at output/category/category_name.html.
article.html
    : This template will be processed for each article, with .html files saved as output/article_name.html. Here are the specific variables it gets.
page.html
    : This template will be processed for each page, with corresponding .html files saved as output/page_name.html.
tag.html
    : This template will be processed for each tag, with corresponding .html files saved as output/tag/tag_name.html.

```
├── static
│   ├── css
│   └── images
└── templates
    ├── archives.html         // to display archives
    ├── period_archives.html  // to display time-period archives
    ├── article.html          // processed for each article
    ├── author.html           // processed for each author
    ├── authors.html          // must list all the authors
    ├── categories.html       // must list all the categories
    ├── category.html         // processed for each category
    ├── index.html            // the index. List all the articles
    ├── page.html             // processed for each page
    ├── tag.html              // processed for each tag
    └── tags.html             // must list all the tags. Can be a tag cloud.
```

```
├── AUTHORS.md
├── LICENSE
├── README.md
├── static
│   ├── css
│   │   ├── bootstrap.amelia.min.css
│   │   ├── bootstrap.cerulean.min.css
│   │   ├── bootstrap.cosmo.min.css
│   │   ├── bootstrap.cyborg.min.css
│   │   ├── bootstrap.flatly.min.css
│   │   ├── bootstrap.journal.min.css
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap.readable.min.css
│   │   ├── bootstrap.readable-old.min.css
│   │   ├── bootstrap.simplex.min.css
│   │   ├── bootstrap.slate.min.css
│   │   ├── bootstrap.spacelab.min.css
│   │   ├── bootstrap.united.min.css
│   │   ├── bootstrap.yeti.min.css
│   │   ├── font-awesome.css
│   │   ├── font-awesome.min.css
│   │   ├── html4css1.css
│   │   ├── style.css
│   │   ├── typogrify.css
│   │   ├── pygments
│   │   │   ├── autumn.css
│   │   │   ├── borland.css
│   │   │   ├── bw.css
│   │   │   ├── colorful.css
│   │   │   ├── default.css
│   │   │   ├── emacs.css
│   │   │   ├── friendly.css
│   │   │   ├── fruity.css
│   │   │   ├── manni.css
│   │   │   ├── monokai.css
│   │   │   ├── murphy.css
│   │   │   ├── native.css
│   │   │   ├── pastie.css
│   │   │   ├── perldoc.css
│   │   │   ├── solarizeddark.css
│   │   │   ├── solarizedlight.css
│   │   │   ├── tango.css
│   │   │   ├── trac.css
│   │   │   ├── vim.css
│   │   │   └── vs.css
│   ├── fonts
│   │   ├── FontAwesome.otf
│   │   ├── fontawesome-webfont.eot
│   │   ├── fontawesome-webfont.svg
│   │   ├── fontawesome-webfont.ttf
│   │   ├── fontawesome-webfont.woff
│   │   ├── glyphicons-halflings-regular.eot
│   │   ├── glyphicons-halflings-regular.svg
│   │   ├── glyphicons-halflings-regular.ttf
│   │   └── glyphicons-halflings-regular.woff
│   └── js
│       ├── bootstrap.min.js
│       ├── github.js
│       ├── jXHR.js
│       └── respond.min.js
└── templates
    ├── archives.html
    ├── article.html
    ├── author.html
    ├── authors.html
    ├── base.html
    ├── categories.html
    ├── category.html
    ├── index.html
    ├── page.html
    ├── tag.html
    ├── tags.html
    └── includes
        ├── addthis.html
        ├── article_info.html
        ├── cc-license.html
        ├── comment_count.html
        ├── comments.html
        ├── disqus_script.html
        ├── footer.html
        ├── ga.html
        ├── github.html
        ├── github-js.html
        ├── links.html
        ├── pagination.html
        ├── piwik.html
        ├── related-posts.html
        ├── sidebar.html
        ├── taglist.html
        └── translations.html
```

### Basic Workflow With Pelican
The workflow required to mange the blog is simple, fully under your control,
and very natural for anyone who is accustom to software development
since you'll be using your development tools.
It goes like this:

Launch Terminal
    : You open your favorate terminal tool and change directory to your Jekyll directory. In my case it `cd ~/myblog`.
Generate  Post
    : To create a new post in the _posts directory, you type following command
Use Your Favorite Editor
    : Launch your favorite editor to write the post. This is the best part of all.  Your using a very fimilar editor to create the post.  In my case, this is done with `vim _post/"title of the post"`.
Add Proper Front Matter
    : I have customized my Jekyll blog a lot and now it supports a lot of varibles, I’m including some variables below with some sample data, for my own reference.
Generating Post in `_site` Directory
    : To generate the post so I can inspect its formatting, I run following command in terminal
Deploying the Website
    : If you use GitHub Pages for your website, here again, you can use some very farmilar tools.  You simply need to push the code to GitHub.

#### Search Function
Check out what this Pelican web site might have used: http://terriyu.info/blog/search.html

#### Atom and RSS Feeds
Web [content syndication][40] is the process of pushing your blog, site, or
video content out into third-party sites, either as a full article, snippet, link, or thumbnail.
Two popular syndication XML-based file format are [Atom][42], which was
developed as an alternative to [RSS][41] because of its perceived shortcomings.
When you put content into RSS or Atom and send that content to other people or websites,
it's called a [feed][43].

#### Web Robots.txt and Sitemap Files
Some obsure [Pelican documentation][46] gives a bit of guidance on Web Robots and Sitemaps.
[Web Robots][45] (also known as Web Crawlers or Web Spiders),
are programs that traverse the Web automatically.
Search engines, such as Google, use them to index the web content.
Web site owners use the `robots.txt` file to give instructions about their site to web robots.
This is called The [Robots Exclusion Protocol][44].
Before a web robot visits a we bsite, it firsts checks for `robots.txt`
in the top-level directory of your web server.

I put the following in `robot.txt`:

```
User-agent: *
Disallow: /drafts/
```

The `User-agent: *` means this section applies to all robots.
The `Disallow: /draft/` tells the robot that it should not
visit any pages within the `drafts` directory.
There are also two important considerations when using `robots.txt`:

* robots can ignore your /robots.txt
* the /robots.txt file is a publicly readable file

Sitemaps are a way to inform search engines about pages on your sites that are available for crawling.
In its simplest form, a Sitemap is an XML file that lists URLs
for a site along with additional metadata about each URL
(when it was last updated, how often it usually changes, and how important it is,
relative to other URLs in the site) so that search engines can more intelligently crawl the site.

#### Setting Up Error Pages
Pelican's documentation does not provide much insight on implement we [error pages][36],
but I did fine the posting "[How to setup error pages with Pelican][37]".
This involves the creation of a `.htaccess` file in the root directory of you web site.
To better understand what this is all about, check out "[.htaccess Tutorial][38]"
and "[How to Set Up A Custom 404 File Not Found Page][39]".
I placed both htaccess and the error files in the Pelcian `content/extra` directory
and used the `pelicanconfig.py` configuration file
to move them to there proper destination for publishing
(see `EXTRA_PATH_METADATA` in the `pelicancong.py` file).

#### Setting Up Google Analytics and Disqus
* [Setup Google Analytics/Piwik and Disqus](http://terriyu.info/blog/posts/2013/07/pelican-setup/#fn:2)
* [54 Google Analytics Resources – The 2013 Edition](http://blog.kissmetrics.com/google-analytics-resources-2013/)

#### Git and GitHub Setup

```shell
git init
git config --global user.name "jeffskinnerbox"
git config --global user.email jeff.irland@verizon.net
git config --global core.editor vim
git config --global merge.tool vimdiff
git add --all
git commit -m "first commit"
git remote add origin https://github.com/jeffskinnerbox/jeffskinnerbox.github.io.git
```

#### Publishing to GitHub Page
[GitHub can create a websites from a repository][29] and this is call GitHub Pages.
There are [two types of GitHub Pages][30]: Project Pages and User Pages.
We are using User Pages here.
Check out [A guide to using Github Pages][33] for more information.

In the case of User Pages, if we create a repository with the name `<username>.github.io`,
whatever is created in the master branch of `<username>.github.io`, will be published.
The website will be the same name (you can provide a custom name, more on this below).
Therefore, for our purpose, just the output generated by Pelican needs to pushed to GitHub
to create the website.
We'll also use GitHub to version control the source for the website,
but that will be via a seperate repository.

To publish a Pelican site in the form of User Pages,
you need to push the content of the `output` directory (i.e. the HTML created for the website)
generated by Pelican to the master branch of your `<username>.github.io` repository on GitHub.
We'll use the utility `[ghp-import][31]` to make this easy.
We'll also use the `publishconf.py` Pelican configuration file,
which will import the `pelicanconf.py` file but override anything needed specifically for publishing.

```shell
pelican content -o output -s publishconf.py
ghp-import output
git push origin gh-pages:master
```

The `git push` command pushes the local `gh-pages` branch
(freshly updated by the `ghp-import` command) to the `<username>.github.io`
repository’s `master` branch on GitHub.
Using `ghp-import` will over write your local `gh-pages` branch and the remote GitHub `master` branch.
In effect, GitHub's `master` branch will maintain the website's current content, but no history.

I do want maintain a historical record of the website's source materials (i.e. the markdown files)a.
To place the source materials for the website into GitHub,
I'll use standard git procedures (i.e. no use of `ghp-import`).
See below for the procedure used:

```shell
git add --all
git commit -m "<comment>"
git push origin master:source
```

The `git push` command pushes the local `master` branch
(which contains the source materials for the website) to the `<username>.github.io`
repository’s `source` branch on GitHub.

If you're having trouble getting Github to publish your site,
go to Settings for your repository and make sure that the `master` branch is the default branch.

##### Custom Domain Name
To use a custom domain with GitHub Pages,
you need to put the domain of your site (e.g., www.jeffskinnerbox.me)
inside a `CNAME` file at the root of your site.
To do this, add the `CNAME` file to the `content/extras/`.
Then use the configuration variable `STATIC_PATHS` setting to tell Pelican
to copy this file to your output directory. For example:

```python
STATIC_PATHS = [ 'images', 'extra/CNAME' ]
EXTRA_PATH_METADATA = { 'extra/CNAME': { 'path': 'CNAME' }, }
```

#### Set Up for Your Domain Name Provider

run this command `dig www.jeffskinnerbox.me +nostats +nocomments +nocmd`
to perform a DNS lookup.

A big issue for me was my domain name and existing links. I was able to keep my 
perma-link structure the same which is nice, but I didn't want my URL changing 
to gkwelding.github.com. I'd had the in-the-attic.co.uk domain for years and years 
and had just recently managed to acquire the .com after many years of watching it 
sit idle in the hands of someone else. Github know this. they have provided a super 
easy method to let you use your own domain.

Create a CNAME file in the top level of your github repository for your site. In 
my CNAME file you will see it just contains in-the-attic.com. That's all it needs. 
Follow the advice at
[https://help.github.com/articles/setting-up-a-custom-domain-with-pages](https://help.github.com/articles/setting-up-a-custom-domain-with-pages) 
for how to set up your DNS, however, as an example mine now looks like this:

    @       A 204.232.175.78
    www     A 204.232.175.78
    www     C gkwelding.github.com

And that's it. Give your DNS time to update and away you go.

One thing about this is you can only have one TLd pointing to your Github page. 
This was a problem for me because I've used the in-the-attic.co.uk domain for years. 
All of my traffic comes through the .co.uk domain, but i now wanted to use the .com 
domain for various reasons. I'd already set up all the 301 redirects on the .co.uk 
domain and I had to piggy back on a server I ran for other clients. I pointed my .co.uk 
domain there and redirected via HTACCESS to the .com, URI string and all.

For those interested the code in the .htaccess is as follows:

    RewriteEngine On
    RewriteBase /

    RewriteCond %{HTTP_HOST} ^(www\.)?in-the-attic\.co\.uk$ [NC]
    RewriteRule ^(.*)$ http://www.in-the-attic.com/$1 [R=301,L]

#### Upgrading Packages
If you installed a stable Pelican, Markdown, or other package release via pip or easy_install
and wish to upgrade to the latest stable release,
you can do so by adding `--upgrade` to the relevant command. For Pelican, that would be:

    pip install --upgrade pelican



[01]:http://arunrocks.com/moving-blogs-to-pelican/
[02]:http://blog.getpelican.com/
[03]:http://docs.getpelican.com/en/3.3.0/getting_started.html
[04]:http://martinbrochhaus.com/pelican2.html
[05]:https://github.com/getpelican
[06]:http://jekyllrb.com/
[07]:http://hackercodex.com/guide/pelican-static-site-generator-install/
[08]:http://docs.fabfile.org/en/1.8/
[09]:http://www.linuxforu.com/2012/06/gnu-make-in-detail-for-beginners/
[10]:http://docs.getpelican.com/en/3.3.0/
[11]:http://jeffskinnerbox.wordpress.com/
[12]:https://github.com/getpelican/pelican-themes
[13]:https://github.com/getpelican/pelican-plugins
[14]:https://help.github.com/articles/fork-a-repo
[15]:http://jinja.pocoo.org/
[16]:http://docs.getpelican.com/en/3.3.0/themes.html#templates-and-variables
[17]:http://vuongnguyen.com/creating-blog-python-virtualenv-pelican.html
[18]:http://terriyu.info/blog/posts/2013/07/pelican-setup/
[19]:http://daringfireball.net/projects/markdown/
[20]:http://docutils.sourceforge.net/rst.html
[21]:http://www.methods.co.nz/asciidoc/index.html
[22]:http://pythonhosted.org/Markdown/extensions/extra.html
[23]:https://github.com/getpelican/pelican/tree/master/docs
[24]:https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
[25]:http://www.w3.org/TR/html5/
[26]:http://pelicanthemes.com/
[27]:https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
[28]:http://getbootstrap.com/
[29]:http://pages.github.com/
[30]:https://help.github.com/articles/user-organization-and-project-pages
[31]:https://pypi.python.org/pypi/ghp-import
[32]:http://docs.getpelican.com/en/3.3.0/tips.html
[33]:http://www.thinkful.com/learn/a-guide-to-using-github-pages/
[34]:http://www.onextrapixel.com/2012/11/12/how-to-use-twitter-bootstrap-to-create-a-responsive-website-design/
[35]:http://bootswatch.com/
[36]:https://en.wikipedia.org/wiki/Http_404
[37]:http://bertelsen.ca/setup/how-to-setup-error-pages-with-pelican/
[38]:http://www.freewebmasterhelp.com/tutorials/htaccess/
[39]:http://www.thesitewizard.com/archive/custom404.shtml
[40]:http://en.wikipedia.org/wiki/Web_syndication
[41]:http://en.wikipedia.org/wiki/RSS
[42]:http://atomenabled.org/
[43]:http://www.press-feed.com/howitworks/rss_tutorial.php
[44]:http://www.robotstxt.org/orig.html
[45]:http://en.wikipedia.org/wiki/Internet_bot
[46]:https://github.com/getpelican/pelican/wiki/Tips-n-Tricks#generate-sitemapxml
[47]:https://wordpress.org/
[48]:https://www.python.org/
[49]:http://www.virtualenv.org/en/latest/
[50]:http://docs.getpelican.com/en/3.2/getting_started.html#installing-pelican
[51]:https://gist.github.com/jeffskinnerbox/9612119
[52]:
[53]:
[54]:
[55]:
[56]:
[57]:
[58]:
[59]:
[60]: