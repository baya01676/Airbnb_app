import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from airbnb_app.models import (
    UserProfile, City, Rules, Guest, Property,
    PropertyImage, Booking, Review, Amenity
)
from django.contrib.auth.hashers import make_password
from datetime import date, timedelta

# Очистка базы данных (опционально)
print("Очистка базы данных...")
Review.objects.all().delete()
Booking.objects.all().delete()
PropertyImage.objects.all().delete()
Property.objects.all().delete()
Amenity.objects.all().delete()
Guest.objects.all().delete()
Rules.objects.all().delete()
City.objects.all().delete()
UserProfile.objects.all().delete()

print("База данных очищена!")

# Создание городов
print("\nСоздание городов...")
cities_data = [
    {'city_name_ru': 'Бишкек', 'city_name_en': 'Bishkek'},
    {'city_name_ru': 'Ош', 'city_name_en': 'Osh'},
    {'city_name_ru': 'Джалал-Абад', 'city_name_en': 'Jalal-Abad'},
    {'city_name_ru': 'Каракол', 'city_name_en': 'Karakol'},
    {'city_name_ru': 'Токмок', 'city_name_en': 'Tokmok'},
    {'city_name_ru': 'Нарын', 'city_name_en': 'Naryn'},
    {'city_name_ru': 'Талас', 'city_name_en': 'Talas'},
    {'city_name_ru': 'Баткен', 'city_name_en': 'Batken'},
]

cities = []
for city_data in cities_data:
    city = City.objects.create(
        city_name=city_data['city_name_ru'],
        city_name_ru=city_data['city_name_ru'],
        city_name_en=city_data['city_name_en']
    )
    cities.append(city)
    print(f"✓ Создан город: {city.city_name}")

# Создание правил
print("\nСоздание правил...")
rules_data = [
    {'rules': 'no_smoking', 'rules_ru': 'Курение запрещено', 'rules_en': 'No smoking'},
    {'rules': 'pets_allowed', 'rules_ru': 'Разрешены домашние животные', 'rules_en': 'Pets allowed'},
    {'rules': 'no_smoking', 'rules_ru': 'Не курить в помещении', 'rules_en': 'No indoor smoking'},
    {'rules': 'pets_allowed', 'rules_ru': 'Можно с питомцами', 'rules_en': 'Pet friendly'},
    {'rules': 'etc', 'rules_ru': 'Тихие часы после 22:00', 'rules_en': 'Quiet hours after 10 PM'},
    {'rules': 'etc', 'rules_ru': 'Уборка перед выездом', 'rules_en': 'Clean before checkout'},
    {'rules': 'etc', 'rules_ru': 'Запрещены вечеринки', 'rules_en': 'No parties'},
    {'rules': 'etc', 'rules_ru': 'Не беспокоить соседей', 'rules_en': 'Respect neighbors'},
]

rules = []
for rule_data in rules_data:
    rule = Rules.objects.create(
        rules=rule_data['rules'],
        rules_ru=rule_data['rules_ru'],
        rules_en=rule_data['rules_en']
    )
    rules.append(rule)
    print(f"✓ Создано правило: {rule.rules_ru}")

# Создание типов гостей
print("\nСоздание типов гостей...")
guests_data = [
    {'guest_name_ru': 'Семьи с детьми', 'guest_name_en': 'Families with children'},
    {'guest_name_ru': 'Бизнес-путешественники', 'guest_name_en': 'Business travelers'},
    {'guest_name_ru': 'Пары', 'guest_name_en': 'Couples'},
    {'guest_name_ru': 'Группы друзей', 'guest_name_en': 'Groups of friends'},
    {'guest_name_ru': 'Индивидуальные путешественники', 'guest_name_en': 'Solo travelers'},
    {'guest_name_ru': 'Пожилые люди', 'guest_name_en': 'Senior citizens'},
    {'guest_name_ru': 'Студенты', 'guest_name_en': 'Students'},
    {'guest_name_ru': 'Молодожёны', 'guest_name_en': 'Newlyweds'},
]

guests = []
for guest_data in guests_data:
    guest = Guest.objects.create(
        guest_name=guest_data['guest_name_ru'],
        guest_name_ru=guest_data['guest_name_ru'],
        guest_name_en=guest_data['guest_name_en']
    )
    guests.append(guest)
    print(f"✓ Создан тип гостя: {guest.guest_name}")

# Создание пользователей
print("\nСоздание пользователей...")
users_data = [
    {
        'username': 'admin', 'email': 'admin@airbnb.kg',
        'first_name': 'Администратор', 'last_name': 'Системы',
        'role': 'admin', 'phone_number': '+996555123456'
    },
    {
        'username': 'aibek_host', 'email': 'aibek@gmail.com',
        'first_name': 'Айбек', 'last_name': 'Исаков',
        'role': 'host', 'phone_number': '+996700111222'
    },
    {
        'username': 'aigul_host', 'email': 'aigul@gmail.com',
        'first_name': 'Айгуль', 'last_name': 'Токтосунова',
        'role': 'host', 'phone_number': '+996555333444'
    },
    {
        'username': 'nurlan_host', 'email': 'nurlan@gmail.com',
        'first_name': 'Нурлан', 'last_name': 'Асанов',
        'role': 'host', 'phone_number': '+996777555666'
    },
    {
        'username': 'maria_guest', 'email': 'maria@gmail.com',
        'first_name': 'Мария', 'last_name': 'Петрова',
        'role': 'guest', 'phone_number': '+996555777888'
    },
    {
        'username': 'john_guest', 'email': 'john@gmail.com',
        'first_name': 'John', 'last_name': 'Smith',
        'role': 'guest', 'phone_number': '+996700999000'
    },
    {
        'username': 'azamat_guest', 'email': 'azamat@gmail.com',
        'first_name': 'Азамат', 'last_name': 'Бакиров',
        'role': 'guest', 'phone_number': '+996555222333'
    },
    {
        'username': 'elena_guest', 'email': 'elena@gmail.com',
        'first_name': 'Елена', 'last_name': 'Соколова',
        'role': 'guest', 'phone_number': '+996777444555'
    },
]

users = []
for user_data in users_data:
    user = UserProfile.objects.create(
        username=user_data['username'],
        email=user_data['email'],
        first_name=user_data['first_name'],
        last_name=user_data['last_name'],
        role=user_data['role'],
        phone_number=user_data['phone_number'],
        password=make_password('password123')
    )
    users.append(user)
    print(f"✓ Создан пользователь: {user.username} ({user.role})")

# Получаем хостов
hosts = [u for u in users if u.role == 'host']
guests_users = [u for u in users if u.role == 'guest']

# Создание объектов недвижимости
print("\nСоздание объектов недвижимости...")
properties_data = [
    {
        'title_ru': 'Уютная квартира в центре Бишкека',
        'title_en': 'Cozy apartment in the center of Bishkek',
        'description_ru': 'Современная квартира с прекрасным видом на горы. Рядом с торговым центром Vefa и парком. Идеально для туристов и бизнесменов.',
        'description_en': 'Modern apartment with beautiful mountain views. Near Vefa shopping center and park. Perfect for tourists and businessmen.',
        'price_per_night': 3500,
        'city': cities[0],
        'address_ru': 'пр. Чуй 125, Бишкек',
        'address_en': 'Chui Ave 125, Bishkek',
        'property_type': 'apartment',
        'max_guests': 4,
        'max_bedrooms': 2,
        'max_bathrooms': 1,
        'owner': hosts[0],
        'is_active': True
    },
    {
        'title_ru': 'Просторный дом у озера Иссык-Куль',
        'title_en': 'Spacious house by Issyk-Kul lake',
        'description_ru': 'Большой дом с собственным пляжем. 3 спальни, огромная терраса, барбекю зона. До воды 50 метров.',
        'description_en': 'Large house with private beach. 3 bedrooms, huge terrace, BBQ area. 50 meters to water.',
        'price_per_night': 8000,
        'city': cities[3],
        'address_ru': 'ул. Набережная 45, Каракол',
        'address_en': 'Naberezhnaya St 45, Karakol',
        'property_type': 'house',
        'max_guests': 8,
        'max_bedrooms': 3,
        'max_bathrooms': 2,
        'owner': hosts[1],
        'is_active': True
    },
    {
        'title_ru': 'Студия для студентов в Оше',
        'title_en': 'Studio for students in Osh',
        'description_ru': 'Небольшая уютная студия рядом с ОшГУ. Все необходимое для комфортной жизни. Wi-Fi, кухня, стиральная машина.',
        'description_en': 'Small cozy studio near OshSU. Everything you need for comfortable living. Wi-Fi, kitchen, washing machine.',
        'price_per_night': 1500,
        'city': cities[1],
        'address_ru': 'ул. Ленина 88, Ош',
        'address_en': 'Lenin St 88, Osh',
        'property_type': 'studio',
        'max_guests': 2,
        'max_bedrooms': 1,
        'max_bathrooms': 1,
        'owner': hosts[2],
        'is_active': True
    },
    {
        'title_ru': 'Роскошные апартаменты с панорамным видом',
        'title_en': 'Luxury apartments with panoramic view',
        'description_ru': 'Элитная квартира на последнем этаже. Панорамные окна, дизайнерский ремонт, все включено. Парковка в подземном паркинге.',
        'description_en': 'Elite apartment on the top floor. Panoramic windows, designer renovation, all inclusive. Underground parking.',
        'price_per_night': 12000,
        'city': cities[0],
        'address_ru': 'мкр. Асанбай, Бишкек',
        'address_en': 'Asanbai district, Bishkek',
        'property_type': 'apartment',
        'max_guests': 6,
        'max_bedrooms': 3,
        'max_bathrooms': 2,
        'owner': hosts[0],
        'is_active': True
    },
    {
        'title_ru': 'Семейный дом в Джалал-Абаде',
        'title_en': 'Family house in Jalal-Abad',
        'description_ru': 'Большой семейный дом с садом и детской площадкой. Тихий район, рядом школа и детский сад. Идеально для семей.',
        'description_en': 'Large family house with garden and playground. Quiet area, near school and kindergarten. Perfect for families.',
        'price_per_night': 5000,
        'city': cities[2],
        'address_ru': 'ул. Токтогула 23, Джалал-Абад',
        'address_en': 'Toktogul St 23, Jalal-Abad',
        'property_type': 'house',
        'max_guests': 6,
        'max_bedrooms': 3,
        'max_bathrooms': 2,
        'owner': hosts[1],
        'is_active': True
    },
    {
        'title_ru': 'Минималистичная студия в новостройке',
        'title_en': 'Minimalist studio in new building',
        'description_ru': 'Современная студия в стиле минимализм. Новая мебель, бытовая техника. Охраняемая территория, консьерж.',
        'description_en': 'Modern studio in minimalist style. New furniture, appliances. Secure area, concierge.',
        'price_per_night': 2800,
        'city': cities[0],
        'address_ru': 'мкр. Джал, Бишкек',
        'address_en': 'Jal district, Bishkek',
        'property_type': 'studio',
        'max_guests': 2,
        'max_bedrooms': 1,
        'max_bathrooms': 1,
        'owner': hosts[2],
        'is_active': True
    },
    {
        'title_ru': 'Загородная вилла в Токмоке',
        'title_en': 'Country villa in Tokmok',
        'description_ru': 'Роскошная вилла с бассейном и сауной. Огромная территория, беседка, мангальная зона. До города 15 минут.',
        'description_en': 'Luxury villa with pool and sauna. Huge territory, gazebo, BBQ area. 15 minutes to city.',
        'price_per_night': 15000,
        'city': cities[4],
        'address_ru': 'с. Ивановка, Токмок',
        'address_en': 'Ivanovka village, Tokmok',
        'property_type': 'house',
        'max_guests': 10,
        'max_bedrooms': 4,
        'max_bathrooms': 3,
        'owner': hosts[0],
        'is_active': True
    },
    {
        'title_ru': 'Квартира с видом на Ала-Тоо',
        'title_en': 'Apartment with Ala-Too view',
        'description_ru': 'Светлая квартира с балконом и видом на площадь Ала-Тоо. В шаговой доступности все достопримечательности столицы.',
        'description_en': 'Bright apartment with balcony and Ala-Too square view. Walking distance to all city attractions.',
        'price_per_night': 4200,
        'city': cities[0],
        'address_ru': 'ул. Киевская 112, Бишкек',
        'address_en': 'Kievskaya St 112, Bishkek',
        'property_type': 'apartment',
        'max_guests': 3,
        'max_bedrooms': 1,
        'max_bathrooms': 1,
        'owner': hosts[1],
        'is_active': True
    },
]

properties = []
for prop_data in properties_data:
    property_obj = Property.objects.create(
        title=prop_data['title_ru'],
        title_ru=prop_data['title_ru'],
        title_en=prop_data['title_en'],
        description=prop_data['description_ru'],
        description_ru=prop_data['description_ru'],
        description_en=prop_data['description_en'],
        price_per_night=prop_data['price_per_night'],
        city=prop_data['city'],
        address=prop_data['address_ru'],
        address_ru=prop_data['address_ru'],
        address_en=prop_data['address_en'],
        property_type=prop_data['property_type'],
        max_guests=prop_data['max_guests'],
        max_bedrooms=prop_data['max_bedrooms'],
        max_bathrooms=prop_data['max_bathrooms'],
        owner=prop_data['owner'],
        is_active=prop_data['is_active']
    )

    # Добавление правил к объекту
    property_obj.rules.add(rules[0], rules[4], rules[6])

    properties.append(property_obj)
    print(f"✓ Создана недвижимость: {property_obj.title}")

# Создание удобств (Amenities)
print("\nСоздание удобств...")
amenities_data = [
    'Wi-Fi', 'Кондиционер', 'Отопление', 'Кухня',
    'Стиральная машина', 'Телевизор', 'Парковка', 'Бассейн'
]

amenities = []
for amenity_name in amenities_data:
    amenity = Amenity.objects.create(name=amenity_name)
    # Добавляем удобства к нескольким объектам
    amenity.property.add(*properties[:4])
    amenities.append(amenity)
    print(f"✓ Создано удобство: {amenity.name}")

# Создание бронирований
print("\nСоздание бронирований...")
bookings_data = [
    {
        'property': properties[0],
        'quest': guests_users[0],
        'check_in': date.today() + timedelta(days=5),
        'check_out': date.today() + timedelta(days=10),
        'status': 'approved'
    },
    {
        'property': properties[1],
        'quest': guests_users[1],
        'check_in': date.today() + timedelta(days=15),
        'check_out': date.today() + timedelta(days=20),
        'status': 'pending'
    },
    {
        'property': properties[2],
        'quest': guests_users[2],
        'check_in': date.today() - timedelta(days=10),
        'check_out': date.today() - timedelta(days=5),
        'status': 'approved'
    },
    {
        'property': properties[3],
        'quest': guests_users[0],
        'check_in': date.today() + timedelta(days=30),
        'check_out': date.today() + timedelta(days=35),
        'status': 'approved'
    },
    {
        'property': properties[4],
        'quest': guests_users[1],
        'check_in': date.today() + timedelta(days=7),
        'check_out': date.today() + timedelta(days=14),
        'status': 'rejected'
    },
    {
        'property': properties[5],
        'quest': guests_users[2],
        'check_in': date.today() + timedelta(days=20),
        'check_out': date.today() + timedelta(days=25),
        'status': 'pending'
    },
    {
        'property': properties[6],
        'quest': guests_users[3],
        'check_in': date.today() - timedelta(days=5),
        'check_out': date.today(),
        'status': 'approved'
    },
    {
        'property': properties[7],
        'quest': guests_users[3],
        'check_in': date.today() + timedelta(days=3),
        'check_out': date.today() + timedelta(days=6),
        'status': 'cancelled'
    },
]

bookings = []
for booking_data in bookings_data:
    booking = Booking.objects.create(**booking_data)
    bookings.append(booking)
    print(f"✓ Создано бронирование: {booking.property.title} - {booking.status}")

# Создание отзывов
print("\nСоздание отзывов...")
reviews_data = [
    {
        'property': properties[0],
        'rating': 5,
        'guest': guests[0],
        'comment': 'Отличная квартира! Все как на фотографиях. Хозяин очень приветливый. Рекомендую!'
    },
    {
        'property': properties[1],
        'rating': 4,
        'guest': guests[1],
        'comment': 'Прекрасное место для отдыха с семьей. Немного далеко от города, но оно того стоит.'
    },
    {
        'property': properties[2],
        'rating': 5,
        'guest': guests[4],
        'comment': 'Идеально для студента! Чисто, уютно, недорого. Буду бронировать еще.'
    },
    {
        'property': properties[3],
        'rating': 5,
        'guest': guests[2],
        'comment': 'Роскошные апартаменты! Вид просто потрясающий. Все удобства на высшем уровне.'
    },
    {
        'property': properties[4],
        'rating': 4,
        'guest': guests[0],
        'comment': 'Хороший дом для семейного отдыха. Детям понравилась площадка во дворе.'
    },
    {
        'property': properties[5],
        'rating': 5,
        'guest': guests[3],
        'comment': 'Современная студия в новом доме. Все новое, чистое. Консьерж помог с багажом.'
    },
    {
        'property': properties[6],
        'rating': 5,
        'guest': guests[2],
        'comment': 'Шикарная вилла! Бассейн, сауна, огромная территория. Праздновали день рождения - все на высоте!'
    },
    {
        'property': properties[7],
        'rating': 4,
        'guest': guests[1],
        'comment': 'Хорошая квартира в центре. Удобное расположение, рядом все необходимое.'
    },
]

reviews = []
for review_data in reviews_data:
    review = Review.objects.create(**review_data)
    reviews.append(review)
    print(f"✓ Создан отзыв: {review.property.title} - {review.rating}⭐")

print("\n" + "=" * 60)
print("✅ База данных успешно заполнена!")
print("=" * 60)
print(f"Создано:")
print(f"  • Городов: {len(cities)}")
print(f"  • Правил: {len(rules)}")
print(f"  • Типов гостей: {len(guests)}")
print(f"  • Пользователей: {len(users)}")
print(f"  • Объектов недвижимости: {len(properties)}")
print(f"  • Удобств: {len(amenities)}")
print(f"  • Бронирований: {len(bookings)}")
print(f"  • Отзывов: {len(reviews)}")
print("=" * 60)
print("\nДля входа в админку используйте:")
print("  Username: admin")
print("  Password: password123")
print("=" * 60)