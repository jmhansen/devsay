from django.contrib import admin

from .models import Term, Pronunciation

# for future modification to admin

# class TermAdmin(admin.ModelAdmin):
#     model = Term
#
#
# class PronunciationAdmin(admin.ModelAdmin):
#     model = Pronunciation


admin.site.register(Term)
admin.site.register(Pronunciation)
