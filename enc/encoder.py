from common.extension_field_lut import extension_field
from enc.rs_prime_encoder import RSPrimeFieldEncoder
from enc.rs_extension_encoder import RSExtensionFieldEncoder

class Encoder:
    
    def apply_RS_prime_field_encoder(self, rs_trial):
        rs_enc=RSPrimeFieldEncoder(rs_trial)
        rs_enc.encode()

