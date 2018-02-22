import recurly
import os
import vcr

recurly.SUBDOMAIN = os.environ.get('RECURLY_SUBDOMAIN')
recurly.API_KEY = os.environ.get('RECURLY_API_KEY')

with vcr.use_cassette('vcr_cassette.yaml'):
  account = recurly.Account.get('blahblahblah')

print account
