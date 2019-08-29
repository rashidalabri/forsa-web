from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Entry(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    hash = models.CharField(max_length=255)
    is_pushed = models.BooleanField(default=False)

    def __str__(self):
        return self.source.name + ' ' + self.hash


class EntryValue(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self):
        return self.entry.source.name + ': ' + self.name
