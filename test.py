from myFunctions import *
inputData = [1.3, '22', 3, 4, 5, 6]

# Print original data
print("Original data:", inputData)
inputDataType = dictType(inputData)
print("Original data type:", inputDataType)

# Serialize in binary format
inputData_bytes = serialize(inputData)
print("Serialized data:", inputData_bytes)

# Deserialize
resultData = deserialize(inputData_bytes, inputDataType)
print("After loading, content of the text file:", resultData)

# Check if the original data equal to deserialized data
print("is Equal:", np.array_equal(inputData, resultData))
