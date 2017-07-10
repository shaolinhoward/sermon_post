#!/usr/bin/python
# Adds an entry to the Hoc 4 blog via WordPress

import datetime
import sys
import utils

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetRecentPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

today = datetime.date.today()

# read centrally defined var vals
sermon_vars = utils.read_msg_bundle('/home/howard/git_repos/sermon_post/sermon_vars')

p_title = today.strftime('%b %d, %Y Sermon')
p_description = sys.argv[1]
p_description = p_description.replace("_", " ")
print p_description
p_format = sermon_vars['post_format']
p_categories = sermon_vars['post_categories']
p_category_id = sermon_vars['post_category_id']
p_tags = sermon_vars['post_tags']

rpc_url = sermon_vars['wp_rpc_url']
username = sermon_vars['wp_username']
password =  sermon_vars['wp_password']

wp = Client(rpc_url, username, password)

post = WordPressPost()
post.title = p_title
post.description = p_description
post.format = p_format
post.categories = p_categories
#post.terms = post_category_name
post.tags = p_tags

print post.title + ": " + post.description + " [posted]"
post_id = wp.call(NewPost(post, True))

#podpress: https://wordpress.org/support/topic/xml-rpc-support-1
file_prefix = today.strftime('Hoc4Service%y%b%d_')
sermon_file = file_prefix + 'sermon' + '.mp3'
file_url = today.strftime('http://hoctoga.org/english/recordings/%Y/' + sermon_file)

print file_url

fields = {}
fields["URI"] = file_url
fields["title"] = p_title
fields["type"] =  sermon_vars['file_type']
fields["rss"] = "on"
fields["atom"] = "on"
xmlContent = [fields]
params = [post_id, xmlContent]
print params
wp.execute("podPress.addNewXmlrpcPost", params);

#Then data can be added by just calling RPclient.execute("podPress.addNewXmlrpcPost", params); on the client where params is an array: [int PostID, Hashtable xmlContent] and xmlContent has the structure that you have shown above.
