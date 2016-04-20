from django.utils.autoreload import reset_translations


class ReloadTranslationsMiddleware(object):
    @staticmethod
    def process_request(request):
        reset_translations()
