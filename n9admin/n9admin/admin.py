from django.contrib import admin
from .models import Welcome,Idea, Portfolio,ClientArchives
class WelcomeAdmin(admin.ModelAdmin):
    list_display = ('phrase', 'sub_phrase', 'created_at', 'img')
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title','msg','desc')
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','desc','img','created_at','specs')
class ClientArchive(admin.ModelAdmin):
    list_display = ('email','title','description','archive','specifications','created_at')

admin.site.register(Welcome, WelcomeAdmin)
admin.site.register(Idea,IdeaAdmin)
admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(ClientArchives, ClientArchive)