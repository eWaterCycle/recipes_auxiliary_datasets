# Generate masks on jupyter.ewatercycle.org machine

The lisflood notebooks available at
[era5-comparison repository](https://github.com/eWaterCycle/era5-comparison/tree/master/lisflood)
require two mask files `catchment_masks.nc` and `model_mask.nc`, and a lookup table linking
GRDC discharge stations with model pixels (`station-pixel_matches.json`)
To re-generate those files, follow the instruction described below.

## Environment variables

```bash
export LOCAL_DIR=/mnt/data/lorentz-models/lisflood
export SETUP_GLOBAL=Lisflood01degree
```

Please note that the full global setup (`Lisflood01degree`) is not publicly available. Please contact the [Lisflood authors](https://ec-jrc.github.io/lisflood-model/) to request access.

## Docker image

The docker image lisflood-grpc4bmi is available [on dockerhub](https://hub.docker.com/r/ewatercycle/lisflood-grpc4bmi).

Alternatively, this image can be re-generated using instructions
at [lisflood readme in era5-comparison repository](https://github.com/eWaterCycle/era5-comparison/tree/master/lisflood).

## Create catchment masks and station-pixel lookup

To re-generate the files, run:

```bash
docker run -ti --user $(id -u) -v /mnt/data/grdc:/grdc -v $LOCAL_DIR/$SETUP_GLOBAL:/setup -v /mnt/data/lorentz-models/lisflood/areamaps:/amaps --entrypoint python3 ewatercycle/lisflood-grpc4bmi:latest /opt/basin_station_processing/match_stations_pixels.py /grdc /opt/recipes_auxiliary_datasets/Lorentz_Basin_Shapefiles /setup /amaps/area.nc
```

Output:

- `$LOCAL_DIR/areamaps/catchment_masks.nc` containing a mask for each catchment, used for forcing pre-processing
- `$LOCAL_DIR/areamaps/model_mask.nc` is the union of all catchment masks, used for running LISVAP and LISFLOOD
- `$LOCAL_DIR/areamaps/station-pixel_matches.json` is the lookup table pairing GRDC stations with model pixels

Given the model river flow direction matrix (`$LOCAL_DIR/$SETUP_GLOBAL/maps_netcdf/ldd.nc`) and [the input basin
shapefiles](https://github.com/eWaterCycle/recipes_auxiliary_datasets/tree/master/Lorentz_Basin_Shapefiles),
each catchment mask is computed as follows:

1. We find the set of model pixels *P* that are within the catchment shapefile polygon;
2. Among *P*, the pixel *p* with the largest upstream (drained) area is selected;
3. The catchment mask consists of all pixels upstream of *p*.
