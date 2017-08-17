from django.db import models

class Category(models.Model):
	cat_name = models.CharField(max_length=100)
	cat_desc = models.TextField()
	def __str__(self):
		return self.cat_name

class Tag(models.Model):
	tag_name = models.CharField(max_length=100)
	tag_desc = models.TextField()
	def __str__(self):
		return self.tag_name

class Season(models.Model):
	season_name = models.CharField(max_length=100)
	season_desc = models.TextField()
	def __str__(self):
		return self.season_name

class Environment(models.Model):
	env_name = models.CharField(max_length=100)
	env_desc = models.TextField()
	def __str__(self):
		return self.env_name

class Material(models.Model):
	mat_name = models.CharField(max_length=100)
	mat_desc = models.TextField()
	def __str__(self):
		return self.mat_name

class Game(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    seasons = models.ManyToManyField(Season)
    environments = models.ManyToManyField(Environment)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    materials = models.ManyToManyField(Material)
    image = models.ImageField(default="../static/images/spelen.png")
    
    def __str__(self):
    	return self.title
    
    def steps_as_list(self):
        return self.text.split('\n')





