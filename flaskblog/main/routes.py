from flask import Blueprint, render_template, request, flash
from flaskblog.models import Post, Comment

main = Blueprint('main', __name__)


@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    comments = Comment.query.order_by(Comment.id).paginate(page=1, per_page=5000)
    return render_template('home.html', posts=posts, comments=comments)


@main.route("/")
@main.route("/about")
def about():
    return render_template('about.html', title='About')
    