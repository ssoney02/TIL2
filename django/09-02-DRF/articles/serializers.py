from rest_framework import serializers 
from .models import Article, Comment


# 게시글의 일부 필드를 직렬화 하는 클래스
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


# 게시글의 전체 필드를 직렬화 하는 클래스
class ArticleSerializer(serializers.ModelSerializer):
    
    
    class CommentDetailSerializer(serializers.ModelSerializer): 
        # CommentSerializer 그대로 써도 되는데 그러면 commentserializer를 위로 올려야됨..
        class Meta:
            model = Comment
            fields = ('id', 'content',)
            
    # 기존에 있던 역참조 매니저인 comment_set의 값을 덮어쓰기
    # related_name 설정하면 해당 이름으로 사용할 수 있은ㅁ
    comment_set = CommentDetailSerializer(many=True, read_only=True)
    
    # 새로운 필드 생성 (댓글 개수를 담기 위한 새로운 필드)
    num_of_comments = serializers.SerializerMethodField()       # 읽기 전용 필드를 만듦!
    # 메서드 필드 -> 메서드의 결과를 필드에 담는..
    
    class Meta:
        model = Article
        fields = '__all__'
    
    # SerializerMethodField의 값을 채울 함수
    def get_num_of_comments(self, obj):
        # 여기서 obj는 serializer가 처리하는 article (특정, 해당 게시글) 인스턴스
        # view에서 annotate해서 생긴 새로운 속성 결과를 사용할 수 있게 됨
        
        # 새로운 필드 , get_num_of_commments 필드 이름 맞춤.. => 규칙임!!! 반드시 맞춰야됨!!!!!
        return obj.num_of_comments
        
        
# 댓글 목록 조회를 위한 serializer
class CommentSerializer(serializers.ModelSerializer):
    # 게시글의 제목을 가공해주는 serializer class 만들어야 => 외래키 데이터 내용을 재구성 하기 위해서..
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    
    article = ArticleTitleSerializer(read_only=True)
    # 기존의 article의 결과를 덮어 씌움!!
    
    class Meta:
        model = Comment
        fields = '__all__'
        # 외래키 필드를 유효성 검사 목록에서 빼줘야 함
        # 외래키를 아예 exclude시키면 안됨
        # client가 응답은 받을 수 있는데 사용자가 쓰는 필드는 x
        # <읽기전용 필드>
        # 응답 데이터로서는 유지하는데 유효성 검사에서만 뺌!!!
        
        # read_only_fields = ('article',)     
        
        
        # 위에서 article을 새로 덮어 씌워버리면 read_only_fields는 동작하지 않음
        # -> 위에서 read_only=True로 해당 기능 추가..
        
        
        
        
