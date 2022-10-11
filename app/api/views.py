from flask import Blueprint, jsonify

from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO
from config import POSTS_DATA_PATH, COMMENTS_DATA_PATH

api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao = PostsDAO(POSTS_DATA_PATH)
comments_dao = CommentsDAO(COMMENTS_DATA_PATH)

@api_blueprint.route('/api/posts/')
def posts_api():
    posts = posts_dao.get_all()
    return jsonify(posts), 200


@api_blueprint.route('/api/posts/<int:post_id>')
def single_post_api(post_id):
    post = posts_dao.get_by_pk(post_id)
    return jsonify(post), 200
