from django.conf.urls.defaults import *
# from ct_blog.views import blog_new_site_post

urlpatterns = patterns('ct_blog.views',
    url(r'^$', view='index', name='blog_index'),
    url(r'^(?P<object_id>[-\d]+)/$', view='detail', name='post'),
    url(r'^(?P<object_id>[-\d]+)/comment/(?P<comment_id>[-\d]+)/delete/$', view='post_comment_delete', name='post-comment-delete'),
    url(r'^new-post/', view='blog_new_site_post', name='blog-new-site-post'),
    url(r'^(?P<object_id>[-\d]+)/edit/$', view='blog_edit_site_post', name='blog-edit-site-post'),

    # url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
    #     view='post_detail',
    #     name='blog_detail'
    # ),
    # url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
    #     view='post_archive_day',
    #     name='blog_archive_day'
    # ),
    # url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
    #     view='post_archive_month',
    #     name='blog_archive_month'
    # ),
    # url(r'^(?P<year>\d{4})/$',
    #     view='post_archive_year',
    #     name='blog_archive_year'
    # ),
    # url(r'^categories/(?P<slug>[-\w]+)/$',
    #     view='category_detail',
    #     name='blog_category_detail'
    # ),
    # url (r'^categories/$',
    #     view='category_list',
    #     name='blog_category_list'
    # ),
    # url(r'^tags/(?P<slug>[-\w]+)/$',
    #     view='tag_detail',
    #     name='blog_tag_detail'
    # ),
    # url (r'^search/$',
    #     view='search',
    #     name='blog_search'
    # ),
    # url(r'^page/(?P<page>\d+)/$',
    #     view='post_list',
    #     name='blog_index_paginated'
    # ),
)
