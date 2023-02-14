pip install -r "requirements.txt" --user
if exist ctrl4bi.egg-info rmdir /s /q ctrl4bi.egg-info
python -m build
pip install --force-reinstall dist\ctrl4bi-1.0.6-py3-none-any.whl
