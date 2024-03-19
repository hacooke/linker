# Linker

A nether portal linking calculator for Minecraft: resolve conflicts
with portal locations and plan complex inter-connected portal
networks.

## Prerequisites

`pip install quads`?

## To do

Start from interface (CLI for now), build up back-end code as
required.

Build linking calculator
 + Relies on nether portal coord storage infrastructure

Build config file system for logging nether portal locations in world

Take POC code to read world files and use it to generate config files
 + Should be able to update an existing config without removing things
   like portal names, link constraints

Add system for testing proposed portal locations, either given at CLI
or in a (separate?) config

Additional config which constrains which portal much link to which
(option of this being in the same file as location config or different?)

All this config stuff probably requires a dedicated class to handle
config files and interpret contents as portal objects
