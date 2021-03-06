# -*- coding: utf-8 -*-
# This file is part of Shoop.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from shoop.utils.excs import Problem


class ImmutabilityError(ValueError):
    pass


class NoProductsToShipException(Exception):
    pass


class NoPaymentToCreateException(Exception):
    pass


class ProductNotOrderableProblem(Problem):
    pass


class ProductNotVisibleProblem(Problem):
    pass


class ImpossibleProductModeException(ValueError):
    def __init__(self, message, code=None):
        super(ImpossibleProductModeException, self).__init__(message)
        self.code = code
