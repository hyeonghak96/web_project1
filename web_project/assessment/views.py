from django.views.generic import ListView, DetailView
from assessment.models import Post
# ListView
class PostLV(ListView):
 model = Post
 template_name = 'assessment/post_all.html' # 템플릿 파일명 변경
 context_object_name = 'posts' # 컨텍스트 객체 이름 변경(object_list)
#  paginate_by = 6 # 페이지네이션, 페이지당 문서 건 수

# DetailView
class PostDV(DetailView):
 model = Post