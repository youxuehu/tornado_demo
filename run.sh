rm -rf build
rm -rf dist
python setup.py bdist_wheel --universal
cd dist
pip uninstall -y tornado_demo
pip install tornado_demo-20211128-py2.py3-none-any.whl
tornado_start