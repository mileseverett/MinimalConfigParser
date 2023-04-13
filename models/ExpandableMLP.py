import torch.nn as nn
import torch


class ExpandableMLPLM(nn.Module):
    def __init__(
        self,
        input_dim=3072,
        num_classes=10,
        norm=torch.nn.BatchNorm1d,
        activation=torch.nn.ReLU,
        hidden_dims=[780, 780],
        num_blocks=2,
        bias=True,
        strategy=None,
    ):
        super().__init__()

        print("Using ExpandableMLPLM model")
        print(f"Input dimension: {input_dim}")
        print(f"Number of classes: {num_classes}")
        print(f"Normalization: {norm}")
        print(f"Activation: {activation}")
        print(f"Hidden dimensions: {hidden_dims}")
        print(f"Number of blocks: {num_blocks}")
        print(f"Bias: {bias}")
        print(f"Strategy: {strategy}")

        # Your model implementation goes here
        pass

    def forward(self, x):
        # Your forward pass implementation goes here
        pass
