from flask import Blueprint, render_template, url_for, flash, redirect, request, abort, jsonify
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, Comment
from flaskblog.comments.forms import CommentForm
from flaskblog.users.utils import save_picture

comments = Blueprint('comments', __name__)

@comments.route("/post/<int:post_id>/comment", methods=['GET', 'POST'])
@login_required
def new_comment(post_id):
    post = Post.query.get_or_404(post_id)
    user = current_user
    form = CommentForm()
    if form.validate_on_submit():
        if form.picture.data:
            medium = save_picture(form.picture.data)
            comment = Comment(content=form.content.data, commentor=user, post=post, medium=medium)
        else:
            comment = Comment(content=form.content.data, commentor=user, post=post)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been submitted!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_comment.html', title='New Comment', form=form, post=post)

# @comments.route("/post/<int:post_id>/comment/like", methods=['GET', 'POST'])
# def like(post_id):
#     post = Post.query.get_or_404(post_id)
#     post.likes += 1
#     db.session.commit()
#     return redirect(url_for('posts.post', post_id=post.id))

@comments.route("/post/like", methods=['POST'])
def like():
    post_id = request.form['post_id']
    post = Post.query.get_or_404(post_id)
    post.likes += 1
    db.session.commit()
    return jsonify({'nOfLikes' : post.likes, 'post_id' : post.id})