# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()
from ui.cli import run


if __name__ == '__main__':
    run()
