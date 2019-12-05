# RS- encoder/ and decoder on python

This is github repo for RS codes API. Documentation and description of API is provided in documentation.pdf document. 

## Getting Started

First we make sure that everything is installed on a local PC of developer/user. 

### Installtion of necessary python-wise tools

If you’re using some version of Ubuntu (e.g. the latest LTS release), we recommend using the deadsnakes PPA to install Python 3.6:
```
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6

```
### Usage of python 3

At this point, you may have system Python 2.7 available as well.

```python```
This will launch the Python 2 interpreter, WHICH WE DON't NEED.

```python3```
This will launch the Python 3 interpreter. WE NEED THIS ONE.


#### pip and pip3 installation

Except for python3 you will need to install ```pip3```, so first and foremost we must check whether it is already installed. Open terminal and type: 
```pip3 -V```

2 outcomes are possible:
 
 -> Either there will be pip3 installed and terminal will tell you the version ( something like: pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6) )
 
 -> Or there will be no pip3 installed and terminal will write something like: pip3 command not found

If there is no pip3 installed, do following:

Run the following command from a terminal:
```sudo apt-get install python3-pip```

Done.

## numpy and sympy installation

Run the following command from a terminal in order to install ```numpy```:
```pip3 install numpy```

Run the following command from a terminal in order to install ```sympy```:
```pip3 install sympy```

Done.

## Running example with teabag API
In order to execute the transmission first instantiate the field, using ```ExtensionField``` or ```PrimeField```. Example:

```
from common.prime_field import prime_field
gf11=prime_field(11) #prime field with p=11
```

Then use so-called ```trial``` - which imitates the transmission. 
For example in case of Reed-Solomon Codes you have to create instance of ```RSTrial```, constructor of which takes following parameters: `n`,`k`,`field`,`locators`,`multipliers`,`message` prior to encoding(pls note if you just want use decoder or channel you have to pass the parameters to constructor). Example:

```
from common.rs_trial import RSTrial
locators = [1,2,3,4,5,6,7,8,9,10] #locators
multipliers =  [1,1,1,1,1,1,1,1,1,1] #multipliers
k=5 # msg length
n=10 #code length
message = [3,5,3,4,1] #message
rs_trial_one = RSTrial(gf11,k,n,locators,multipliers,message=message)
```
After trial is created, we proceed to encoder. Simply instantiate the generic plugin system and use one of the builder methods. Example:
 
```
from enc.encoder import Encoder
encoder = Encoder()
encoder.apply_RS_prime_field_encoder(rs_trial_one)
```
We proceed to channel and decoder using the same principle as we used for encoder. 
```
from common.channel import Channel
from dec.decoder import Decoder

channel = Channel()
decoder = Decoder()

channel.apply_DMC_channel(rs_trial_one,0.2)
decoder.apply_RS_prime_field_decoder(rs_trial_one)

```
Since the procedure happens by-pass-by-reference it is recommended to keep track of the trial. Pass-by-reference strategy was used for efficiency and simplicity of the library. Note that library still needs improvements.
