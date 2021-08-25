from sys import maxsize

class Project:
    def __init__(self, id=None, project_name=None, status=None, categories=None, view_status=None, description=None):
        self.project_name = project_name
        self.status = status
        self.categories = categories
        self.view_status = view_status
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.project_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.project_name == other.project_name

    def project_name(self):
        if self.project_name:
            return self.project_name

    def id_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize