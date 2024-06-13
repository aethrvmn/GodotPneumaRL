from glob import glob

import tensorboard_reducer as tbr

from policy import policies

strict_steps=False
overwrite = True
reduce_ops = ("mean", "min", "max")

for policy_name in policies:
    print(f"Calculating {policy_name}")
    
    # Define glob pattern to find the directories
    input_event_dirs = sorted(glob(f"tnsrbrd/sb3/{policy_name}_[0-9]"))
    print(f"Found {input_event_dirs}")
    
    # Define output dir
    events_output_dir = f"tnsrbrd/results/{policy_name}"

    # Load TB events
    events_dict = tbr.load_tb_events(input_event_dirs, strict_steps=False, verbose=True)

    # Get number of steps and other params
    n_scalars = len(events_dict)
    n_steps, n_events = list(events_dict.values())[0].shape

    print(f"Loaded {n_events} TensorBoard runs with {n_scalars} scalars and {n_steps} steps each")
    print(", ".join(events_dict))

    # Reduce events
    reduced_events = tbr.reduce_events(events_dict, reduce_ops, verbose=True)

    for op in reduce_ops:
        print(f"Writing '{op}' reduction to '{events_output_dir}-{op}'")
        
    tbr.write_tb_events(reduced_events, events_output_dir, overwrite)

    print(f"Reduction of {policy_name} done.")
