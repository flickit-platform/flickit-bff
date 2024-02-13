from django.db import transaction
from django.core.files.storage import default_storage
from rest_framework import serializers

from account.serializers.userserializers import UserSimpleSerializer, UserSerializer
from account.services import userservices

from baseinfo.models.assessmentkitmodels import ExpertGroup, ExpertGroupAccess
from baseinfo.services import expertgroupservice


class ExpertGroupSerilizer(serializers.ModelSerializer):
    users = UserSimpleSerializer(many=True)
    number_of_members = serializers.SerializerMethodField()
    number_of_assessment_kits = serializers.SerializerMethodField()
    owner = UserSimpleSerializer()
    is_expert = serializers.SerializerMethodField(method_name='check_expert')
    is_member = serializers.SerializerMethodField(method_name='check_is_member')
    is_owner = serializers.SerializerMethodField(method_name='check_is_owner')
    picture = serializers.SerializerMethodField(method_name='get_picture')

    def get_number_of_members(self, expert_group: ExpertGroup):
        return expert_group.users.count()

    def get_number_of_assessment_kits(self, expert_group: ExpertGroup):
        return expert_group.assessmentkits.filter(is_active=True).count()

    def check_expert(self, expert_group: ExpertGroup):
        current_user = self.context.get('request', None).user
        return expertgroupservice.is_current_user_expert(expert_group, current_user)

    def check_is_member(self, expert_group: ExpertGroup):
        current_user = self.context.get('request', None).user
        return current_user in expert_group.users.all()

    def check_is_owner(self, expert_group: ExpertGroup):
        current_user = self.context.get('request', None).user
        return current_user == expert_group.owner

    def get_picture(self, expert_group: ExpertGroup):
        picture_path = expert_group.picture.name
        picture_path = picture_path.replace("media/", '')
        return default_storage.url(picture_path)

    class Meta:
        model = ExpertGroup
        fields = ['id', 'name', 'about', 'bio', 'website', 'picture', 'users',
                  'number_of_members', 'number_of_assessment_kits', 'owner', 'is_expert', 'is_member', 'is_owner']


class ExpertGroupSimpleSerilizer(serializers.ModelSerializer):
    owner = UserSimpleSerializer()

    class Meta:
        model = ExpertGroup
        fields = ['id', 'name', 'owner']


class ExpertGroupAccessSerializer(serializers.ModelSerializer):
    expert_group = ExpertGroupSimpleSerilizer()
    user = UserSerializer()

    class Meta:
        model = ExpertGroupAccess
        fields = ['id', 'user', 'expert_group', 'invite_email', 'invite_expiration_date']


class ExpertGroupGiveAccessSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        user = userservices.load_user_by_email(attrs['email'])
        if user is None:
            error_message = 'user with email {} is not found'.format(attrs['email'])
            raise serializers.ValidationError({'message': error_message})
        return attrs


class ExpertGroupCreateSerilizers(serializers.ModelSerializer):

    @transaction.atomic
    def create(self, validated_data):
        current_user = self.context.get('request', None).user
        expert_group = ExpertGroup(**validated_data)
        expert_group.owner = current_user
        expert_group.save()
        expertgroupservice.add_expert_group_coordinator(expert_group, current_user)
        return expert_group

    @transaction.atomic
    def update(self, expert_group, validated_data):
        ExpertGroup.objects.filter(id=expert_group.id).update(**validated_data)
        expert_group_updated = ExpertGroup.objects.get(id=expert_group.id)

        if 'picture' in validated_data:
            expert_group_updated.picture = validated_data['picture']
            expert_group_updated.save()
            expert_group_updated.picture = "media/" + expert_group_updated.picture.name
            expert_group_updated.save()
        picture_path = expert_group_updated.picture.name
        expert_group_updated.picture.name = picture_path.replace("media/", '')
        return expert_group_updated

    def validate_website(self, website):
        return expertgroupservice.validate_website(website)



    class Meta:
        model = ExpertGroup
        fields = ['id', 'name', 'bio', 'about', 'website', 'picture']


class ExpertGroupAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertGroup
        fields = ['id', 'name', 'picture']
