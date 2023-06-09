from django.core.management.base import BaseCommand
from faker import Faker
from houses.models import Dong_list
import random
from users.models import User
from houses.models import House, Dong_list, Gu_list, Option, Safetyoption
from images.models import Image
import json


class Command(BaseCommand):
    help = "이 커맨드를 통해 랜덤한 테스트 유저 데이터를 만듭니다."

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=0,
            type=int,
            help="몇 명의 유저를 만드나",
        )

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            self.stdout.write(self.style.SUCCESS("유저를 먼저 생성해주세요."))
            return
        if not Gu_list.objects.exists():
            self.stdout.write(self.style.SUCCESS("구 리스트를 작성중입니다."))
            with open("gu_list.json", "r", encoding="UTF-8") as gu_data:
                gu = json.load(gu_data)
            for i in gu:
                Gu_list.objects.create(
                    pk=i.get("pk"),
                    name=i.get("fields").get("name"),
                )
            self.stdout.write(self.style.SUCCESS("구 리스트가 작성되었습니다."))

        if not Option.objects.exists():
            self.stdout.write(self.style.SUCCESS("옵션 리스트를 작성중입니다."))
            with open("option_list.json", "r", encoding="UTF-8") as option_data:
                option_list = json.load(option_data)
            for option in option_list:
                Option.objects.create(
                    name=option.get("fields").get("name"),
                )
            self.stdout.write(self.style.SUCCESS("옵션 리스트가 작성되었습니다."))

        if not Safetyoption.objects.exists():
            self.stdout.write(self.style.SUCCESS("보안 옵션 리스트를 작성중입니다."))
            with open("safetyoptions.json", "r", encoding="UTF-8") as option_data:
                option_list = json.load(option_data)
            for option in option_list:
                Safetyoption.objects.create(
                    name=option.get("safetyoption"),
                )
            self.stdout.write(self.style.SUCCESS("보안 옵션 리스트가 작성되었습니다."))

        if not Dong_list.objects.exists():
            self.stdout.write(self.style.SUCCESS("동 리스트를 작성중입니다."))
            with open("dong_list.json", "r", encoding="UTF-8") as dong_data:
                dong_list = json.load(dong_data)
            for dong in dong_list:
                Dong_list.objects.create(
                    pk=dong.get("pk"),
                    gu=Gu_list.objects.get(pk=dong.get("fields").get("gu")),
                    name=dong.get("fields").get("name"),
                )
            self.stdout.write(self.style.SUCCESS("동 리스트가 작성되었습니다."))

        total = options.get("total")
        fake = Faker(["ko_KR"])
        new_list = []
        image_key = [
            "4b618568-d21e-4f4c-35bc-12d770c9d200",
            "b254536e-83e6-4167-74f8-970b5b46e700",
            "eb6ccedd-4af5-4597-563c-381d93770100",
            "59f0b7dd-e2f0-4808-92ab-a9636701e600",
            "c88e7a1d-8a03-46a1-35de-a22465f44100",
            "5cd3caef-5455-42ae-0928-819766aade00",
        ]
        self.stdout.write(self.style.SUCCESS("새로운 방을 작성중입니다."))
        all_option = Option.objects.all()
        all_safety_option = Safetyoption.objects.all()
        for i in Dong_list.objects.all():
            for k in range(total):
                house = {"model": "houses.House"}
                data = {
                    "title": fake.building_name(),
                    "sale": 0,
                    "deposit": 0,
                    "monthly_rent": 0,
                    "maintenance_cost": random.randint(5, 20) * 10000,
                    "host": User.objects.get(pk=random.choice([1])),
                    "room": random.randint(1, 3),
                    "toilet": random.randint(1, 3),
                    "pyeongsu": random.randint(10, 50),
                    "room_kind": random.choice(House.RoomKindChoices.values),
                    "sell_kind": random.choice(House.SellKindChoices.values),
                    "address": " ".join(i for i in fake.land_address().split(" ")[2:]),
                    "description": "인근에서 가장 좋은 방입니다.",
                }
                cell_kind = data.get("sell_kind")
                if cell_kind == "SALE":
                    data["sale"] = random.randint(5, 300) * 10000000
                elif cell_kind == "CHARTER":
                    data["deposit"] = random.randint(5, 200) * 1000000
                elif cell_kind == "MONTHLY_RENT":
                    data["deposit"] = random.randint(5, 200) * 1000000
                    data["monthly_rent"] = random.randint(1, 20) * 100000

                create_house = House.objects.create(
                    title=data["title"],
                    sale=data["sale"],
                    deposit=data["deposit"],
                    monthly_rent=data["monthly_rent"],
                    maintenance_cost=data["maintenance_cost"],
                    host=data["host"],
                    room=data["room"],
                    toilet=data["toilet"],
                    pyeongsu=data["pyeongsu"],
                    room_kind=data["room_kind"],
                    sell_kind=data["sell_kind"],
                    address=data["address"],
                    description=data["description"],
                    dong=i,
                    is_sale=True,
                )
                for i in range(random.randint(1, all_option.count() + 1)):
                    create_house.option.add(
                        all_option[random.randint(0, all_option.count() - 1)]
                    )
                for i in range(random.randint(1, all_safety_option.count() + 1)):
                    create_house.Safetyoption.add(
                        all_safety_option[
                            random.randint(0, all_safety_option.count() - 1)
                        ]
                    )
                create_house.save()
                for j in range(5):
                    Image.objects.create(
                        house=create_house,
                        url=f"https://imagedelivery.net/TfkiqSGnbio9VWWQtYee6A/{random.choice(image_key)}/public",
                    )

        self.stdout.write(self.style.SUCCESS(f"{total}개의 방이 작성되었습니다."))
