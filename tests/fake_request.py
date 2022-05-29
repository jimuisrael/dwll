class Session(dict):
   def __init__(self,*arg,**kw):
      super(Session, self).__init__(*arg, **kw)
      self.modified = False

class Request:
    def __init__(self):
        self.session = Session()

request = Request()