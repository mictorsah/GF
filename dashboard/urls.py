from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('pricing', views.pricing, name='pricing'),
    path('blog-post', views.blog_post, name='blog-post'),
    path('blog-home-1', views.blog_home_1, name='blog-home-1'),
    path('blog-home-2', views.blog_home_2, name='blog-home-2'),
    path('portfolio-item', views.portfolio_item, name='portfolio-item'),
    path('portfolio-1-col', views.portfolio_1_col, name='portfolio-1-col'),
    path('portfolio-2-col', views.portfolio_2_col, name='portfolio-2-col'),
    path('portfolio-3-col', views.portfolio_3_col, name='portfolio-3-col'),
    path('portfolio-4-col', views.portfolio_4_col, name='portfolio-4-col')
]