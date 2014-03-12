Title: Testing: Tag Cloud
Date: 2100-01-01 00:00
Category: Testing
Slug: testing-tag-cloud
Author: Jeff Irland
Image: DRAFT_stamp.svg
Summary: This page is for testing purposes only.
Status: draft

## The Back Story

To sort tags in alphabetical order, use

```
{% for tag, articles in tags|sort %}
```

```
<ul class="tagcloud">
    {% for tag in tag_cloud %}
        <li class="tag-{{ tag.1 }}"><a href="{{ SITEURL }}/{{ tag.0.url }}">{{ tag.0 }}</a></li>
    {% endfor %}
</ul>
```
