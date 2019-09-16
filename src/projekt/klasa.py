# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:06:01 2019

@author: Ola
"""
from sklearn import manifold, datasets
class Funkcja:
    def fun(data, n):
        mds=manifold.mds.MDS(n_components=2, max_iter=n)
        return mds.fit_transform(data)
    