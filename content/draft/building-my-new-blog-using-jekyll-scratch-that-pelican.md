Title: Building My New Blog Using Jekyll...Scratch That...Pelican
Date: 2014-02-21 18:20
Category: Blogging
Tags: Jekyll, Pelican, Blog, Bootstrap
Slug: building-my-new-blog-using-jekyll-scratch-that-pelican
Author: Jeff Irland
Summary: This Jekyll introduction outlines specifically how I set up my Jekyll blog, as well as, explains how Jekyll does what it does.

* [Migrating from Octopress to Pelican](http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/)

* Disquis
    * [Jekyll Installation Instructions](http://help.disqus.com/customer/portal/articles/472138-jekyll-installation-instructions)
    * [How I Built This Blog: Jekyll + Disqus](http://erictang.org/blog/2012/01/21/how-I-built-this-blog%3A-jekyll-%2B-disqus/)
    * [Migrate Custom Blog to Jekyll and Disqus](http://blog.huangzhimin.com/2011/01/20/migrate-custom-blog-to-jekyll-and-disqus/)
* [Learning Jekyll By Example](https://learn.andrewmunsell.com/learn/jekyll-by-example)
* [Building a blog using Jekyll, Bootstrap and Github pages. A beginners guide!](http://in-the-attic.com/2013/01/04/building-a-blog-using-jekyll-bootstrap-and-github-pages-a-beginners-guide/)
* [How I built my blog in one day](http://erjjones.github.io/blog/How-I-built-my-blog-in-one-day/)
* [Part two on how I built my blog](http://erjjones.github.io/blog/Part-two-how-I-built-my-blog/)
* [Migrating from WordPress to Jekyll – Part 1: Why I gave up on WordPress](http://vitobotta.com/migrating-from-wordpress-to-jekyll-part-one-why-i-gave-up-on-wordpress/#sthash.1ysfNdU6.dpbs)
* [Migrating from WordPress to Jekyll – Part 2: **Everything** you need to know about Jekyll](http://vitobotta.com/how-to-migrate-from-wordpress-to-jekyll/#converting-to-markdown)
* [Zero to Hosted Jekyll Blog in 3 Minutes](http://jekyllbootstrap.com/)
* [Building Sites with Jekyll](http://www.spintoapp.com/documentation/building_websites_with_jekyll#pre-processors)
* [Blogging With Jekyll Quickstart](http://hellarobots.com/2012/01/06/blogging-with-jekyll-quickstart.html)
* [Getting Started with Jekyll Plugins](http://tech.pro/tutorial/1299/getting-started-with-jekyll-plugins)

* [How to use Twitter Bootstrap to Create a Responsive Website Design](http://www.onextrapixel.com/2012/11/12/how-to-use-twitter-bootstrap-to-create-a-responsive-website-design/)
* [Twitter Bootstrap Tutorial](http://www.w3resource.com/twitter-bootstrap/tutorial.php.)
* [Customizing Bootstrap](http://coding.smashingmagazine.com/2013/03/12/customizing-bootstrap/)
* [Twitter Bootstrap 101: Introduction](http://webdesign.tutsplus.com/tutorials/complete-websites/twitter-bootstrap-101-introduction/)
* [Customizing Bootstrap](http://coding.smashingmagazine.com/2013/03/12/customizing-bootstrap/)
* [Introducing Bootswatch](http://thomaspark.me/2012/02/introducing-bootswatch/)

* [User, Organization, and Project Pages](https://help.github.com/articles/user-organization-and-project-pages)
*[Setting up a custom domain with Pages](https://help.github.com/articles/setting-up-a-custom-domain-with-pages)
* [Publishing to GitHub](http://docs.getpelican.com/en/3.0/tips.html)
* [GitHub-pages-like publishing](http://www.hackzine.org/github-pages-like-publishing.html)

* Site Search
    * [http://alexpearce.me/2012/04/simple-jekyll-searching/](http://alexpearce.me/2012/04/simple-jekyll-searching/)
    * [http://developmentseed.org/blog/2011/09/09/jekyll-github-pages/](http://developmentseed.org/blog/2011/09/09/jekyll-github-pages/)

* [The Web Robots Pages](http://www.robotstxt.org/)
* [What are Sitemaps?](http://www.sitemaps.org/)
* [Generating a sitemap.xml in Pelican](https://github.com/getpelican/pelican/wiki/Tips-n-Tricks#wiki-generate-sitemapxml)
*
* [How to setup error pages with Pelican](http://bertelsen.ca/setup/how-to-setup-error-pages-with-pelican/)
* [.htaccess Tutorial](http://www.freewebmasterhelp.com/tutorials/htaccess/)

# Pelican
My orginal plan was to port [my WordPress blog][11] to GitHub and use [Jekyll][06].
I did this, and I used it for several months, but felt less and less satisfied with my choose.
I then read the post "[Moving Blogs to Pelican][01]" and I resounated with nearly ever word.
As a result, I have now change my direction, and ported my blog from Jekyll to [Pelican][10].
Like Jekyll, Pelican is a static site generator requiring no database or server-side logic,
but it makes use of Python, Make, and Shell, not Ruby.
This was an important factor, I never had a need to use Ruby and why should my blog force the issue?

The [Pelican Development Blog][02] will provide the detail documentation needed
but to get started I followed the advice of the [Tutorial: Generating Static Sites with Pelican][07],
[Pelican Getting Started Guide][03], and [Pelican and Github Pages][04] very useful.
Also, reading [Creating a Blog with Python Pelican][17] and [How I setup Pelican][18] prove very helpful.
You can find the latest Pelican code, along with its [themes and plugins on GitHub][05].
You might find more information on [Pelican's GetHub][23] and [Pelican's Tips & Tricks][24].

##### Contents of Pelican Blog
The contents of a Pelican  blog is either a post (in Pelican terminalogy, an article) or a page.
The raw, unprocessed content is contained (pages, articles, drafts, images, etc.) in a directory called `content`.
Both articles and pages are be written in
[Markdown][19], [reStructuredText][20], [AsciiDoc][21], or even raw [HTML][25].
markdown, textile, or HTML and may also contain Liquid templating syntax.
Both articles and pages can have meta-data at the top of the document containing things like such as
title, publication date, tags, etc. and even arbitrary custom meta-data.

The processed, ready to be published materials are contained in a directory called `output`.
It is this directory that will be pushed to your web server.
Their are other things that make up a Pelican blog, such as plugins, themes, make files, and other publishing tools.
More on this later.

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

##### Create a virtualenv
To assure I have a clean Python envirnment to work in and it doesn't conflict with other Python work,
create a virtual environment for your Project.

```shell
cd ~
virtualenv --python python2.7 --no-site-packages blogging
cd blogging
source bin/activate
pip install Pelican==3.3
pip install Markdown
pip install typogrify
pip install ghp-import
```

#### Quickstart Pelican
Pelican now comes with a quickstart command that will create a skeleton directory structure for your project.
When running the command will ask you a series of questions.

    pelican-quickstart

At this point, running the command `pelican -s pelican.conf.py` in the `blogging`
directory would generate all static files for the blog using the
default theme `notmyidea` into the `output/` directory.
You can no serve this directory as you would any other static html files.
You can test this out by doing the following:

    make html
    make serve

Then using a browser, enter `localhost:8000`.
Nothing much will be there since not content has been created but you see the shell for
your `notmyidea` themed blog.

#### Fork & Clone Pelican Themes and Plugins
I wanted to leverage the official [Pelican themes][12] and [Pelican plugins][13],
and have them under version control, so I performed the standard procedure of [forking/cloning the GitHub][14].
First step is to fork these repositories on GitHub then do the following:

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
Do the `git init` and create a `.gitignore` file:

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
I have posted a final and more complete version of `.gitignore` on Gist. XXXX FINISH THIS XXXX

#### Pelican Configuration File
Pelican is configurable via setting is a Python module called `pelicanconf.py`.
The settings you define in this configuration file will be used within templates that are part of the themes.
The basic idea is that Pelican will be using the template files in your
`pelican-themes/<theme>/templates/` directory to generate all static html files.
Pelican uses [Jinja][15] for its templating language.
In these templates, you should have access to all variables from `pelicanconf.py`
as well as template-specific variables (See “[Template and Variables][16]”
section of the Pelican documentation).

My `pelicanconf.py` file looks like this:

    must add pelicanconf.py here  XXXX FINISH THIS XXXX


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
and are used for content that does not change very often (e.g., “About” page).
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
you chose during the pelican-quickstart questionnaire. For this example, we’ll use rsync over ssh:

    make rsync_upload

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
a front-end framework for developing responsive web sites.

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

#### Setup Google Analytics and Disqus
http://terriyu.info/blog/posts/2013/07/pelican-setup/#fn:2

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
you need to push the content of the `output` directory generated by Pelican
to the master branch of your `<username>.github.io` repository on GitHub.
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
repository’s master branch on GitHub.

To place the source materials for the websit into GitHub, do the following:

```shell
```

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

#### Set Up for Your Name provider
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
[34]:
[35]:
[36]:
[37]:
[38]:
[39]:
[40]:
