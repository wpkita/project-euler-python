import argparse
import shutil
import fileinput

# Configure and read command line arguments
parser = argparse.ArgumentParser(description='Scaffold out directory/file structure for new Project Euler problem.')
parser.add_argument('problem_number', type=int)
args = parser.parse_args()

if __name__ == '__main__':
    problem_number = args.problem_number

    # e.g. 6 becomes 'p006'
    problem_label = 'p{0:03d}'.format(problem_number)

    # Copy template files into p### directory
    shutil.copytree('problem_template', '{0}'.format(problem_label))

    # Move tests file into tests directory, rename as p###_tests.py
    tests_file_name = 'tests/{0}_tests.py'.format(problem_label)
    shutil.move('{0}/tests.py'.format(problem_label), tests_file_name)

    # Fix reference in tests file to point to p### package
    for line in fileinput.input(tests_file_name, inplace=True):
        print(line.replace('problem_template', problem_label), end='')
