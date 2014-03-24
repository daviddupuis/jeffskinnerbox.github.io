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
{% for tag in tag_cloud|sort) %}
    <button type="button" class="btn btn-primary btn-xs">
    <a class="tag-{{ tag.1 }}" href="{{ SITEURL }}/{{ tag.0.url }}">
        {{ tag.0 }}
    </a>
    </button>
    {% if not loop.last %}
        &nbsp;
    {% endif %}
{% endfor %}
```

{% for tag in tag_cloud|sort) %}
    <button type="button" class="btn btn-primary btn-xs">
    <a class="tag-{{ tag.1 }}" href="{{ SITEURL }}/{{ tag.0.url }}">
        {{ tag.0 }}
    </a>
    </button>
    {% if not loop.last %}
        &nbsp;
    {% endif %}
{% endfor %}

To sort by number of articles in tag

```
{% for tag in tag_cloud|sort(attribute='1') %}
    <button type="button" class="btn btn-primary btn-xs">
    <a class="tag-{{ tag.1 }}" href="{{ SITEURL }}/{{ tag.0.url }}">
        {{ tag.0 }}
    </a>
    </button>
    {% if not loop.last %}
        &nbsp;
    {% endif %}
{% endfor %}
```

{% for tag in tag_cloud|sort(attribute='1') %}
    <button type="button" class="btn btn-primary btn-xs">
    <a class="tag-{{ tag.1 }}" href="{{ SITEURL }}/{{ tag.0.url }}">
        {{ tag.0 }}
    </a>
    </button>
    {% if not loop.last %}
        &nbsp;
    {% endif %}
{% endfor %}

