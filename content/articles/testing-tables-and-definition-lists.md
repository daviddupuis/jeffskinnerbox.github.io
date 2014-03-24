Title: Testing: Tables and Definition Lists
Date: 2100-01-01 00:00
Category: Testing
Slug: testing-tables-and-definition-lists
Author: Jeff Irland
Image: DRAFT_stamp.svg
Summary: This page is for testing purposes only.
Status: draft

## The Back Story
Out of the box, the table formating of Python Markdown sucks!
It has no borders, no header formating, no padding in cells, etc.
This can be fixed with a little custom CSS.
My fix is in `content/extra/custom.css` and is listed blow:

```
/* This will provide some visual improvements to Markdown's formatted tables */
table, th, td {
    margin-left: auto; 
    margin-right: auto;
    border: 1px solid black;
}

th {
    padding-top: 5px;
    padding-bottom: 5px;
    padding-right: 15px;
    padding-left: 15px;
    background-color: #B8B8B8;
    color: black;
}

td {
    padding-top: 5px;
    padding-bottom: 5px;
    padding-right: 15px;
    padding-left: 15px;
    background-color: #FFFFFF;
    color: black;
}
```

## Tables
Tables aren't part of the core Markdown spec, but are part of Python / Pelican
implementation.
This posting gives you some idea on how [tables should be supported][01]
and see the [Python Table extension][02].
You combine this, with the `custom.css` discussed above, and you can get the following:

| Default Justified | Left Justified | Right Justified | Centered Justified |
| ----------------- |:-------------- | ---------------:|:------------------:|
| row 1, col 1 | row 1, col 2     | row 1, col 3 | _this should be italics_   |
| row 2, col 1 | **this should be bold** | row 2, col 3 | row 2, col 4     |
| row 3, col 1 | row 3, col 2     | $\frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac25 \pi}}$ | row 3, col 4     |
| `this should be code` | row 4, col 2     | row 4, col 3 | row 4, col 4     |
| row 5, col 1 | row 5, col 2     | row 5, col 3 | row 5, col 4     |o

Test of inline MathJax: $\frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac25 \pi}}$

## Definition Lists
The [Definition Lists][03] extension adds the ability to create definition lists in Markdown documents.
For example, here are defintions of two fruits:
 
Apple
:   Pomaceous fruit of plants of the genus Malus in 
    the family Rosaceae.

Orange
:   The fruit of an evergreen tree of the genus Citrus.

You can also add multiple definitions (if you add some spacing between items):

Apple
:   Pomaceous fruit of plants of the genus Malus in 
    the family Rosaceae.
:   An American computer company.

Orange
:    The fruit of an evergreen tree of the genus Citrus.



[01]:http://stackoverflow.com/questions/16099153/table-not-render-when-use-redcarpet-in-jekyll-github-pages
[02]:http://pythonhosted.org//Markdown/extensions/tables.html
[03]:http://pythonhosted.org/Markdown/extensions/definition_lists.html
[04]:
[05]:
[06]:
[07]:
[08]:
