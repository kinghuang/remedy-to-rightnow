#!/usr/bin/env python
# coding=utf-8

""" Migration script to move Remedy incidents to RightNow for ISC

Copies specified incidents from Remedy ARS to RightNow for the
Integrated Service Centre go-live.
"""

from suds.client import Client


class R2R(object):

	def __init__(self):
		super(R2R, self).__init__()

	def run(self):
		self.main()

	def main(self):
		print 'R2R'


if __name__ == '__main__':
	R2R().run()