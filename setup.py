from glob import glob
from setuptools import setup, find_packages
from os.path import basename
from os.path import splitext

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='LalaTools', # 패키지 명
    version='0.0.11',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    description='0.0.11 : add long description',
    author='LalaUser789',
    author_email='aa01092308481@gmail.com',
    #url='none',
    license='MIT', # MIT에서 정한 표준 라이센스 따른다
    py_modules=[splitext(basename(path))[0] for path in glob('lalatools/*.py')], # 패키지에 포함되는 모듈
    python_requires='>=3',
    install_requires=_requires_from_file('requirements.txt'),
    packages=find_packages(
        include=["lalatools",'lalatools*']
        ),# 패키지가 들어있는 폴더들
)

# 버전 수정
# rmdir build
# python setup.py bdist_wheel
# twine upload dist/LalaTools-0.0.11-py3-none-any.whl