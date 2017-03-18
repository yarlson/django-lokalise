===============
Django-Lokalise
===============

`Lokalise <https://lokalise.co>`_ lets you manage keys and translations of your app, game or website – either on your own or with a team of collaborators. Built for developers, Lokalise offers neat features including inline suggestions, project chat, export webhooks and an API, so you can easily integrate with your projects workflow.

Installation
============
You can install Django-Lokalise From **Pypi**::

  pip install django-lokalise

Configuration
=============
First you need to add ``lokalise`` to your INSTALLED_APPS::

    INSTALLED_APPS = [
      # ...
      'lokalise',
    ]

Than you have to add ``lokalise.middleware.ReloadTranslationsMiddleware`` middleware as early as possible ::

    MIDDLEWARE_CLASSES = (
        ...
        'lokalise.middleware.ReloadTranslationsMiddleware',
        ...
    )

Add to your urlpatterns::

    urlpatterns = [
      url(r'^lokalise/', include('lokalise.urls')),
    ]

Add webhook at Download section of lokali.se project such as http://example.org/lokalise/hook and use Gettext(.po) format