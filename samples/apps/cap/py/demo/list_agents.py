import time
from typing import List

from AppAgents import FidelityAgent, GreeterAgent
from autogencap.DebugLog import Info
from autogencap.ComponentEnsemble import ComponentEnsemble
from autogencap.proto.CAP_pb2 import ActorInfo


def list_agents():
    """
    Demonstrates the usage of the CAP platform by registering an actor, connecting to the actor,
    sending a message, and performing cleanup operations.
    """
    # CAP Platform

    ensemble = ComponentEnsemble()
    # Register an actor
    ensemble.register(GreeterAgent())
    # Register an actor
    ensemble.register(FidelityAgent())
    # Tell actor to connect to other actors
    ensemble.connect()
    # Get a list of actors
    actor_infos: List[ActorInfo] = ensemble.find_by_name_regex(name_regex=".*")
    # Print out all actors found
    Info("list_agents", f"{len(actor_infos)} actors found:")
    for actor_info in actor_infos:
        Info(
            "list_agents",
            f"Name: {actor_info.name}, Namespace: {actor_info.namespace}, Description: {actor_info.description}",
        )
    # Cleanup
    ensemble.disconnect()
