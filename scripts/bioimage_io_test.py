import os
import hashlib
import imagej
import bioimageio.core
import numpy as np
import xarray as xr
import code

# intialize ImageJ
ij = imagej.init(mode='interactive')
print(f"ImageJ version: {ij.getVersion()}")

# load model from on of the following sources
#  - zenodo doi string
#  - url of the yaml file
#  - a local copy of the model package
rdf_path = ""
model_resource = bioimageio.core.load_resource_description(rdf_path)

# get test image from the loaded model
test_image = xr.DataArray(np.load(model_resource.test_inputs[0]), dims=tuple(model_resource.inputs[0].axes))

# create the prediction pipeline and run a prediction on the test image
prediction_pipeline = bioimageio.core.create_prediction_pipeline(model_resource, devices=None, weight_format=None)
pred_result = bioimageio.core.prediction.predict(prediction_pipeline, test_image)

# combine the prediction results with the input data (test image)
out = pred_result[0]
new_stack = xr.concat([test_image[:, :, :, :], out[:, :, :, :]], dim='c')

# display in ImageJ
ij.ui().show(ij.py.to_dataset(new_stack))

# return REPL
code.interact(local=locals())