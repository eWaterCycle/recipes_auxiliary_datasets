# Generate the catchment masks

## Environment variables

```bash
export LOCAL_DIR=/mnt/data/lorentz-models/lisflood
export SETUP_GLOBAL=Lisflood01degree
export GRDC=$LOCAL_DIR/grdc
```

## Build Docker container

```bash
docker build -t ec-jrc/lisflood .
```

## Run Docker

```docker
docker run -ti --user $(id -u) -v $LOCAL_DIR/$SETUP_GLOBAL/maps_netcdf:/maps_netcdf -v $GRDC:/grdc -v $LOCAL_DIR/areamaps:/amaps --entrypoint python3 ec-jrc/lisflood:latest /opt/basin_station_processing/catchment.py /maps_netcdf/ldd.nc /opt/recipes_auxiliary_datasets/Lorentz_Basin_Shapefiles /grdc /amaps
```

Output:

- `$LOCAL_DIR/areamaps/catchment_masks.nc` containing a mask for each catchment, used for forcing pre-processing
- `$LOCAL_DIR/areamaps/model_mask.nc` is the union of all catchment masks, used for running LISVAP and LISFLOOD