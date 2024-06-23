run:
	@uvicorn workout_api.main:app --reload
create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revison --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head