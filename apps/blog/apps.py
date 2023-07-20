from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'apps.blog'
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = '文章管理'