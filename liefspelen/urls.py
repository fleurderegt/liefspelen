from django.conf.urls import url

from . import views


app_name = 'liefspelen'
urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /games/5/
    url(r'^(?P<game_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<game_id>[0-9]+)/recipe$', views.recipe, name='recipe'),
    url(r'^(?P<game_id>[0-9]+)/worksheet$', views.worksheet, name='worksheet'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^suggestion$', views.suggestion, name='suggestion'),
    url(r'^buiten$', views.buiten, name='buiten'),
    url(r'^binnen$', views.binnen, name='binnen'),
    url(r'^tuin$', views.tuin, name='tuin'),
    url(r'^bos$', views.bos, name='bos'),
    url(r'^strand$', views.strand, name='strand'),
    url(r'^schoolplein$', views.schoolplein, name='schoolplein'),
    url(r'^zwembad$', views.zwembad, name='zwembad'),
    url(r'^koken$', views.koken, name='koken'),
    url(r'^spelletjes$', views.spelletjes, name='spelletjes'),
    url(r'^knutselen$', views.knutselen, name='knutselen'),
    url(r'^gym_ideetjes$', views.gym_ideetjes, name='gym_ideetjes'),
    url(r'^handwerken$', views.handwerken, name='handwerken'),
    url(r'^werkbladen$', views.werkbladen, name='werkbladen'),
    ]