from django.contrib import admin
from .models import Article, Tag, Scope
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
    
class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags_count = 0
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_main'):
                    main_tags_count += 1
                    
        if main_tags_count == 0:
            raise ValidationError('Укажите основной тег для статьи')
        elif main_tags_count > 1:
            raise ValidationError('Основным может быть только один тег')
        
        return super().clean()
    
class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
