Title: Testing: Tables and Definition Lists
Date: 2100-01-01 00:00
Category: Testing
Slug: testing-tables-and-definition-lists
Author: Jeff Irland
Image: DRAFT_stamp.svg
Summary: This page is for testing purposes only.
Status: draft

## The Back Story

## Tables
Tables aren't part of the core Markdown spec, but are by Pyhton / Pelican.
This posting gives you some idea on how [tables should be supported][01]
and see the [Python Table extension][02].  For example:

| Default Justified | Left Justified | Right Justified | Centered Justified |
| ----------------- |:-------------- | ---------------:|:------------------:|
| row 1, col 1 | row 1, col 2     | row 1, col 3 | _this should be italics_   |
| row 2, col 1 | **this Should be bold** | row 2, col 3 | row 2, col 4     |
| row 3, col 1 | row 3, col 2     | row 3, col 3 | row 3, col 4     |
| `this should be code` | row 4, col 2     | row 4, col 3 | row 4, col 4     |
| row 5, col 1 | row 5, col 2     | row 5, col 3 | row 5, col 4     |

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
