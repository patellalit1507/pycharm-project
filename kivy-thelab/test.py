blog_1="i am"
blog_2="so "
blog_3="serious"
def blog_post(*args):
    for post in args:
        print(post)

blog_post(blog_1,blog_2,blog_3)