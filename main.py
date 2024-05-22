from policy import policies
from agent import main
import args

for policy_name, policy in policies.items():
    if policy_name in ["policy_big_tanh", "policy_big_optim_tanh"]:
        print(policy_name)
        main(policy_name=policy_name, policy=policy, parseargs=args.parse_args())
