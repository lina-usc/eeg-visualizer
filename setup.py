# Authors: Christian O'Reilly <christian.oreilly@gmail.com>;
# Scott Huberty <scott.huberty@mail.mcgill.ca>
# License: MIT

from setuptools import setup


if __name__ == "__main__":
    hard_dependencies = ('numpy', 'mne', 'mne-bids','dash')
    install_requires = list()
    with open('requirements.txt', 'r') as fid:
        for line in fid:
            req = line.strip()
            for hard_dep in hard_dependencies:
                if req.startswith(hard_dep):
                    install_requires.append(req)

    setup(
        name='eeg-visualizer',
        version="0.0.1",
        description='EEG/MEG Remote Visualization tools built on mne-python with Dash',
        python_requires='>=3.5',
        author="Scott Huberty",
        author_email='seh33@uw.edu',
        url='https://github.com/scott-huberty/eeg-visualizer.git',
        packages=['eeg-visualizer'],
        install_requires=install_requires)
