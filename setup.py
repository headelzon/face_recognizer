#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [
    'face_recognition_models>=0.2.0',
    'Click>=6.0',
    'dlib>=19.5',
    'numpy',
    'Pillow',
    'scipy>=0.17.0'
]

setup(
    name='face_recognizer_module',
    version='1.0.0',
    description="Recognize faces with Python",
    author="Wiktor Koziak",
    author_email='w.koziak@aol.com',
    packages=[
        'face_recognizer_module',
    ],
    package_dir={'face_recognizer_module': 'face_recognizer_module'},
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)