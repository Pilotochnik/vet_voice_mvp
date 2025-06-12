from sqlalchemy import Column, Integer, String, DateTime
from db import Base
import datetime

class Intake(Base):
    __tablename__ = "intakes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    result_text = Column(String)
    txt_path = Column(String)
    docx_path = Column(String)
