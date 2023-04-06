# CO2-mini

CO2-miniを利用して温度と二酸化炭素濃度を取得するスクリプト。

muninと組み合わせることで、画像のような監視を行うことができる。

![co2_temp](https://user-images.githubusercontent.com/909444/230387803-07f6e300-2a1c-42f7-9b44-d0027eb1dbab.png)
![co2_ppm](https://user-images.githubusercontent.com/909444/230387799-1be228f7-a559-4d46-90c8-e9555d50066d.png)

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
