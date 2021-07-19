from sys import maxsize

class Сontact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None, home_phone=None,
                 mob_phone=None, work_phone=None, EMail=None, bday=None, bmonth=None, byear=None, id=None,
                 second_phone=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mob_phone = mob_phone
        self.work_phone = work_phone
        self.second_phone = second_phone
        self.EMail = EMail
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
