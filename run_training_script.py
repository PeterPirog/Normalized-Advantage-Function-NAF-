import os

os.environ["WANDB_API_KEY"] = '1ed2c67731159621d3caad4917cee0c5e21b3c2f'
#os.environ["WANDB_MODE"] = "dryrun"

env='BipedalWalker-v3'  #Name of the environment (default: Pendulum-v0)
info='Experiment-3'     #Name of the Experiment (default: Experiment-1)
frames='40000'          #Number of training frames (default: 40000)
mem='100000'            #Replay buffer size (default: 100000)
batch_size='128'        #Batch size (default: 128)
layer_size='256'        #Neural Network layer size (default: 256)
gamma='0.99'            #Discount factor gamma (default: 0.99)
tau='1e-3'              #Soft update factor tau (default: 1e-3)
learning_rate ='1e-3'   #Learning rate (default: 1e-3)
update_every ='1'       #update the network every x step (default: 1)
n_updates='1'           #update the network for x steps (default: 1)
seed='0'                #random seed (default: 0)
choices='0'             #choices=[0,1] : Use prioritized experience replay (default: 0)
nstep_bootstrapping='1' #nstep_bootstrapping (default: 1)
d2rl='0'                #Using Deep Dense Network if set to 1 (default: 0)
eval_every='1000'       #Doing an evaluation of the current policy every X frames (default: 1000)
eval_runs='3'           #Number of evaluation runs - performance is averaged over all runs (default: 3)

cmd=f'python naf.py ' \
    f'-env {env} ' \
    f'-info {info} ' \
    f'-f {frames} ' \
    f'-mem {mem} ' \
    f'-b {batch_size} ' \
    f'-l {layer_size} ' \
    f'-g {gamma} ' \
    f'-t {tau} ' \
    f'-lr {learning_rate} ' \
    f'-u {update_every} ' \
    f'-n_up {n_updates} ' \
    f'-s {seed} ' \
    f'-per {choices} ' \
    f'-nstep {nstep_bootstrapping} ' \
    f'-d2rl {d2rl} ' \
    f'--eval_every {eval_every} ' \
    f'--eval_runs {eval_runs}'


returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value)
