''' Commands to run python shell and interact with backend / database '''

# first run command python3 manage.py shell
from academia.models import Post
from django.contrib.auth.models import User

User.objects.all()  # returns all users

# for first user
User.objects.first()

# to filter resutls
User.objects.filter(username='arlindstafaj')

# returns just object not query set
User.objects.filter(username='arlindstafaj').first()

user = User.objects.filter(username='arlindstafaj').first()
user.id  # same as .pk
user.pk  # primary key
user = User.objects.get(id=1)  # returns same as .first
# Creating a new post and make this user author of new Post
Post.objects.all()  # No QuerySet because no posts
post_1 = Post(title='Blog 1', content='First Post Content', author=user)
post_1.save()  # saves to db
Post.objects.all()  # returns: <QuerySet [Post: Post object (1)]>
# By updating Post class with :
''' def __str__(self):
        return self.title'''
Post.objects.all()  # returns: <QuerySet [Post: Post Blog 1]>

user = User.objects.filter(username='arlindstafaj').first()
post_2 = Post(title='Blog 2', content='Second post content', author_id=user.id)
post_2.save()

Post.objects.all()  # returns: <QuerySet [<Post: Post Blog 1>, <Post: Blog 2>]>

post = Post.objects.first()
post.content  # prints 'First post content'
post.author  # prints <User: arlindstafaj>
post.author.email  # prints email of user

# Get all posts written by a specific user
# .modelset_set = query set to user model - naming convention

user.post_set.all()  # return: <QuerySet [<Post: Post Blog 1>, <Post: Blog 2>]>
# To create third post, author not needed to be specified and no need to save
user.post_set.create(title='Blog 3', content='Third post content')
