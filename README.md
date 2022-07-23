# CO2-mini

## Requirements

- poetry
- yarn

## Install

```sh
yarn install
```

## Run

```sh
poetry run sensor
```

## Munin

Copy `munin/*` to `/etc/munin/plugins` and `alias co2-mini='cd PATH_TO_CO2_MINI && poetry run sensor'`
