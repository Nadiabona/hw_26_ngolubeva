import pytest

class TestCommentsDAO:

    def test_get_comments_all_type(self, comments_dao):
        """ Все комментарии: Тестируем тип и количество """
        comments = comments_dao.load_comments()
        assert type(comments) == list, "Не получается список комментариев"
        assert len(comments) == 20

    def test_get_comments_all_output(self, comments_dao):
        """ Тестируем структуру комментариев"""
        comments = comments_dao.load_comments()
        first_comment = comments[0]
        keys_correct = {"post_id", "commenter_name", "comment", "pk"}
        first_comment_keys = set(first_comment.keys())
        assert first_comment_keys == keys_correct, "Неравильные ключи"


    def test_get_comments_by_post_ID_check_type(self, comments_dao):
        """ Тестируем получение комментариев к посту"""
        comments_for_post = comments_dao.get_comments_by_post_id(1)
        assert type(comments_for_post) == list, "Комментарии должны быть списком"

    def test_get_comments_by_post_ID_correct(self, comments_dao, post_id):
        """ Тестируем  комментарию к каждому посту """
        comments_for_post = comments_dao.get_comments_by_post_id(post_id)
        for comment in comments_for_post:
            assert comment["post_id"] == post_id
