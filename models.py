import datetime
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class UserSettings(Model):
    __tablename__ = 'UserSettings'
    id = Column(Integer, primary_key=True)
    # username = Column(String(64), ForeignKey('ab_user.username'), nullable=False)
    # ab_user = relationship('User')
    photoPath = Column(String(256), default='c:\dosc\photos', unique=False, nullable=True)
    lastChange = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)

    def __repr__(self):
        return 'Settings for' + self.username
