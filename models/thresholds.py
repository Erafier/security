from sqlalchemy import String, Column, Integer

# from ...shared.db_manager import Base
# from ...shared.models.abstract_base import AbstractBaseMixin
from tools import db_tools, db


class SecurityThresholds(db_tools.AbstractBaseMixin, db.Base):
    __tablename__ = "sec_thresholds"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, unique=False, nullable=False)
    test_name = Column(String, unique=False, nullable=False)
    test_uid = Column(String, unique=False, nullable=False)
    critical = Column(Integer, unique=False, nullable=False)
    high = Column(Integer, unique=False, nullable=False)
    medium = Column(Integer, unique=False, nullable=False)
    low = Column(Integer, unique=False, nullable=False)
    info = Column(Integer, unique=False, nullable=False)
    critical_life = Column(Integer, unique=False, nullable=False)
    high_life = Column(Integer, unique=False, nullable=False)
    medium_life = Column(Integer, unique=False, nullable=False)
    low_life = Column(Integer, unique=False, nullable=False)
    info_life = Column(Integer, unique=False, nullable=False)
