from background_task import background
from misfa import models

import requests
import hashlib


class Source():

    def get_model(self):
        pass

    @background
    def pull_data(self):
        pass


class EventbriteSource(Source):

    api_key = '6FNUYEQJTYT7Y4ACYSKI'
    base_url = 'https://www.eventbriteapi.com/v3/events/search'

    @staticmethod
    def get_model():
        return models.Source.objects.get(name='eventbrite')

    @staticmethod
    def make_request(page=1):
        request = requests.get(
            EventbriteSource.base_url,
            params={
                'token': EventbriteSource.api_key,
                'location.address': 'muscat,oman,',
                'page': page
            }
        )

        if request.status_code == 200:
            return request
        return None

    @staticmethod
    def pull_request_data(json_response):
        for event in json_response['events']:

            event_id = str(event['id']).encode('utf-8')
            event_hash = hashlib.sha256(
                'eventbrite'.encode('utf-8') + event_id).hexdigest()

            if models.Entry.objects.filter(source=EventbriteSource.get_model(), hash=event_hash).count() > 0:
                continue

            entry = models.Entry(source=EventbriteSource.get_model(
            ), hash=event_hash)
            entry.save()

            try:
                id_number = models.EntryValue(
                    entry=entry, name='id', value=event['id'])
                id_number.save()

                title = models.EntryValue(
                    entry=entry, name='name', value=event['name']['text'])
                title.save()

                description = models.EntryValue(
                    entry=entry, name='description', value=event['description']['text'])
                description.save()

                url = models.EntryValue(
                    entry=entry, name='url', value=event['url'])
                url.save()

                start = models.EntryValue(
                    entry=entry, name='start', value=event['start']['utc'])
                start.save()

                end = models.EntryValue(
                    entry=entry, name='end', value=event['end']['utc'])
                end.save()

                logo = models.EntryValue(
                    entry=entry, name='logo', value=event['logo']['url'])
                logo.save()
            except:
                pass

    @staticmethod
    @background
    def pull_data():
        json_response = EventbriteSource.make_request().json()

        EventbriteSource.pull_request_data(json_response)

        while json_response['pagination']['has_more_items']:
            json_response = EventbriteSource.make_request(
                page=int(json_response['pagination']['page_number'])+1).json()

            EventbriteSource.pull_request_data(json_response)

    @staticmethod
    def build_entry_dict(entry):
        entry_values = models.EntryValue.objects.filter(entry=entry)
        entry_dict = {}

        for entry_value in entry_values:
            entry_dict[entry_value.name] = entry_value.value

        return entry_dict

    @staticmethod
    @background
    def push_data():
        from wajiha.models import Opportunity
        from django.template.defaultfilters import slugify
        import requests
        from django.core.files.base import ContentFile
        import dateutil.parser

        model = EventbriteSource.get_model()
        entries = models.Entry.objects.filter(source=model, is_pushed=False)

        for entry in entries:
            entry_dict = EventbriteSource.build_entry_dict(entry)
            try:
                opportunity = Opportunity()
                opportunity.slug = slugify(entry_dict['name'])[:50]
                opportunity.title = entry_dict['name']
                opportunity.description = entry_dict['description']
                opportunity.source_url = entry_dict['url']
                opportunity.website = entry_dict['url']
                opportunity.start_at = dateutil.parser.parse(entry_dict['start'])
                opportunity.end_at = dateutil.parser.parse(entry_dict['end'])

                img_response = requests.get(entry_dict['logo'])
                if img_response.status_code == 200:
                    opportunity.image.save('img.jpg', ContentFile(
                        img_response.content), save=True)

                opportunity.save()
            except:
                pass

            entry.is_pushed = True
            entry.save()
