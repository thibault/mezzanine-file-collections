from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from mezzanine_file_collections.models import MediaLibrary, MediaFile


class MediaFileInline(TabularDynamicInlineAdmin):
    model = MediaFile


class MediaLibraryAdmin(PageAdmin):
    inlines = (MediaFileInline,)


admin.site.register(MediaLibrary, MediaLibraryAdmin)
