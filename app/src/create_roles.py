import asyncio
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config.virt_env_db import DB_HOST, DB_NAME, DB_PASS, DB_USER, DB_PORT
from internal.database.models import Role

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session():
    async with async_session_maker() as session:
        yield session

async def create_roles(session):
    roles_to_create = [
        Role(status='user', permissions=''),
        Role(status='admin', permissions=''),
    ]
    for role in roles_to_create:
        existing_role = await session.execute(
            Role.__table__.select().where(Role.status == role.status)
        )
        if existing_role.scalar() is None:
            session.add(role)
    await session.commit()

async def main():
    async with async_session_maker() as session:
        await create_roles(session)
    print('Role setup completed')

if __name__ == '__main__':
    asyncio.run(main())