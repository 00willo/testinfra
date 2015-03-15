# -*- coding: utf8 -*-
# Copyright © 2015 Philippe Pepiot
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import unicode_literals

import threading

from testinfra import backend

__all__ = ["set_backend", "run", "check_output"]

g = threading.local()
g.backend = None
g.sysinfo = None


def run(command, *args, **kwargs):
    if g.backend is None:
        raise RuntimeError("No runner available")
    return g.backend.run(command, *args, **kwargs)


def check_output(command, *args, **kwargs):
    from testinfra.modules.command import Command
    return Command.check_output(command, *args, **kwargs)


def get_system_info():
    if g.sysinfo is None:
        import testinfra.sysinfo
        g.sysinfo = testinfra.sysinfo.get_system_info()
    return g.sysinfo


def set_backend(backend_type, *args, **kwargs):
    g.backend = backend.get_backend(backend_type, *args, **kwargs)
    g.sysinfo = None
