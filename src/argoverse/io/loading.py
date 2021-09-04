"""I/O for manipulating the Argoverse 2.0 dataset."""
from pathlib import Path
from typing import Optional, Tuple
import numpy as np
import pandas as pd


def load_calibration(fpath: Path, columns: Optional[Tuple[str, ...]] = None) -> pd.DataFrame:
    """Loads the calibration metadata for the Argoverse 2.0 sensor dataset.

    Schema/DataType:
        Sensor name
        Focal Length (x): np.float64
        Focal Length (y): np.float64
        Focal Center (x): np.float64
        Focal Center (y): np.float64
        Skew (s): np.float64
        Sensor Width (width): np.uint16
        Sensor Height (height): np.uin16
        Translation (tx): np.float64
        Translation (ty): np.float64
        Translation (tz): np.float64
        Quaternion coefficient (qw): np.float64
        Quaternion coefficient (qx): np.float64
        Quaternion coefficient (qy): np.float64
        Quaternion coefficient (qz): np.float64

    Args:
        fpath (Path): [description]
        columns (Optional[Tuple[str, ...]]): [description]

    Returns:
        pd.DataFrame: (N,15) Dataframe of calibration metadata.
    """
    calibration = pd.read_feather(fpath)
    return calibration


def load_labels(fpath: Path, columns: Optional[Tuple[str, ...]] = None) -> pd.DataFrame:
    """Loads the track labels for the Argoverse 2.0 sensor dataset.

    The Argoverse 2.0 track labels consist of 3D cuboids with 6-DOF pose.

    Schema/DataType:
        Translation (tx): np.float64
        Translation (ty): np.float64
        Translation (tz): np.float64
        Quaternion coefficient (qw): np.float64
        Quaternion coefficient (qx): np.float64
        Quaternion coefficient (qy): np.float64
        Quaternion coefficient (qz): np.float64
        Time of Validity (tov): np.int64

    Args:
        fpath (Path): Source file path.
        columns (Optional[Tuple[str, ...]]): DataFrame columns to load.

    Returns:
        pd.DataFrame: (N,13) Dataframe of .
    """
    labels = pd.read_feather(fpath)
    return labels


def load_lidar(fpath: Path, columns: Optional[Tuple[str, ...]] = None) -> pd.DataFrame:
    """[summary]

    Schema/DataType:
        X-Coordinate (x): np.float16
        Y-Coordinate (y): np.float16
        Z-Coordinate (z): np.float16
        Intensity (i): np.uint8
        Sensor (s): np.uint8
        Time of Validity (tov): np.int64

    Args:
        fpath (Path): [description]
        columns (Optional[Tuple[str, ...]], optional): [description]. Defaults to None.

    Returns:
        pd.DataFrame: [description]
    """
    lidar = pd.read_feather(fpath)
    return lidar


def load_poses(fpath: Path, columns: Optional[Tuple[str, ...]] = None) -> pd.DataFrame:
    """[summary]

    Schema/DataType:
        Translation (tx): np.float64
        Translation (ty): np.float64
        Translation (tz): np.float64
        Quaternion coefficient (qw): np.float64
        Quaternion coefficient (qx): np.float64
        Quaternion coefficient (qy): np.float64
        Quaternion coefficient (qz): np.float64
        Time of Validity (tov): np.int64

    Args:
        fpath (Path): [description]
        columns (Optional[Tuple[str, ...]], optional): [description]. Defaults to None.

    Returns:
        pd.DataFrame: [description]
    """
    poses = pd.read_feather(fpath)
    return poses