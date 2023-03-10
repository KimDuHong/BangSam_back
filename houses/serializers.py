from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import House, Gu_list, Dong_list
from images.serializers import ImageSerializer


class TinyHouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = ("id", "title")


class DonglistSerializer(ModelSerializer):
    class Meta:
        model = Dong_list
        fields = (
            # "gu",
            "pk",
            "name",
        )


class HouseSerializer(ModelSerializer):
    Image = ImageSerializer(many=True, read_only=True)
    dong = DonglistSerializer(read_only=True)

    class Meta:
        model = House
        fields = (
            "id",
            "Image",
            "gu",
            "title",
            "price",
            "room",
            "toilet",
            "pyeongsu",
            "distance_to_station",
            "room_kind",
            "cell_kind",
            "address",
            "photo",
            "description",
            "visited",
            "owner",
            "realtor",
            "dong",
        )


class HouseDetailSerializer(ModelSerializer):
    class Meta:
        model = House
        exclude = ("updated_at",)


class GulistSerializer(ModelSerializer):
    class Meta:
        model = Gu_list
        fields = (
            "pk",
            "name",
        )
