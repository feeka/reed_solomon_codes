from textx import get_children_of_type
from textx import metamodel_from_file
from common.rs_trial import RSTrial
from common.prime_field import prime_field
from enc.encoder import Encoder
from common.channel import Channel
from dec.decoder import Decoder

encoder = Encoder()
channel = Channel()
decoder = Decoder()

def initial_setup(field,locators,multipliers,k,n,message):
    gfk=prime_field(field) #prime field field
    rs_trial_one = RSTrial(gfk,k,n,locators,multipliers,message=message)
    return rs_trial_one

grammar_file = "grammar.tx"
mm = metamodel_from_file(grammar_file)

model_str = "test_mod.ecc"

model = mm.model_from_file("test_mod.ecc")

def cname(o):
    return o.__class__.__name__


trial = None
for command in model.commands:
    #print(cname(command))
    if cname(command) == 'TrialCreate':
        print("______________________\nNEW TRANSACTION STARTED\nSuccessfully CREATED the trial\n----------------")
        trial = initial_setup(command.field,command.locators,command.multipliers,command.k,command.n,command.message)

    elif command == 'encode':
        encoder.apply_RS_prime_field_encoder(trial)
        print("Successfully ENCODED the trial")
        print("Codeword is: ",trial.word)
        print("-------------------")
    elif command == 'distort':
        channel.apply_DMC_channel(trial,0.2)
        print("Successfully DISTORTED the trial")
        print("Message: ", trial.message)
        print("-------------------")
    elif command == 'decode':
        decoder.apply_RS_prime_field_decoder(trial)
        print("Successfully DECODED the trial")
        print("Message: ", trial.message)
        print("-------------------")

