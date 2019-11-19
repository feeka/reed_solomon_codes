import types

import numpy as np
import math
from common.trial import Trial
from math import fabs
from common.extension_field_lut import extension_field
from sympy import *
from dec.rs_prime_decoder import RSPrimeDecoder
class Decoder:
    
    def apply_RS_prime_field_decoder(self,trial):
        trial = trial
        rs_prime_dec = RSPrimeDecoder(trial)
        rs_prime_dec.decode()
        