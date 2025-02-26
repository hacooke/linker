# Linker

A nether portal linking calculator for Minecraft: resolve conflicts
with portal locations and plan complex inter-connected portal
networks.

This project is in early development, stay tuned for updates.

## To do

Build core systems and associated tests
 * Portal
 * PortalMap
 * ConfigHandler
 * PortalMatcher
     * (This code could be in PortalMap but better to separate the data structure from the algorithm)

Then build up from interface (CLI for now), adding to back-end code as
required.

Take POC code to read world files and use it to generate config files
 + Should be able to update an existing config without removing things
   like portal names, link constraints

Add system for testing proposed portal locations, either given at CLI
or in a (separate?) config

Additional config which constrains which portal much link to which
(option of this being in the same file as location config or different?)
