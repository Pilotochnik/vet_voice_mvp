from db import SessionLocal
from models import Intake
from sqlalchemy import select

async def save_intake(user_id, result_text, txt_path, docx_path):
    async with SessionLocal() as session:
        intake = Intake(
            user_id=user_id,
            result_text=result_text,
            txt_path=txt_path,
            docx_path=docx_path
        )
        session.add(intake)
        await session.commit()

async def get_user_intakes(user_id):
    async with SessionLocal() as session:
        result = await session.execute(
            select(Intake).where(Intake.user_id == user_id)
        )
        return result.scalars().all()

async def get_intake_by_id(intake_id):
    async with SessionLocal() as session:
        result = await session.execute(
            select(Intake).where(Intake.id == intake_id)
        )
        return result.scalar_one_or_none()
