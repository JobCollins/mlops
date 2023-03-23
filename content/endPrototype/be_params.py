WANDB_PROJECT = "aerial-imagery-mlops"
ENTITY = None # set this to team name if working in a team
BE_CLASSES = {i:c for i,c in enumerate(['Water','Land (unpaved area)', 'Road','Building', 'Vegetation', 'Unlabeled'])}
RAW_DATA_AT = 'big_earth_net'
PROCESSED_DATA_AT = 'big_earth_net_split'