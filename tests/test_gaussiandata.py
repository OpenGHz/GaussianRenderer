import torch

from gaussian_renderer import GaussianData


def test_gaussian_data_init():
    xyz = torch.randn(10, 3)
    rot = torch.randn(10, 4)
    scale = torch.randn(10, 3)
    opacity = torch.randn(10)
    sh = torch.randn(10, 16, 3)

    gd = GaussianData(xyz, rot, scale, opacity, sh)

    assert len(gd) == 10
    assert gd.xyz.shape == (10, 3)
    assert gd.rot.shape == (10, 4)


def test_gaussian_data_device():
    xyz = torch.randn(5, 3)
    rot = torch.randn(5, 4)
    scale = torch.randn(5, 3)
    opacity = torch.randn(5)
    sh = torch.randn(5, 16, 3)

    gd = GaussianData(xyz, rot, scale, opacity, sh)
    assert gd.device == xyz.device
