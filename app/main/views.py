from . import main
from flask import render_template
from app import app
from flask_login import login_required, current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import User, Pitch, Comment, Role, Upvote, Downvote
from .forms import ReviewForm,UpdateProfile,CommentForm
from .. import db, photos
import markdown2



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitches'
    pitches = Pitch.query.all()
    users = User.query.all()
    pickuplines = Pitch.query.filter_by(category = 'Pick-up Lines').all()
    interview = Pitch.query.filter_by(category = 'Interview').all()
    product = Pitch.query.filter_by(category = 'Product').all()
    promotion = Pitch.query.filter_by(category = 'Promotion').all()
    music = Pitch.query.filter_by(category = 'Music').all()
    sports = Pitch.query.filter_by(category = 'Sports').all()

    return render_template('index.html',title = title,pitches = pitches,pickuplines=pickuplines,interview=interview,product=product,promotion=promotion,music=music,sports=sports,users=users)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/comment/<int:pitch_id>')
@login_required
def single_comment(id):
    comment = Pitch.query.get(id)
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.pitch_comment,extras=["code-friendly","fenced-code blocks"])
    return render_template('comment.html',comment = comment,format_comment = format_comment)


@main.route('/comment/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        # Updated comment instance
        new_comment= Comment(title=title,pitch_comment=comment,user_id=user_id,pitch_id=pitch_id)

        # save review method
        new_comment.save_comment()
        return redirect(url_for('.new_comment',pitch_id = pitch_id))
    return render_template('new_comment.html',pitch=pitch,all_comments=all_comments,comment_form=form)