from shared import file_manage as fm
from shared.decorater import timer
from shared import argv_manager
from shared.configure import Configuration as conf

from matcher import Matcher

result = None


def main():
    if conf.resource_path is None:
        resources = conf.default_resource_list
    else:
        resources = [conf.resource_path]

    for resource_path in resources:
        print()
        print('----')
        print('start find couples with file {}'.format(resource_path))
        run(fm.read_resource_as_list(resource_path))

        if conf.should_save_result:
            global result
            fm.write_result_as_file(result, resource_path)


@timer
def run(file_lines: list):
    couples = Matcher().get_couples(file_lines)

    global result
    result = ','.join(couples)

    print('Result:')
    print(result)


if __name__ == '__main__':
    argv_manager.set_argument()
    main()
