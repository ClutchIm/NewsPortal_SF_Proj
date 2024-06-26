from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    a_rating = models.IntegerField(default=0)

    def update_rating(self):
        p_rating = self.post_set.aggregate(postRating=Sum('p_rating'))
        p_rat = 0
        p_rat += p_rating.get('postRating')

        c_rating = self.author.comment_set.aggregate(commentRating=Sum('c_rating'))
        c_rat = 0
        c_rat += c_rating.get('commentRating')

        self.a_rating = p_rat * 3 + c_rat
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=255,
                                unique=True)

    def __str__(self):
        return f'{self.category}'


class Post(models.Model):
    article = 'AR'
    news = 'NE'

    CHOOSE = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    p_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=2,
                             choices=CHOOSE,
                             default=news)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=150)
    main_text = models.TextField()
    p_rating = models.IntegerField(default=0)

    def like(self):
        self.p_rating += 1
        self.save()

    def dislike(self):
        self.p_rating -= 1
        self.save()

    def preview(self):
        return self.main_text[:124]+'...'

    def __str__(self):
        return f'{self.title.title()}: {self.preview()}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
    c_rating = models.IntegerField(default=0)

    def like(self):
        self.c_rating += 1
        self.save()

    def dislike(self):
        self.c_rating -= 1
        self.save()
