from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import*

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['Firstname', 'Lastname1', 'Lastname2', 'Age','CP','Location','Street','Municipality','State','Phone']

    def create(self, validated_data):
            return Client.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Firstname=validated_data.get('name',instance.firstname)
        instance.Lastname1 = validated_data.get('lastname', instance.Lastname1)
        instance.Lastname2 = validated_data.get('lastname', instance.Lastname2)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.CP = validated_data.get('CP', instance.CP)
        instance.Location = validated_data.get('location', instance.Location)
        instance.Street = validated_data.get('Street', instance.Street)
        instance.Municipality = validated_data.get('Municipality', instance.Municipality)
        instance.State = validated_data.get('State', instance.State)
        instance.Phone = validated_data.get('Phone', instance.Phone)
        instance.save()
        return instance

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['Firstname', 'Lastname1', 'Lastname2', 'Age','CP','Location','Street','Municipality','State','Phone','Professional']

    def create(self, validated_data):
            return Doctor.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Firstname=validated_data.get('name',instance.firstname)
        instance.Lastname1 = validated_data.get('lastname', instance.Lastname1)
        instance.Lastname2 = validated_data.get('lastname', instance.Lastname2)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.CP = validated_data.get('CP', instance.CP)
        instance.Location = validated_data.get('location', instance.Location)
        instance.Street = validated_data.get('Street', instance.Street)
        instance.Municipality = validated_data.get('Municipality', instance.Municipality)
        instance.State = validated_data.get('State', instance.State)
        instance.Phone = validated_data.get('Phone', instance.Phone)
        instance.Professional = validated_data.get('Professional', instance.Professional)
        instance.save()
        return instance

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ['Firstname', 'Lastname1', 'Lastname2', 'Age','CP','Location','Street','Municipality','State','Phone']

    def create(self, validated_data):
            return Vendor.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Firstname=validated_data.get('name',instance.firstname)
        instance.Lastname1 = validated_data.get('lastname', instance.Lastname1)
        instance.Lastname2 = validated_data.get('lastname', instance.Lastname2)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.CP = validated_data.get('CP', instance.CP)
        instance.Location = validated_data.get('location', instance.Location)
        instance.Street = validated_data.get('Street', instance.Street)
        instance.Municipality = validated_data.get('Municipality', instance.Municipality)
        instance.State = validated_data.get('State', instance.State)
        instance.Phone = validated_data.get('Phone', instance.Phone)
        instance.save()
        return instance

class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ['Firstname', 'Lastname1', 'Lastname2','Phone']

    def create(self, validated_data):
            return Provider.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Firstname=validated_data.get('name',instance.Firstname)
        instance.Lastname1 = validated_data.get('lastname', instance.Lastname1)
        instance.Lastname2 = validated_data.get('lastname', instance.Lastname2)
        instance.Phone = validated_data.get('Phone', instance.Phone)
        instance.save()
        return instance

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['Name','Description']

    def create(self, validated_data):
            return Service.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Name=validated_data.get('Name',instance.Name)
        instance.Description = validated_data.get('Description', instance.Description)
        instance.save()
        return instance

class MascotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascot
        fields = ['Name','Race','Color','Age','Type','Foto']

    def create(self, validated_data):
            return Mascot.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Name=validated_data.get('Name',instance.Name)
        instance.Race = validated_data.get('Race', instance.Race)
        instance.Color = validated_data.get('Color', instance.Color)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.Type = validated_data.get('Type', instance.Type)
        instance.Foto = validated_data.get('Foto', instance.Foto)
        instance.save()
        return instance

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['Name','Quantity','Price','Expiration']

    def create(self, validated_data):
            return Product.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Name=validated_data.get('Name',instance.Name)
        instance.Quantity = validated_data.get('Quantity', instance.Quantity)
        instance.Price = validated_data.get('Price', instance.Price)
        instance.Expiration = validated_data.get('Expiration', instance.Expiration)
        instance.save()
        return instance


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office
        fields = ['Name','CP','Location','Street','Municipality','State','Phone']

    def create(self, validated_data):
            return Office.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Name=validated_data.get('Name',instance.Name)
        instance.CP = validated_data.get('CP', instance.CP)
        instance.Location = validated_data.get('location', instance.Location)
        instance.Street = validated_data.get('Street', instance.Street)
        instance.Municipality = validated_data.get('Municipality', instance.Municipality)
        instance.State = validated_data.get('State', instance.State)
        instance.Phone = validated_data.get('Phone', instance.Phone)
        instance.save()
        return instance

class CiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cite
        fields = ['Date']

    def create(self, validated_data):
            return Cite.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Date=validated_data.get('Date',instance.Date)

        instance.save()
        return instance

class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cite
        fields = ['Date']

    def create(self, validated_data):
            return Cite.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Date=validated_data.get('Date',instance.Date)

        instance.save()
        return instance
