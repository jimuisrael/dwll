class Session(dict):
   def __init__(self,*arg,**kw):
      super(Session, self).__init__(*arg, **kw)
      self.modified = False

class User:
    def __init__(self):
        self.username = 'admin'

class Request:
    def __init__(self):
        self.session = Session()
        self.user = User()

request = Request()