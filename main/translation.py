from modeltranslation.translator import translator, TranslationOptions

from main.models import Category, SubCategory, Production, TeamMember, HeadLine, NetworkPartner
from theater.settings import MODELTRANSLATION_LANGUAGES


class CategoryTranslationOptions(TranslationOptions):
    fields = Category.translatable_fields_list()
    required_languages = MODELTRANSLATION_LANGUAGES


translator.register(Category, CategoryTranslationOptions)


class SubCategoryTranslationOptions(TranslationOptions):
    fields = SubCategory.translatable_fields_list()
    required_languages = MODELTRANSLATION_LANGUAGES


translator.register(SubCategory, CategoryTranslationOptions)


class ProductionTranslationOptions(TranslationOptions):
    fields = Production.translatable_fields_list()
    required_languages = MODELTRANSLATION_LANGUAGES


translator.register(Production, ProductionTranslationOptions)


class TeamMemberTranslationOptions(TranslationOptions):
    fields = TeamMember.translatable_fields_list()
    required_languages = MODELTRANSLATION_LANGUAGES


translator.register(TeamMember, TeamMemberTranslationOptions)


class HeadLineTranslationOptions(TranslationOptions):
    fields = HeadLine.translatable_fields_list()
    required_languages = MODELTRANSLATION_LANGUAGES


translator.register(HeadLine, HeadLineTranslationOptions)


class NetworkPartnerTranslationOptions(TranslationOptions):
    fields = NetworkPartner.translatable_fields_list()
    required_languages = MODELTRANSLATION_LANGUAGES


translator.register(NetworkPartner, NetworkPartnerTranslationOptions)
