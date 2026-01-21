from modeltranslation.translator import TranslationOptions, register
from .models import City, Rules, Guest, Property

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)

@register(Rules)
class RulesTranslationOptions(TranslationOptions):
    fields = ('rules_name',)

@register(Guest)
class GuestTranslationOptions(TranslationOptions):
    fields = ('guest_name',)

@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'address', 'property_type',)