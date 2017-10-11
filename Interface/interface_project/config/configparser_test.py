import configparser
import codecs
cp = configparser.SafeConfigParser()
with codecs.open('logconfig.conf', 'r', encoding='utf-8') as f:
    cp.readfp(f)
print 'all sections:', cp.sections()
print 'items of [ssh]:', cp.items('LOGGING')