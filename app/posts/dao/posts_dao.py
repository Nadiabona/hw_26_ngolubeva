import json

class PostsDAO:

    def __init__(self, path):
        self.path = path

    def get_all(self):
        """
        возвращает все посты ленты
        """
        with open(f"{self.path}", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def get_by_user(self, user_name):
        """
        получает посты по имени пользователя и обрабатывает ошибку имени пользрвателя
        """
        posts = self.get_all()
        if user_name not in [post['poster_name'] for post in posts]:
            raise ValueError
        else:
            posts_by_user = [post for post in posts if post["poster_name"] == user_name]

        return posts_by_user

    def search(self, query):
        """
        получает посты по вхождению слова (query)
        """
        if query == "":
            print ("Введите слово для поиска")
        else:
            posts = self.get_all()

            posts_matched = []
            query_lower = query.lower()
            count = 0

            for post in posts:
                if query_lower in post["content"].lower():
                    posts_matched.append(post)
                    count+=1
                    if count == 10:
                        break

        return posts_matched

    def get_by_pk(self, pk):
        """
        возвращает пост по pk
        """
        posts = self.get_all()

        for post in posts:
            if post['pk'] == pk:
                return post

