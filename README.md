## Wordpress to Staticman Comments

The original script was written by [Dan](https://github.com/dancwilliams/wordpress_to_staticman_comments) as a quick-fix for his usage. I don't know if he intended for anyone else to use it eventually. I ended up modifying his script quite a lot to suit my own needs while moving from Wordpress to Hugo. Needless to say, the script is still rough and I modified it just enough so that my own use-cases were being catered to. I am hopeful that it will work fine for you too but try it at your own risk. Or maybe you can fork this and add the functionality you want and open up a PR? :smile:

### Requirements

- Python 3
- `xmltodict` (`pip install xmltodict`)

### Run

- Rename your wordpress xml dump file to `big_data.xml` and put it in the same folder as this script. 
- Create a `comments` folder in the same folder as this script.
- Run `python wordpress_to_staticman.py`

In the end just copy the `comments` folder to the `data` folder in the base directory of your Hugo source files. 

### Nested replies

If you don't already have nested comments functionality working in your Staticman installation, you can follow [this](https://yasoob.me/posts/running_staticman_on_static_hugo_blog_with_nested_comments/) tutorial to set that up. The output of this script will also work with nested replies!
