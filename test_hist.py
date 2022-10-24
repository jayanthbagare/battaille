#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PIL
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
matplotlib.use( 'tkagg' )

x = np.random.normal(180,10,250)

plt.hist(x)
plt.show()
