import numpy as np

# NOTE: Define dict() function


def dict(data):
    return np.array(data)


# NOTE: Define dictType() function


def dictType(data):
    originData = np.array(data)
    return originData.dtype

# NOTE: Define serialize() function


def serialize(data):
    originData = np.array(data)
    # Serialize in binary format
    data_bytes = originData.tobytes()
    return data_bytes

# NOTE: Define deserialize() function


def deserialize(data, type):
    returnData = np.frombuffer(data, dtype=type)
    return returnData
