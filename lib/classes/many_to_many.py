class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
           raise ValueError("Error: Author must be type of Author.")
        elif not isinstance(magazine, Magazine):
            raise ValueError("Error: Magazine must be type of Magazine.")
        elif not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Error: Title must be a string between 5 and 50 length.")
        else:
            self._title = title
            self.author = author
            self.magazine = magazine
            Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            print("Error: Title is immutable once set.")
        elif not isinstance(value, str) or not (5 <= len(value) <= 50):
            print("Error: Title must be a string between 5 and 50 characters.")
        else:
            self._title = value




class Author:
    
    def __init__(self, name):
        if isinstance(name, str) or len(name) == 0:
            self._name = name
        else:
            print("Error: Name must be a string and of length more or equal to one")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        print("Error: Author name is immutable upon being set.")

    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if self.magazines():
            
            return list({magazine.category for magazine in self.magazines()})
        return None




class Magazine:

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            print("Error: Name must be a string between 2 and 16 length .")
        elif not isinstance(category, str) or len(category) == 0:
            print("Error: Category must be a string and be of more than zero length.")
        else:
            self._name = name
            self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            print("Error: Name must be a string between 2 and 16 characters.")
        else:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print("Error: Category must be a non-empty string.")
        else:
            self._category = value

    

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None