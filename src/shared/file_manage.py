import os


def read_resource_as_list(file_path: str) -> list:
    file = open(file_path, 'r')
    file_lines = file.readlines()
    file.close()
    return file_lines


def write_result_as_file(result: str, resource_path):
    file_path = _get_result_file_name(resource_path)
    file = open(file_path, 'w')
    file.write(result)
    file.close()


def _get_result_file_name(resource: str) -> str:
    curr_dir = os.path.realpath(__file__).split('/')[:-3]
    file_name = resource.split('/')[-1]
    return '{}/result-{}'.format('/'.join(curr_dir), file_name)
