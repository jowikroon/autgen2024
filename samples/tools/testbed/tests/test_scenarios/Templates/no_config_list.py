import os
import json
import testbed_utils
import autogen

testbed_utils.init()
##############################

work_dir = "coding"

# Read the prompt
PROMPT = "__PROMPT__"

config_list = None
assistant = autogen.AssistantAgent(
    "assistant",
    is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    llm_config=testbed_utils.default_llm_config(config_list, timeout=180),
)
user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    code_execution_config={
        "work_dir": work_dir,
        "use_docker": False,
    },
    max_consecutive_auto_reply=10,
    default_auto_reply="TERMINATE",
)

user_proxy.initiate_chat(
    assistant,
    message=PROMPT,
)

##############################
testbed_utils.finalize(agents=[assistant, user_proxy])
