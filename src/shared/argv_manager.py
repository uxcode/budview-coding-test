import os
import sys

from shared.configure import Configuration as conf


def set_argument():
    _categorize_arguments()
    _set_resource_dir()
    _set_default_resource_list()


def _categorize_arguments():
    for arg in sys.argv[1:]:
        if arg == '--save-result':
            conf.should_save_result = True
        elif arg[:1] != '-':
            conf.resource_path = arg


def _set_resource_dir():
    conf.script_dir = '/'.join(os.path.realpath(__file__).split('/')[:-2]) + '/'
    conf.resource_dir = conf.script_dir + 'resources/'


def _set_default_resource_list():
    for i, default_resource_name in enumerate(conf.default_resource_list):
        conf.default_resource_list[i] = conf.resource_dir + default_resource_name
