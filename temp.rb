#!/usr/bin/ruby

puts File.read("/sys/class/thermal/thermal_zone0/temp").to_i / 1000.0
