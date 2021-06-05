from sqlalchemy import Column as SQLColumn
from sqlalchemy import Integer as SQLInteger
from sqlalchemy import String as SQLString

from pathseeker.src.flask_app.app_factory import DATABASE


class Trait(DATABASE.Model):
    guid = SQLColumn(SQLInteger, primary_key=True)
    name = SQLColumn(SQLString(80), unique=True, nullable=False)
    type = SQLColumn(SQLString(80), unique=False, nullable=True)

    def __str__(self) -> str:
        return f"<{Trait.__name__} {self.name}>"

    def __repr__(self) -> str:
        return f"<{Trait.__name__} name:{self.name}, type:{self.type}>"
