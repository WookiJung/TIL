# workshop 13



1) 투표는 생성 및 조회가 가능합니다.

 2) 투표는 주제와 주제에 맞는 항목 2개를 가지고 있습니다. 

3) 댓글은 생성 및 조회가 가능합니다. 

4) 댓글은 하나의 투표에 여러 개가 작성 될 수 있습니다. 

5) 댓글은 투표 문제 중 하나를 반드시 선택해야 합니다. 

6) random 링크를 클릭하면 투표 조회페이지가 랜덤으로 렌더링됩니다. 

7) 투표 조회 페이지에서는 항목별 댓글 개수를 통해 두 항목간 선택 비율을 출력합니다.



class article:

​	title:

​	content1

​	content2



class 투표

​	article= models.for

​	CHOICES = [(content1, content1), (content2, content2)]

​	choices = models.charfield(max_length = 20, choices = CHOICES, default = content1)

