from __future__ import unicode_literals

from django.db import models

# Create your models here.
class upstream_config(models.Model):
    status = models.BooleanField(default=False)
    address = models.CharField(max_length=64,null=True)
    port = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    max_fails = models.IntegerField()
    fail_timeout = models.IntegerField()

class proxy_config(models.Model):
    config_id = models.CharField(max_length=64,null=True)
    protocols = models.BooleanField(default=False)
    proxy_name = models.CharField(max_length=128,null=True)
    status = models.BooleanField(default=False)
    listen = models.IntegerField(null=False)
    server_name = models.CharField(max_length=128,null=True)
    access_log = models.CharField(max_length=128,null=True)
    error_log = models.CharField(max_length=128,null=True)
    ssl_cert = models.CharField(max_length=32,null=True)
    ssl_key = models.CharField(max_length=32,null=True)
    balancer_type = models.CharField(max_length=64,null=True)
    update_time = models.FloatField(null=False)
    upstream_list = models.ManyToManyField(upstream_config)


