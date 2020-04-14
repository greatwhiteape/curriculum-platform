from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query

# from evolution.content.models import ContentPage
# from evolution.home.models import HomePage

from modules.models import Module
# from modules.models import Module, Chapter
# from lessons.models import StandAloneLesson


def search(request):
    # Search
    search_query = request.GET.get('q', None)
    if search_query:
        if 'elasticsearch' in settings.WAGTAILSEARCH_BACKENDS['default']['BACKEND']:
            # In production, use ElasticSearch and a simplified search query, per
            # http://docs.wagtail.io/en/v1.12.1/topics/search/backends.html
            # like this:
            search_results = Page.objects.live().search(search_query)
        else:
            # If we aren't using ElasticSearch for the demo, fall back to native db search.
            # But native DB search can't search specific fields in our models on a `Page` query.
            # So for demo purposes ONLY, we hard-code in the model names we want to search.

            content_results = ContentPage.objects.live().search(search_query)
            content_results_ids = [p.page_ptr.id for p in content_results]

            curriculum_results = ContentPage.objects.live().search(search_query)
            curriculum_results_ids = [p.page_ptr.id for p in curriculum_results]

            page_ids = content_results_ids + curriculum_results_ids
            search_results = Page.objects.live().filter(id__in=page_ids)

        query = Query.get(search_query)

        # Record hit
        query.add_hit()

    else:
        search_results = Page.objects.none()

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
    })