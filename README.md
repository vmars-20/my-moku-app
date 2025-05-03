# [my-moku-app](https://github.com/vmars-20/my-moku-app)
[vmars_20](https://github.com/vmars-20) [my-moku-app](https://github.com/vmars-20/my-moku-app)

## Moku-ENV
A quick ref for the most common moku env settings


Usage: mokucli download [OPTIONS] FW_VER

  Download bitstreams for a given firmware version

Arguments:
  FW_VER  Firmware version to download  [required]

Options:
  --target PATH         File path to download bitstreams to  [default: .]
  --force / --no-force  Force rewrite by ignoring checksum  [default: no-
                        force]

vmars20@DRP-e1 my-moku-app % mokucli download --target ./bits 601
Downloading latest instruments for firmware version 601...
[##############################] Done!
Verifying download..
Download complete
vmars20@DRP-e1 my-moku-app % find ./bits
./bits
./bits/mokudata-601.tar


#### `MOKU_DATA_PATH` 
You can customize the path to the first-party bitstream files:



## [README-uv](https://www.datacamp.com/tutorial/python-uv)
**README-uv**
`uv sync`

$ uv tool run black hello.py
$ uvx black hello.py

