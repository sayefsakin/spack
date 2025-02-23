# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoruta(RPackage):
    """Wrapper Algorithm for All Relevant Feature Selection.

    An all relevant feature selection wrapper algorithm. It finds relevant
    features by comparing original attributes' importance with importance
    achievable at random, estimated using their permuted copies (shadows)."""

    cran = "Boruta"

    version('7.0.0', sha256='6ff520d27d68637058c33a34c547a656bb44d5e351b7cc7afed6cd4216275c78')
    version('6.0.0', sha256='1c9a7aabe09f040e147f6c614f5fe1d0b951d3b0f0024161fbb4c31da8fae8de')

    depends_on('r-ranger', type=('build', 'run'))
