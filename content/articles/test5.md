Title: Testing: Python Markdown Extensions
Date: 2100-01-01 00:00
Category: Testing
Slug: testing-python-markdown-extensions
Author: Jeff Irland
Image: DRAFT_stamp.svg
Summary: This page is for testing purposes only.
Status: draft

## The Back Story

A compilation of test for the various [Python-Markdown extensions][01] found in Pyhton's version of Markdown.
http://pythonhosted.org/Markdown/extensions/extra.html

To support Latex, you need to enable the [latex plugin][02].

For a deonstration, see
http://terriyu.info/blog/posts/2013/06/pelican-demo/#fn:2

## Latex Math

$$
\begin{align*}
  & \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
  & (x_1, \ldots, x_n) \left( \begin{array}{ccc}
      \phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
      \vdots & \ddots & \vdots \\
      \phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
    \end{array} \right)
  \left( \begin{array}{c}
      y_1 \\
      \vdots \\
      y_n
    \end{array} \right)
\end{align*}
$$


[01]:http://pythonhosted.org/Markdown/extensions/extra.html
[02]:https://github.com/getpelican/pelican-plugins/blob/master/latex
