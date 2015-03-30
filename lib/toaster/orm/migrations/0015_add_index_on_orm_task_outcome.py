# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.create_index(u'orm_task', ['outcome'])

    def backwards(self, orm):
        db.delete_index(u'orm_task', ['outcome'])

