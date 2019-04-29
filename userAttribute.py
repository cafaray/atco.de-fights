class User(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name

    def __getattr__(inst, attr):
        if attr in inst.__dict__:
            return inst.__dict__[attr]
        else:
            return attr + ' attribute is not defined'


def userAttribute(attribute):
    user = User("annymaster", "1234567", "1500", "anny")
    return getattr(user, attribute)
