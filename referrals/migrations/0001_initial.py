# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table('referrals_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('referrals', ['Country'])

        # Adding model 'Industry'
        db.create_table('referrals_industry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('entity_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('referrals', ['Industry'])

        # Adding model 'EntityContact'
        db.create_table('referrals_entitycontact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('referrals', ['EntityContact'])

        # Adding model 'EntityReferral'
        db.create_table('referrals_entityreferral', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('referrer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='referrer', to=orm['auth.User'])),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entity_referred', to=orm['auth.User'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['referrals.Department'], null=True, blank=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('entity_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('referrals', ['EntityReferral'])

        # Adding M2M table for field referred on 'EntityReferral'
        m2m_table_name = db.shorten_name('referrals_entityreferral_referred')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entityreferral', models.ForeignKey(orm['referrals.entityreferral'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['entityreferral_id', 'user_id'])

        # Adding model 'ReferrerPoints'
        db.create_table('referrals_referrerpoints', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('referrer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='points_referrer', to=orm['auth.User'])),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='points_org', to=orm['auth.User'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('entity_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('referrals', ['ReferrerPoints'])

        # Adding model 'EntityPlan'
        db.create_table('referrals_entityplan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plan_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('plan_description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('max_referrals_allowed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num_referrals_for_gift', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('direct_referal_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('indirect_referral_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('unlimited_referrals', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_add_entity', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_use_social_media', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entity_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('referrals', ['EntityPlan'])

        # Adding model 'Department'
        db.create_table('referrals_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('referrals', ['Department'])

        # Adding model 'EntityProfile'
        db.create_table('referrals_entityprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['referrals.EntityPlan'], null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['referrals.Industry'], null=True, blank=True)),
            ('entity_contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['referrals.EntityContact'])),
            ('referrals_made', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('inherit_from_plan', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('business_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('num_referrals_for_gift', self.gf('django.db.models.fields.IntegerField')(default=10, null=True, blank=True)),
            ('direct_referal_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('indirect_referral_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['referrals.Country'])),
            ('post_to_facebook', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('post_to_twitter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('entity_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('referrals', ['EntityProfile'])

        # Adding M2M table for field departments on 'EntityProfile'
        m2m_table_name = db.shorten_name('referrals_entityprofile_departments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entityprofile', models.ForeignKey(orm['referrals.entityprofile'], null=False)),
            ('department', models.ForeignKey(orm['referrals.department'], null=False))
        ))
        db.create_unique(m2m_table_name, ['entityprofile_id', 'department_id'])

        # Adding model 'FacebookPostMessage'
        db.create_table('referrals_facebookpostmessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['social_auth.UserSocialAuth'], unique=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('referrals', ['FacebookPostMessage'])

        # Adding model 'TwitterPostMessage'
        db.create_table('referrals_twitterpostmessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['social_auth.UserSocialAuth'], unique=True)),
            ('tweet', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal('referrals', ['TwitterPostMessage'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table('referrals_country')

        # Deleting model 'Industry'
        db.delete_table('referrals_industry')

        # Deleting model 'EntityContact'
        db.delete_table('referrals_entitycontact')

        # Deleting model 'EntityReferral'
        db.delete_table('referrals_entityreferral')

        # Removing M2M table for field referred on 'EntityReferral'
        db.delete_table(db.shorten_name('referrals_entityreferral_referred'))

        # Deleting model 'ReferrerPoints'
        db.delete_table('referrals_referrerpoints')

        # Deleting model 'EntityPlan'
        db.delete_table('referrals_entityplan')

        # Deleting model 'Department'
        db.delete_table('referrals_department')

        # Deleting model 'EntityProfile'
        db.delete_table('referrals_entityprofile')

        # Removing M2M table for field departments on 'EntityProfile'
        db.delete_table(db.shorten_name('referrals_entityprofile_departments'))

        # Deleting model 'FacebookPostMessage'
        db.delete_table('referrals_facebookpostmessage')

        # Deleting model 'TwitterPostMessage'
        db.delete_table('referrals_twitterpostmessage')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'referrals.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'referrals.department': {
            'Meta': {'ordering': "['department']", 'object_name': 'Department'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'referrals.entitycontact': {
            'Meta': {'object_name': 'EntityContact'},
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'referrals.entityplan': {
            'Meta': {'object_name': 'EntityPlan'},
            'can_add_entity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_use_social_media': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'direct_referal_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'entity_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirect_referral_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'max_referrals_allowed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_referrals_for_gift': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'plan_description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'plan_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'unlimited_referrals': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'referrals.entityprofile': {
            'Meta': {'object_name': 'EntityProfile'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['referrals.Country']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {}),
            'departments': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['referrals.Department']", 'null': 'True', 'blank': 'True'}),
            'direct_referal_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'entity_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'entity_contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['referrals.EntityContact']"}),
            'entity_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirect_referral_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['referrals.Industry']", 'null': 'True', 'blank': 'True'}),
            'inherit_from_plan': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'num_referrals_for_gift': ('django.db.models.fields.IntegerField', [], {'default': '10', 'null': 'True', 'blank': 'True'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['referrals.EntityPlan']", 'null': 'True', 'blank': 'True'}),
            'post_to_facebook': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'post_to_twitter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'referrals_made': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'referrals.entityreferral': {
            'Meta': {'object_name': 'EntityReferral'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['referrals.Department']", 'null': 'True', 'blank': 'True'}),
            'entity_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_referred'", 'to': "orm['auth.User']"}),
            'referred': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'referred'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'referrer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referrer'", 'to': "orm['auth.User']"}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'referrals.facebookpostmessage': {
            'Meta': {'object_name': 'FacebookPostMessage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['social_auth.UserSocialAuth']", 'unique': 'True'})
        },
        'referrals.industry': {
            'Meta': {'object_name': 'Industry'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'entity_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'referrals.referrerpoints': {
            'Meta': {'object_name': 'ReferrerPoints'},
            'entity_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'points_org'", 'to': "orm['auth.User']"}),
            'referrer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'points_referrer'", 'to': "orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'referrals.twitterpostmessage': {
            'Meta': {'object_name': 'TwitterPostMessage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tweet': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['social_auth.UserSocialAuth']", 'unique': 'True'})
        },
        'social_auth.usersocialauth': {
            'Meta': {'unique_together': "(('provider', 'uid'),)", 'object_name': 'UserSocialAuth'},
            'extra_data': ('social_auth.fields.JSONField', [], {'default': "'{}'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'social_auth'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['referrals']