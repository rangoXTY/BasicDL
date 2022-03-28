import torch


class BaseModel:
    """Base model."""

    def __init__(self, opt) -> None:
        self.opt = opt
        self.device = torch.device("cuda" if opt["num_gpu"] != 0 else "cpu")
        self.is_train = opt["is_train"]
        self.schedulers = []
        self.optimizers = []

    def feed_data(self, data):
        pass

    def optimize_parameters(self):
        pass

    def get_current_visuals(self):
        pass

    def save(self, epoch, current_iter):
        """Save networks and training state."""
        pass
