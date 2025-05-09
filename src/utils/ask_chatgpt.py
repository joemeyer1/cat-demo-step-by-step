
from src.environments.environment import Environment


def is_appropriate(behavior: float, environment: Environment) -> bool:
    """Ask almighty ChatGPT, oracle of all moral validity, whether behavior is appropriate for the given environment."""

    return environment.is_ok(behavior)
