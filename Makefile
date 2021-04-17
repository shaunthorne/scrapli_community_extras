lint:
	python -m isort .
	python -m black .
	python -m pylama .
	python -m pydocstyle .
	python -m mypy --strict scrapli_community/

darglint:
	find scrapli_cfg -type f \( -iname "*.py"\) | xargs darglint -x

test:
	python -m pytest \
	tests/

cov:
	python -m pytest \
	--cov=scrapli_community \
	--cov-report html \
	--cov-report term \
	tests/

test_unit:
	python -m pytest \
	--cov=scrapli_community \
	--cov-report html \
	--cov-report term \
	tests/unit/

cov_unit:
	python -m pytest \
	--cov=scrapli_community \
	--cov-report html \
	--cov-report term \
	tests/unit/

.PHONY: docs
docs:
	python docs/generate/generate_docs.py

deploy_docs:
	mkdocs gh-deploy
