# Static&Media



- HTML에서 image를 경로로 쓰면 어떻게될까?

  - URL에서는 경로를 듣도보도 못했는데? =>안띄워

- 장고에서 이미지 파일이 보고싶으면?

  - templates와 비슷하게 /static/요청이 오면 app_name/static/폴더를 찾아서 불러오는거야.

  - settings.py

    - ```django
      STATIC_URL = '/static/'
      STATICFILE_DIRS = [BASE_DIR/'static']
      MEDIA_URL = '/media/'
      MEDIA_ROOT = BASE_DIR/'media'
      ```

  - mater app의 URL

    - ```django
      from django.conf import settings
      from django.conf.urls.static import static
      ```

    - 

- html파일안에

- ```html
  {% load static %}
  
  <img src="/static/app_name/파일이름.확장자" alt = "">
  
  or
  <img src="{% static '/app_name/파일이름.확장자' %}" alt="">
  
  ```



- 데이터 파일을 올릴 때

- ```django
  <form method="post" enctype="multipart/form-data">
      {% csrf_token %}
      <input type="file" name="data" accept="video/*, .pdf">
      
  </form>
  ```

  - input type ="file"의 경우
    - accept = 입력받을 수 있는 파일의 유형을 지정하는 속성.
    - 지정하지않으면 모든 유형의 파일을 입력받을수 있음
    - 여러 종류의 파일을 입력받기 위해서는 아래와 같이 쉼표로 목록을 구분하여 작성합니다.
    - 여러개의 파일을 한꺼번에 지정가능하게 하려면 multiple 속성 부여.
    - required를 적을 경우 해당 칸에 input이 반드시 들어가야함.

## class ResolverMatch

```html
{% if Request.resolver_match.url_name == 'name' %}

{% else %}

{% endif %}

=> resolver_match는 많은걸 들고있어..
자세한건 https://docs.djangoproject.com/en/3.1/ref/urlresolvers/#django.urls.ResolverMatch
```



