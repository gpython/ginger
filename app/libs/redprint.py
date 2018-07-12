#encoding:utf-8

class Redprint:
  def __init__(self, name):
    self.name = name
    self.mound = []

  def route(self, rule, **options):
    def decorator(f):
      self.mound.append((f, rule, options))
      print(f.__name__)
      return f
    return decorator

  def register(self, bp, url_prefix=None):
    for f, rule, options in self.mound:
      endpoint = options.pop('endpoint', f.__name__)
      bp.add_url_rule(url_prefix+rule, endpoint, f, **options)