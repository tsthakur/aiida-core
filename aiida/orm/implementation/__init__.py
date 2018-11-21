# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida_core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from aiida.backends.settings import BACKEND
from aiida.common.exceptions import ConfigurationError
from aiida.backends.profile import BACKEND_DJANGO, BACKEND_SQLA

from .authinfos import *
from .backends import *
from .computers import *
from .logs import *
from .querybuilder import *
from .groups import *
from .users import *

_local = 'Node', 'Workflow', 'kill_all', 'get_all_running_steps', 'get_workflow_info', 'delete_code', 'Comment',

__all__ = (_local +
           computers.__all__ +
           logs.__all__ +
           users.__all__ +
           authinfos.__all__ +
           backends.__all__ +
           querybuilder.__all__ +
           groups.__all__)

if BACKEND == BACKEND_SQLA:
    from aiida.orm.implementation.sqlalchemy.node import Node
    from aiida.orm.implementation.sqlalchemy.workflow import Workflow, kill_all, get_workflow_info, \
        get_all_running_steps
    from aiida.orm.implementation.sqlalchemy.code import delete_code
    from aiida.orm.implementation.sqlalchemy.comment import Comment
elif BACKEND == BACKEND_DJANGO:
    from aiida.orm.implementation.django.node import Node
    from aiida.orm.implementation.django.workflow import Workflow, kill_all, get_workflow_info, get_all_running_steps
    from aiida.orm.implementation.django.code import delete_code
    from aiida.orm.implementation.django.comment import Comment
elif BACKEND is None:
    raise ConfigurationError("settings.BACKEND has not been set.\n"
                             "Hint: Have you called aiida.load_dbenv?")
else:
    raise ConfigurationError("Unknown settings.BACKEND: {}".format(
        BACKEND))
