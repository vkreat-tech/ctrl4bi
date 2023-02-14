pip install twine --user

set token="pypi-"

python -m twine upload -u __token__ -p %token% --repository pypi dist\ctrl4bi-1.0.5.tar.gz
python -m twine upload -u __token__ -p %token% --repository pypi dist\ctrl4bi-1.0.5-py3-none-any.whl
