# USED IN MAIN.PY
# ---------------
# memory info
MEMORY_SIZE = 64
PAGE_SIZE = FRAME_SIZE = 4

WORK_TIME = 1000

# -----------------
# USED IN KERNEL.PY
# -----------------
# if random algorithm
RAND = False
# run delay
DELAY = 0


# accesses in processes
MIN_ACCESSES = 8
MAX_ACCESSES = 20

# limit of active processes
MAX_PROCS = 4

# replacement interval
REPLACE_INTERVAL = 8
# reset "R" interval
RESET_INTERVAL = 4

# DELTA for WSClock algorithm
DELTA = 20

# interval of spawning new process attempt
SPAWN_INTERVAL = 8
# chance to spawn new process
SPAWN_CHANCE = 0.9

# size of time quantum
QUANTUM_SIZE = 4

# ---------------
# USED IN PROCESS
# ---------------
# interval of ws update
WS_UPD_INTERVAL = 10

# Number of ws entries
WS_ENTRIES = 3

# --------------------------------
# USED IN OPT.FUNC.GENERATE_ACCESS
# --------------------------------
# chance of access to working set
CHANCE_LOCAL = 0.9

# read/write weights
READ_WEIGHT = 0.7
WRITE_WEIGHT = 0.3
