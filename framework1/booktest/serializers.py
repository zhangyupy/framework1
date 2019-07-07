"""创建序列化类"""
from rest_framework import serializers

from booktest.models import BookInfo


class BookinfoSerializer(serializers.ModelSerializer):
    """图书序列化器类"""
    # id=serializers.IntegerField(label='ID',read_only=True)
    # btitle=serializers.CharField(label='图书名称',max_length=20)
    # bread=serializers.IntegerField(label='阅读量',required=False)
    # bpub_date = serializers.DateField(label='出版日期')
    # bcomment=serializers.IntegerField(label='阅读量',required=False)
    class Meta:
        model=BookInfo
        fields='__all__'
        extra_kwargs={
            'bread':{'min_value':0},
            'bcomment':{'min_value':0}
        }
    # def create(self, validated_data):
    #     """新建"""
    #     book = BookInfo.objects.create(**validated_data)
    #     return book
    #
    # def update(self, instance, validated_data):
    #     """更新，instance为要更新的对象实例"""
    #     instance.btitle = validated_data.get('btitle', instance.btitle)
    #     instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
    #     instance.save()
    #     return instance
class HeroinfoSerializer(serializers.Serializer):
    GENDER_CHOICES=(
        (0,'male'),
        (1,'female')
    )
    id=serializers.IntegerField(label='ID',read_only=True)
    hname=serializers.CharField(label='名字',max_length=20)
    hgender=serializers.ChoiceField(choices=GENDER_CHOICES,label='性别',required=False)
    hcomment=serializers.CharField(label='描述信息',max_length=200,required=False)
    #  1）将关联对象序列化为关联对象的主健
    # hbook=serializers.PrimaryKeyRelatedField(label='图书',read_only=True)
    # 或者
    # hbook=serializers.PrimaryKeyRelatedField(label='图书',queryset=BookInfo.objects.all())
    #  2) 使用指定的序列化器类将关联对象进行序列化。
    # hbook=BookinfoSerializer()
    #  3) 将关联对象序列化为关联对象模型类__str__方法的返回值。
    hbook=serializers.StringRelatedField(label='图书')