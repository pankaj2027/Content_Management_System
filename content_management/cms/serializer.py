from rest_framework import serializers
from cms.models import User, UserProfile, Content
import re


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'state', 'country', 'pincode')

    # field validation for pincode
    def validate_pincode(self,value):               
        value = str(value)
        if len(value) != 6:
            raise serializers.ValidationError('Pincode should be 5 digits')
        return int(value)

    # field validation for  Phone_number
    def validate_phone(self,value):                 
        Pattern = re.compile("^[6789][0-9]{9}")
        value = str(value)
        if Pattern.match(value) is None:
            raise serializers.ValidationError('Invalid Mobile Number!!')
        return value


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)
    password = serializers.CharField( write_only=True,required=False,min_length=8, error_messages={
                                            "blank": "Password cannot be empty.",
                                            "min_length": "Password too short.",
                                        },)
    full_name = serializers.CharField(source='get_full_name', read_only= True) 
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id','username', 'email','full_name','first_name','last_name','password','profile')
        
   # Validation on the password, which contains 1 uppercase, 1 lowercase
    def validate_password(self,value):
        if not re.findall('(?=.*[a-z])(?=.*[A-Z])', value):
            raise serializers.ValidationError("The password must contain at least 1 uppercase, 1 lowercase ")
        return value       
        
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user
    

class ContentSerializers(serializers.ModelSerializer):
    user = serializers.CharField(source="user.id",  read_only=True)

    class Meta:
        model = Content
        fields = ['id','user','title','body','summary','document','categories']