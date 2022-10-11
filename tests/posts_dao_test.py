import pytest
from app.posts.dao.posts_dao import PostsDAO
from config import POSTS_DATA_PATH

@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO(POSTS_DATA_PATH)
    return posts_dao_instance

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

class TestPostsDAO:

    def test_get_all(self, posts_dao):
        """  Проверяет получаем ли список кандидатов"""
        posts = posts_dao.get_all()
        assert type(posts) == list, "Возвращает не список"
        assert len(posts) == 8
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"


    def test_get_by_pk(self, posts_dao):
        """ Проверяет, как работает получение поста по pk """
        posts = posts_dao.get_by_pk(1)
        assert posts['pk'] ==1, "Возвращается неверный пост"


    def test_get_by_user(self, posts_dao):
        """ Проверяет, как работает получение поста по used_id """
        posts = posts_dao.get_by_user("Leo")
        assert posts['pk'] in [1,5], "Возвращаются неверные посты по пользователю"





