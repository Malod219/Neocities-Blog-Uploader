# Neocities-Blog-Uploader
A blog uploader for blogs on Neocities See it in action here: https://risingthumb.xyz/blog.html
## Installation
To install this, you will need to make a clone of the repository, save it somewhere and extract it.

You will need Python3.6, get that here https://www.python.org/

You will need python-neocities, get that here https://github.com/neocities/python-neocities

You will need FeedGenerator, Get that from Pip using this command `pip install feedgen`

You will need HTMLParser, Get that from Pip using this command `pip install HTMLParser`

## Use
Blogtext contains all the text files for all your blogs. You name them in numerical order from 1.txt to N.txt where N is the number of blogs texts. You cannot have a missing file in the middle. The text file contains very simple HTML, consisting of tags you would see in the body usin `<h1>` or `<p>` tags. You can even use classes or ids to use specialised CSS if you wish.

BlogUtility contains all the utility .html files. In it you will find `blogHubEmpty.html`. This contains is structured as a normal HTML file, though where you want to have the list of links to your blog posts, is where the comment `<!--PointInsertion>` is.

`blogHead.html` serves as the heading html for everything before the blog text. `blogtail.html` is for the tail of blog text. These are just concatenated onto the the text accordingly.

`blogOutput.html` serves as where everything will be output.

Your blogs will be put into a top-level folder from the root called `blogs`. The blog.html where your blogs are linked will be put in a the root folder of your website. The RSS feed for the blog is also available on the root folder of the website under the name blog.rss

## Configuration
The configuration lets you modify the directory to use for blogtext, blogoutput, the bloghead.html, blogtail.html, blogHubEmpty.html and blog.html locations. The RSS feed informations are important for setting your RSS feed up correctly. the RSS Item information is important if you want the items linked correctly. The login information is important to be able to use the Neocities API.

## Contribution
Feel free to contribute to the repo. I can do code review and pull your changes if they are good.

## License
This software is given to you under the MIT License. Basically put, do what you want with it, but I'm not responsible if anything goes wrong.
