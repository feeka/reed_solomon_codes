#from dec.rs_prime_decoder import RSPrimeDecoder
from common.rs_trial import RSTrial
from common.prime_field import prime_field
from enc.encoder import Encoder
from common.channel import Channel
from dec.decoder import Decoder
import copy
#from dec.decoder import Decoder
def next_move(word):
    print("\t\t|")
    print("\t\tV")
    print("----------------------------------------------------------------")
    input("|\t\t"+word)


def report_welcome(rs_trial):
    print("___________________________________\nWELCOME TO A LITTLE DEMO!","\nOur initial setup is:\n"+"---------------------------------------------\n"+
        "message is: ",rs_trial.message,"\n"+
        "locators: ",rs_trial.locators,"\n"+
        "multipliers: ",rs_trial.multipliers,"\n---------------------------------------------\n")

def report_after_encoding(rs_trial):
    print("|codeword:",rs_trial.word,"\n------------------------------------------------------------")
def report_after_channel(rs_trial):
    print(
        "|message after channel: ",rs_trial.message,"\n"+
       "|modified word:",rs_trial.word,
       "\n---------------------------------------------------------\n"
          )


def report_after_decoding(rs_trial):
    print(
        "|message estimate is: ",rs_trial.message,"\n","----------------------------------------------------------")
#initial setup
#--------------------------------------------------------------------------------------------------------------------
gf11=prime_field(11) #prime field 11
locators = [1,2,3,4,5,6,7,8,9,10] #locators
multipliers =  [1,1,1,1,1,1,1,1,1,1] #multipliers
k=5 # msg length
n=10 #code length
message = [3,5,3,4,1] #message

rs_trial_one = RSTrial(gf11,k,n,locators,multipliers,message=message)
#-----------------------------------------------------------------------
report_welcome(rs_trial_one)


#instantiation of generic classes 
#---------------------------------
encoder = Encoder()
channel = Channel()
decoder = Decoder()
#---------------------------------

next_move("ENCODER")
encoder.apply_RS_prime_field_encoder(rs_trial_one)
report_after_encoding(rs_trial_one)

next_move("CHANNEL")
channel.apply_DMC_channel(rs_trial_one,0.2)
report_after_channel(rs_trial_one)

next_move("DECODE")
decoder.apply_RS_prime_field_decoder(rs_trial_one)
report_after_decoding(rs_trial_one)
