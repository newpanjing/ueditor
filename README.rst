 django ueditor 插件
----
> 本项目大量拷贝了 django-ckeditor的代码

使用：
> pip install ueditor

功能介绍
----
- 最新版ueditor
- 支持图片上传
- 支持在线文件管理
- 完美支持python3+

配置
----
setting.py 文件加入：
::
    UEDITOR_UPLOAD_PREFIX = "/static/upload/"
    UEDITOR_UPLOAD_DIR = os.path.join(BASE_DIR, 'static/upload/')


使用代码：
::
    from ueditor.fields import RichTextField

    #ueditor json配置

    CONFIG={

    }

    class Article(models.Model):
        title = models.CharField(max_length=256, verbose_name='标题', blank=False, null=False)
        content = RichTextField(verbose_name='内容', null=False, blank=False,
                            config=CONFIG)

问题
----
- ueditor 很多东西都已经用不了了，项目最后维护是在2016年
- 如果上传遇到403 错误，django.middleware.csrf.CsrfViewMiddleware 去掉这一句，在settings.py
