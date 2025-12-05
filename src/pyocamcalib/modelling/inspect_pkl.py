import pickle
import numpy


with open('/Users/ellag/Library/CloudStorage/GoogleDrive-elhe2720@colorado.edu/Shared drives/Field Research Videos/Gil Lab/Curacao_2024/garden_eels/position_drop_experiment/triangulation_frames/GH040005_trial2_cam1_synced/detections_mycam_04122025_210024.pickle' , "rb") as f:
    data = pickle.load(f)

print("Type:", type(data))

if isinstance(data, dict):
    print("Keys:", data.keys())
else:
    print("Data:", data)

name = "/Users/ellag/Library/CloudStorage/GoogleDrive-elhe2720@colorado.edu/Shared drives/Field Research Videos/Gil Lab/Curacao_2024/garden_eels/position_drop_experiment/triangulation_frames/GH040005_trial2_cam1_synced/img_0014.jpg"
print(data[name])