# Generate masks on jupyter.ewatercycle.org machine

The lisflood notebooks available at
[era5-comparison repository](https://github.com/eWaterCycle/era5-comparison/tree/master/lisflood)
require two files `catchment_masks.nc` and `model_mask.nc`.
To re-generate those files, follow the instruction described below.

## Environment variables

```bash
export LOCAL_DIR=/mnt/data/lorentz-models/lisflood
export SETUP_GLOBAL=Lisflood01degree
export GRDC=$LOCAL_DIR/grdc
```

Please note that the full global setup (`Lisflood01degree`) will not be published.

## Docker image

The docker image lisflood-grpc4bmi is available [on dockerhub](https://hub.docker.com/r/ewatercycle/lisflood-grpc4bmi).

Alternatively, this image can be re-generated using instructions
at [lisflood readme in era5-comparison repository](https://github.com/eWaterCycle/era5-comparison/tree/master/lisflood).

## Create masks

To re-generate mask files, run:

```bash
docker run -ti --user $(id -u) -v $LOCAL_DIR/$SETUP_GLOBAL/maps_netcdf:/maps_netcdf -v $GRDC:/grdc -v $LOCAL_DIR/areamaps:/amaps --entrypoint python3 ewatercycle/lisflood-grpc4bmi:latest /opt/basin_station_processing/catchment.py /maps_netcdf/ldd.nc /opt/recipes_auxiliary_datasets/Lorentz_Basin_Shapefiles /grdc /amaps
```

Output:

- `$LOCAL_DIR/areamaps/catchment_masks.nc` containing a mask for each catchment, used for forcing pre-processing
- `$LOCAL_DIR/areamaps/model_mask.nc` is the union of all catchment masks, used for running LISVAP and LISFLOOD

Given the model river flow direction matrix (`$LOCAL_DIR/$SETUP_GLOBAL/maps_netcdf/ldd.nc`) and [the input basin
shapefiles](https://github.com/eWaterCycle/recipes_auxiliary_datasets/tree/master/Lorentz_Basin_Shapefiles),
each catchment mask is computed as follows:

1. We find the set of model pixels *P* that are within the catchment shapefile polygon;
2. Among *P*, the pixel *p* with the largest upstream (drained) area is selected;
3. The catchment mask consists of all pixels upstream of *p*.
