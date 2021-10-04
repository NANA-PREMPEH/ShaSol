from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    #displays the posts saved in the database at the home page always
    page = request.args.get('page', 1, type=int)
    #paginate is the number of page to display on the web page
    #post.date_posted.desc is the arrangement for the post on th page
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
