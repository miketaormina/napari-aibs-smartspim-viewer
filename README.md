# napari-aibs-smartspim-viewer

[![License](https://img.shields.io/pypi/l/napari-aibs-smartspim-viewer.svg?color=green)](https://github.com/miketaormina/napari-aibs-smartspim-viewer/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-aibs-smartspim-viewer.svg?color=green)](https://pypi.org/project/napari-aibs-smartspim-viewer)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-aibs-smartspim-viewer.svg?color=green)](https://python.org)
[![tests](https://github.com/miketaormina/napari-aibs-smartspim-viewer/workflows/tests/badge.svg)](https://github.com/miketaormina/napari-aibs-smartspim-viewer/actions)
[![codecov](https://codecov.io/gh/miketaormina/napari-aibs-smartspim-viewer/branch/main/graph/badge.svg)](https://codecov.io/gh/miketaormina/napari-aibs-smartspim-viewer)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-aibs-smartspim-viewer)](https://napari-hub.org/plugins/napari-aibs-smartspim-viewer)

Load all channels and pyramid levels using available `napari_config.json` file.

To open a data set in a napari viewer, use `File->Open File(s)...` and choose the `napari_config.json` in the experiment folder. This file specifies the channels present and the pyramid levels contained in each. I also makes a guess at assigning color maps and contrast limits.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/index.html
-->

## Installation

<!--
You can install `napari-aibs-smartspim-viewer` via [pip]:~~

    pip install napari-aibs-smartspim-viewer
-->
Create an environment using Python 3.8+:

    conda create -n aibs_ss_viewer python=3.8
    conda activate aibs_ss_viewer

Then clone the repo, navigate to it and pip install:

    cd ~/projects
    git clone https://github.com/miketaormina/napari-aibs-smartspim-viewer.git
    cd napari-aibs-smartspim-viewer.git
    pip install -e .
    




## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-aibs-smartspim-viewer" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
