from django.urls import reverse, resolve


class TestUrls:

    #  1 path('', index, name='home'),
    def test_index_url(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'

    #  2 test path('post_detail/<post_pk>/', post_detail, name='post_detail')
    def test_post_detail_url(self):
        path = reverse('post_detail', kwargs={'post_pk': 1})
        assert resolve(path).view_name == 'post_detail'

    #  3 path('add_post/', CreatePost.as_view(), name='add_post')
    def test_add_post_url(self):
        path = reverse('add_post')
        assert resolve(path).view_name == 'add_post'

    #  4 path('delete_post/<post_pk>/', delete_post, name='delete_post')
    def test_delete_post_url(self):
        path = reverse('delete_post', kwargs={'post_pk': 1})
        assert resolve(path).view_name == 'delete_post'

    # 5 path('delete_comment/<comm_pk>/', delete_comment, name='delete_comment'),
    def test_delete_comments_url(self):
        path = reverse('delete_comment', kwargs={'comm_pk': 1})
        assert resolve(path).view_name == 'delete_comment'

    # 6 path('no_permission/', no_permission, name='no_permission'),
    def test_no_permission_url(self):
        path = reverse('no_permission')
        assert resolve(path).view_name == 'no_permission'

    # 7 path('accounts/register/', register, name='register'),
    def test_register_url(self):
        path = reverse('register')
        assert resolve(path).view_name == 'register'

    # 8 path('accounts/profile/', profile, name='profile'),
    def test_profile_url(self):
        path = reverse('profile')
        assert resolve(path).view_name == 'profile'





    # without test
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('admin/', admin.site.urls),